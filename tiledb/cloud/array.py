import multiprocessing
import sys
import urllib
import warnings
import zlib
from typing import Any, Callable, Optional, Sequence, Union

import numpy
import urllib3

from tiledb.cloud import client
from tiledb.cloud import config
from tiledb.cloud import results
from tiledb.cloud import tiledb_cloud_error
from tiledb.cloud import utils
from tiledb.cloud.rest_api import ApiException as GenApiException
from tiledb.cloud.rest_api import models

last_udf_task_id = None


class TaskResult:
    def __init__(self, response, result_format):
        self.response = response
        self.task_id = None
        self.decoder = results.Decoder(result_format)

    def get(self, timeout=None):
        try:
            response: urllib3.HTTPResponse = self.response.get(timeout=timeout)
            res = response.data
        except (GenApiException, multiprocessing.TimeoutError) as exc:
            _maybe_set_last_udf_id(exc)
            raise tiledb_cloud_error.check_exc(exc) from None

        self.task_id = response.getheader(client.TASK_ID_HEADER)

        if res[:2].hex() in ["7801", "785e", "789c", "78da"]:
            try:
                res = zlib.decompress(res)
            except zlib.error:
                raise tiledb_cloud_error.TileDBCloudError(
                    "Failed to decompress (zlib) result object"
                )

        try:
            return self.decoder.decode(res)
        except Exception as e:
            inner_msg = f": {e.args[0]}" if e.args else ""
            raise tiledb_cloud_error.TileDBCloudError(
                f"Failed to load result object{inner_msg}"
            ) from e


class UDFResult(TaskResult):
    def get(self, timeout=None):
        res = super().get(timeout=timeout)

        # Set last udf task id
        global last_udf_task_id
        last_udf_task_id = self.task_id

        return res


class ArrayList:
    def __init__(self):
        """
        This class incrementally builds a list of UDFArrayDetails for use in
        multi array UDFs
        """
        """list[UDFArrayDetails]"""
        self.arrayList = []

    def add(self, uri=None, ranges=None, buffers=None, layout=None):
        """
        Adds an array to list
        """
        if layout is None:
            converted_layout = None
        elif layout.upper() == "R":
            converted_layout = "row-major"
        elif layout.upper() == "C":
            converted_layout = "col-major"
        elif layout.upper() == "G":
            converted_layout = "global-order"
        elif layout.upper() == "U":
            converted_layout = "unordered"

        parse_ranges(ranges)  # check that the ranges are parseable.
        udf_array_details = models.UDFArrayDetails(
            uri=uri,
            ranges=models.QueryRanges(layout=converted_layout, ranges=ranges),
            buffers=buffers,
        )
        self.arrayList.append(udf_array_details)

    def get(self):
        """
        Returns the list of UDFArrayDetails
        """
        return self.arrayList


