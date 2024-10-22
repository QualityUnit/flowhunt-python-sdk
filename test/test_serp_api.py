# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.serp_api import SERPApi


class TestSERPApi(unittest.TestCase):
    """SERPApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SERPApi()

    def tearDown(self) -> None:
        pass

    def test_serp_search(self) -> None:
        """Test case for serp_search

        Serp Search
        """
        pass

    def test_serp_volumes(self) -> None:
        """Test case for serp_volumes

        Serp Volumes
        """
        pass

    def test_serp_volumes_pingback(self) -> None:
        """Test case for serp_volumes_pingback

        Serp Volumes Pingback
        """
        pass


if __name__ == '__main__':
    unittest.main()
