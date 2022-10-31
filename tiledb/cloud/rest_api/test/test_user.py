# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.2.19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import tiledb.cloud.rest_api
from tiledb.cloud.rest_api.models.user import User  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = tiledb.cloud.rest_api.models.user.User()  # noqa: E501
        if include_optional:
            return User(
                id="00000000-0000-0000-0000-000000000000",
                username="username",
                password="password",
                name="Jane Doe",
                email="jane.doe@example.com",
                is_valid_email=False,
                stripe_connect=False,
                company="TileDB",
                logo="0",
                last_activity_date=datetime.datetime.strptime(
                    "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                ),
                timezone="Europe/Athens",
                organizations=[
                    tiledb.cloud.rest_api.models.organization_user.OrganizationUser(
                        user_id="00000000-0000-0000-0000-000000000000",
                        organization_id="00000000-0000-0000-0000-000000000000",
                        username="username",
                        organization_name="MyOrganization",
                        role="owner",
                        allowed_actions=["read"],
                    )
                ],
                allowed_actions=["read"],
                enabled_features=["0"],
                unpaid_subscription=True,
                default_s3_path="0",
                default_s3_path_credentials_name=None,
                asset_locations=tiledb.cloud.rest_api.models.asset_locations.AssetLocations(
                    arrays=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    files=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    groups=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    ml_models=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    notebooks=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    task_graphs=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                    udfs=tiledb.cloud.rest_api.models.storage_location.StorageLocation(
                        path="0",
                        credentials_name="0",
                    ),
                ),
                default_namespace_charged="0",
            )
        else:
            return User(
                username="username",
            )

    def testUser(self):
        """Test User"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