def info(uri, async_req=False):
    """
    Returns the cloud metadata

    :param async_req: return future instead of results for async support

    :return: metadata object
    """
    (namespace, array_name) = split_uri(uri)
    api_instance = client.client.array_api

    try:
        return api_instance.get_array_metadata(
            namespace=namespace, array=array_name, async_req=async_req
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def list_shared_with(uri, async_req=False):
    """Return array sharing policies"""
    (namespace, array_name) = split_uri(uri)
    api_instance = client.client.array_api

    try:
        return api_instance.get_array_sharing_policies(
            namespace=namespace, array=array_name, async_req=async_req
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def share_array(uri, namespace, permissions, async_req=False):
    """
    Shares array with give namespace and permissions

    :param str namespace:
    :param list(str) permissions:
    :param async_req: return future instead of results for async support
    :return:
    """

    if not isinstance(permissions, list):
        permissions = [permissions]

    for perm in permissions:
        if (
            not perm.lower() == models.ArrayActions.READ
            and not perm.lower() == models.ArrayActions.WRITE
        ):
            raise Exception("Only read or write permissions are accepted")

    (array_namespace, array_name) = split_uri(uri)
    api_instance = client.client.array_api

    try:
        return api_instance.share_array(
            namespace=array_namespace,
            array=array_name,
            array_sharing=models.ArraySharing(namespace=namespace, actions=permissions),
            async_req=async_req,
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def unshare_array(uri, namespace, async_req=False):
    """
    Removes sharing of an array from given namespace

    :param str namespace: namespace to remove shared access to the array
    :param async_req: return future instead of results for async support
    :return:
    :raises: :py:exc:
    """
    return share_array(uri, namespace, list(), async_req=async_req)


def update_info(
    uri,
    array_name=None,
    description=None,
    access_credentials_name=None,
    tags=None,
    async_req=False,
):
    """
    Update an array's info
    :param str namespace: optional username or organization array should be registered under. If unset will default to the user
    :param str array_name: name of array to rename to
    :param str description: optional description
    :param str access_credentials_name: optional name of access credentials to use, if left blank default for namespace will be used
    :param list tags: to update to
    :param str file_type: array represents give file type
    :param str file_properties: set file properties on array
    :param async_req: return future instead of results for async support
    """
    api_instance = client.client.array_api
    (namespace, current_array_name) = split_uri(uri)

    try:
        return api_instance.update_array_metadata(
            namespace=namespace,
            array=current_array_name,
            array_metadata=models.ArrayInfoUpdate(
                description=description,
                name=array_name,
                uri=uri,
                access_credentials_name=access_credentials_name,
                tags=tags,
            ),
            async_req=async_req,
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def update_file_properties(uri, file_type=None, file_properties=None, async_req=False):
    """
    Update an Array to indicate its a file and has given properties. Any properties set are returned with the array info
    :param str uri: uri of array to update
    :param str file_type: file type to set
    :param dict file_properties: dictionary of properties to set
    :return:
    """

    api_instance = client.client.array_api
    (namespace, current_array_name) = split_uri(uri)

    try:
        return api_instance.update_array_metadata(
            namespace=namespace,
            array=current_array_name,
            array_metadata=models.ArrayInfoUpdate(
                file_type=file_type, file_properties=file_properties
            ),
            async_req=async_req,
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def register_array(
    uri,
    namespace=None,
    array_name=None,
    description=None,
    access_credentials_name=None,
    async_req=False,
):
    """
    Register this array with the tiledb cloud service
    :param str namespace: optional username or organization array should be registered under. If unset will default to the user
    :param str array_name: name of array
    :param str description: optional description
    :param str access_credentials_name: optional name of access credentials to use, if left blank default for namespace will be used
    :param async_req: return future instead of results for async support
    """
    api_instance = client.client.array_api

    if namespace is None:
        if config.user is None:
            config.user = client.user_profile()

        namespace = config.user.username

    try:
        return api_instance.register_array(
            namespace=namespace,
            array=uri,
            array_metadata=models.ArrayInfoUpdate(
                description=description,
                name=array_name,
                uri=uri,
                access_credentials_name=access_credentials_name,
            ),
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def deregister_array(uri, async_req=False):
    """
    Deregister the from the tiledb cloud service. This does not physically delete the array, it will remain
    in your bucket. All access to the array and cloud metadata will be removed.

    :param async_req: return future instead of results for async support

    :return success or error
    """
    (namespace, array_name) = split_uri(uri)

    api_instance = client.client.array_api

    try:
        return api_instance.deregister_array(
            namespace=namespace, array=array_name, async_req=async_req
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def delete_array(uri, content_type, async_req=False):
    """
    Deregister the array from the tiledb cloud service, then deletes physical array from disk.
    All access to the array and cloud metadata will be removed.

    :param async_req: return future instead of results for async support

    :return success or error
    """
    (namespace, array_name) = split_uri(uri)

    api_instance = client.client.array_api

    try:
        return api_instance.delete_array(
            namespace=namespace,
            array=array_name,
            content_type=content_type,
            async_req=async_req,
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def array_activity(uri, async_req=False):
    """
    Fetch array activity
    :param uri:
    :param async_req: return future instead of results for async support
    :return:
    """
    (namespace, array_name) = split_uri(uri)

    api_instance = client.client.array_api

    try:
        return api_instance.array_activity_log(
            namespace=namespace, array=array_name, async_req=async_req
        )
    except GenApiException as exc:
        raise tiledb_cloud_error.check_exc(exc) from None


def split_uri(uri):
    """
    Split a URI into namespace and array name

    :param uri: uri to split into namespace and array name
    :param async_req: return future instead of results for async support
    :return: tuple (namespace, array_name)
    """
    parsed = urllib.parse.urlparse(uri)
    if not parsed.scheme == "tiledb":
        raise Exception("Incorrect array uri, must be in tiledb:// scheme")
    return parsed.netloc, parsed.path[1:]


def parse_ranges(ranges):
    """
    Takes a list of the following objects per dimension:

    - scalar index
    - (start,end) tuple
    - list of either of the above types

    :param ranges: list of (scalar, tuple, list)
    :param builder: function taking arguments (dim_idx, start, end)
    :return:
    """

    def make_range(dim_range):
        if isinstance(dim_range, (int, float, numpy.datetime64, numpy.timedelta64)):
            start, end = dim_range, dim_range
        elif isinstance(dim_range, (tuple, list)):
            if len(dim_range) == 0:
                return []
            elif len(dim_range) == 1:
                start, end = dim_range[0]
            elif len(dim_range) == 2:
                start, end = dim_range[0], dim_range[1]
            else:
                raise ValueError("List or tuple has count greater than 2 element")
        elif isinstance(dim_range, slice):
            assert dim_range.step is None, "slice steps are not supported!"
            start, end = dim_range.start, dim_range.stop
        elif dim_range is None:
            return []
        else:
            raise ValueError("Unknown index type! (type: '{}')".format(type(dim_range)))

        # Convert datetimes to int64
        if type(start) == numpy.datetime64 or type(start) == numpy.timedelta64:
            start = start.astype("int64").item()
        if type(end) == numpy.datetime64 or type(end) == numpy.timedelta64:
            end = end.astype("int64").item()

        return [start, end]

    result = list()
    for dim_idx, dim_range in enumerate(ranges):
        dim_list = []
        # TODO handle numpy scalars here?
        if isinstance(
            dim_range, (int, float, tuple, slice, numpy.datetime64, numpy.timedelta64)
        ):
            dim_list.extend(make_range(dim_range))
        elif isinstance(dim_range, list):
            for r in dim_range:
                dim_list.extend(make_range(r))
        elif dim_range is None:
            pass
        else:
            raise ValueError(
                "Unknown subarray/index type! (type: '{}', "
                ", idx: '{}', value: '{}')".format(type(dim_range), dim_idx, dim_range)
            )
        result.append(dim_list)

    return result


def apply_async(
    uri: str,
    func: Union[str, Callable, None] = None,
    ranges: Sequence = (),
    name: Optional[str] = None,
    attrs: Sequence = (),
    layout: Optional[str] = None,
    image_name: str = "default",
    http_compressor: str = "deflate",
    include_source_lines: bool = True,
    task_name: Optional[str] = None,
    v2: bool = True,
    result_format: str = models.ResultFormat.NATIVE,
    result_format_version=None,
    **kwargs: Any,
) -> UDFResult:
    """
    Apply a user defined function to an array, asynchronously.

    :param uri: The ``tiledb://...`` URI of the array to apply the function to.
    :param func: The function to run. This can be either a callable function,
        or the name of a registered user-defined function
    :param ranges: ranges to issue query on
    :param name: Deprecated. If ``func`` is ``None``, the name of the registered
        user-defined function to call.
    :param attrs: list of attributes or dimensions to fetch in query
    :param layout: tiledb query layout
    :param image_name: udf image name to use, useful for testing beta features
    :param http_compressor: set http compressor for results
    :param include_source_lines: True to send the source code of your UDF to
        the server with your request. (This means it can be shown to you
        in stack traces if an error occurs.) False to send only compiled Python
        bytecode.
    :param str task_name: optional name to assign the task
        for logging and audit purposes
    :param bool v2: use v2 array udfs
    :param ResultFormat result_format: result serialization format
    :param str result_format_version: set a format version
        for cloudpickle or arrow IPC
    :param kwargs: named arguments to pass to function
    :return: UDFResult, a future containing the results of the UDF

    **Example**
    >>> import tiledb, tiledb.cloud, numpy
    >>> def median(df):
    ...   return numpy.median(df["a"])
    >>> # Open the array then run the UDF
    >>> tiledb.cloud.array.apply_async("tiledb://TileDB-Inc/quickstart_dense", median, [(0,5), (0,5)], attrs=["a", "b", "c"]).get()
    2.0
    """

    (namespace, array_name) = split_uri(uri)
    api_instance = client.client.udf_api

    if name:
        warnings.warn(
            DeprecationWarning(
                "Use of `name` to set a function name is deprecated. "
                "Pass the function name in `func` instead."
            )
        )
    user_func = _pick_func(func=func, name=name)

    parsed_ranges = parse_ranges(ranges)

    if layout is None:
        converted_layout = None
    elif layout.upper() == "R":
        converted_layout = "row-major"
    elif layout.upper() == "C":
        converted_layout = "col-major"
    elif layout.upper() == "G":
        converted_layout = "global-order"
    elif layout.upper() == "U":
        converted_layout = "unordered"
    else:
        raise ValueError("layout must be one of R, C, G, or U, or unset")

    model_ranges = models.QueryRanges(layout=converted_layout, ranges=parsed_ranges)

    udf_model = models.MultiArrayUDF(
        language=models.UDFLanguage.PYTHON,
        ranges=model_ranges,
        buffers=attrs,
        version="{}.{}.{}".format(
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
        ),
        image_name=image_name,
        task_name=task_name,
        result_format=result_format,
        result_format_version=result_format_version,
    )

    if callable(user_func):
        udf_model._exec = utils.b64_pickle(user_func)
        if include_source_lines:
            udf_model.exec_raw = utils.getsourcelines(user_func)
    else:
        udf_model.udf_info_name = user_func

    if kwargs:
        udf_model.argument = utils.b64_pickle((kwargs,))

    submit_kwargs = {}
    if http_compressor:
        submit_kwargs["accept_encoding"] = http_compressor

    try:
        response = api_instance.submit_udf(
            namespace=namespace,
            array=array_name,
            udf=udf_model,
            async_req=True,
            v2=v2,
            _preload_content=False,  # needed to avoid decoding binary data
            **submit_kwargs,
        )

        return UDFResult(response, result_format=result_format)

    except GenApiException as exc:
        _maybe_set_last_udf_id(exc)
        raise tiledb_cloud_error.check_exc(exc) from None


@utils.signature_of(apply_async)
def apply(*args, **kwargs) -> Any:
    """
    Apply a user defined function to an array, synchronously.

    All arguments are exactly as in :func:`apply_async`.

    **Example:**

    >>> import tiledb, tiledb.cloud, numpy
    >>> def median(df):
    ...   return numpy.median(df["a"])
    >>> # Open the array then run the UDF
    >>> tiledb.cloud.array.apply("tiledb://TileDB-Inc/quickstart_dense", median, [(0,5), (0,5)], attrs=["a", "b", "c"])
    2.0
    """
    return apply_async(*args, **kwargs).get()


def exec_multi_array_udf_async(
    func: Union[str, Callable, None] = None,
    array_list: ArrayList = None,
    namespace: Optional[str] = None,
    name: Optional[str] = None,
    layout=None,
    image_name: str = "default",
    http_compressor: Optional[str] = "deflate",
    include_source_lines: bool = True,
    task_name: Optional[str] = None,
    result_format: str = models.ResultFormat.NATIVE,
    result_format_version=None,
    **kwargs,
) -> UDFResult:
    """
    Apply a user defined function to multiple arrays, asynchronously.

    :param func: The function to run. This can be either a callable function,
        or the name of a registered user-defined function
    :param array_list: The list of arrays to run the function on,
        as an already-built ArrayList object.
    :param namespace: namespace to run udf under
    :param layout: (unused)
    :param image_name: udf image name to use, useful for testing beta features
    :param http_compressor: set http compressor for results
    :param str task_name: optional name to assign the task
        for logging and audit purposes
    :param ResultFormat result_format: result serialization format
    :param str result_format_version: set a format version
        for cloudpickle or arrow IPC
    :param kwargs: named arguments to pass to function
    :return: A future containing the results of the UDF.
    >>> import numpy as np
    >>> from tiledb.cloud import array
    >>> import tiledb.cloud
    >>> dense_array = "tiledb://andreas/quickstart_dense_local"
    >>> sparse_array = "tiledb://andreas/quickstart_sparse_local"
    >>> def median(numpy_ordered_dictionary):
    ...    return np.median(numpy_ordered_dictionary[0]["a"]) + np.median(numpy_ordered_dictionary[1]["a"])
    >>> array_list = array.ArrayList()
    >>> array_list.add(dense_array, [(1, 4), (1, 4)], ["a"])
    >>> array_list.add(sparse_array, [(1, 2), (1, 4)], ["a"])
    >>> namespace = "namespace"
    >>> res = array.exec_multi_array_udf(median, array_list, namespace)
    >>> print("Median Multi UDF:\n{}\n".format(res))
    """
    del layout  # unused

    api_instance = client.client.udf_api

    # If the namespace is not set, we will default to the user's namespace
    if namespace is None:
        # Fetch the client profile for username if it is not already cached
        if config.user is None:
            config.user = client.user_profile()

        namespace = client.find_organization_or_user_for_default_charges(config.user)

    if type(array_list) is not ArrayList:
        raise TypeError(
            f"array_list must be passed as an ArrayList, not {type(array_list)}"
        )
    assert array_list
    arrays = array_list.get()
    if not arrays:
        raise ValueError("must pass at least 1 array to a multi-array UDF")

    user_func = _pick_func(func=func, name=name)
    del name, func

    udf_model = models.MultiArrayUDF(
        language=models.UDFLanguage.PYTHON,
        arrays=arrays,
        version="{}.{}.{}".format(
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
        ),
        image_name=image_name,
        task_name=task_name,
        result_format=result_format,
        result_format_version=result_format_version,
    )

    if callable(user_func):
        udf_model._exec = utils.b64_pickle(user_func)
        if include_source_lines:
            udf_model.exec_raw = utils.getsourcelines(user_func)
    else:
        udf_model.udf_info_name = user_func

    if kwargs:
        udf_model.argument = utils.b64_pickle((kwargs,))

    submit_kwargs = {}
    if http_compressor:
        submit_kwargs["accept_encoding"] = http_compressor

    try:
        response = api_instance.submit_multi_array_udf(
            namespace=namespace,
            udf=udf_model,
            async_req=True,
            _preload_content=False,  # needed to avoid decoding binary data
            **submit_kwargs,
        )

        return UDFResult(response, result_format=result_format)

    except GenApiException as exc:
        _maybe_set_last_udf_id(exc)
        raise tiledb_cloud_error.check_exc(exc) from None


@utils.signature_of(exec_multi_array_udf_async)
def exec_multi_array_udf(*args, **kwargs) -> Any:
    """Apply a user-defined function to multiple arrays, synchronously.

    All arguments are exactly as in :func:`exec_multi_array_udf_async`.
    """
    return exec_multi_array_udf_async(*args, **kwargs).get()


def _pick_func(**kwargs: Union[str, Callable, None]) -> Union[str, Callable]:
    """Extracts the exactly *one* function from the provided arguments.

    Raises an error if either zero or more than one functions is passed.
    Uses the names of the arguments as part of the error message.
    """

    result: Union[str, Callable, None] = None
    count = 0

    for val in kwargs.values():
        if val:
            result = val
            count += 1

    if count != 1:
        names = ", ".join(kwargs)
        raise TypeError(f"exactly 1 of [{names}] must be provided")
    if not callable(result) and type(result) != str or not result:
        raise TypeError(
            "provided function must be a callable or the str name of a UDF, "
            f"not {type(result)}"
        )
    return result


def _maybe_set_last_udf_id(exc: Exception) -> None:
    """Tries to set the last_udf_id from the exception, if present."""
    global last_udf_task_id
    try:
        hdrs = getattr(exc, "headers")
        if hdrs:
            task_id = hdrs.get(client.TASK_ID_HEADER)
            if task_id:
                last_udf_task_id = task_id
    except KeyError:
        pass
