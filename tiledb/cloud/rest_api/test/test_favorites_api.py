# coding: utf-8

"""
    TileDB Storage Platform API

    TileDB Storage Platform REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rest_api
from tiledb.cloud.rest_api.api.favorites_api import FavoritesApi  # noqa: E501
from tiledb.cloud.rest_api.rest import ApiException


class TestFavoritesApi(unittest.TestCase):
    """FavoritesApi unit test stubs"""

    def setUp(self):
        self.api = tiledb.cloud.rest_api.api.favorites_api.FavoritesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_favorite_id(self):
        """Test case for delete_favorite_id"""
        pass

    def test_get_favorite(self):
        """Test case for get_favorite"""
        pass

    def test_get_favorites(self):
        """Test case for get_favorites"""
        pass

    def test_post_favorite(self):
        """Test case for post_favorite"""
        pass


if __name__ == "__main__":
    unittest.main()