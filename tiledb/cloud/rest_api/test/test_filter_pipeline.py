# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rest_api
from tiledb.cloud.rest_api.models.filter_pipeline import FilterPipeline  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestFilterPipeline(unittest.TestCase):
    """FilterPipeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FilterPipeline
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.filter_pipeline.FilterPipeline()  # noqa: E501
        if include_optional:
            return FilterPipeline(
                filters=[
                    tiledb.cloud.rest_api.models.filter.Filter(
                        type="FILTER_NONE",
                        data=tiledb.cloud.rest_api.models.filter_data.Filter_data(
                            int8=56,
                            uint8=56,
                            int16=56,
                            uint16=56,
                            int32=56,
                            uint32=56,
                            int64=56,
                            uint64=56,
                            float32=56,
                            float64=56,
                        ),
                    )
                ]
            )
        else:
            return FilterPipeline()

    def testFilterPipeline(self):
        """Test FilterPipeline"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
