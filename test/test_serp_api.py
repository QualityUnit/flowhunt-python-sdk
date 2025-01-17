# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.api.serp_api import SERPApi


class TestSERPApi(unittest.TestCase):
    """SERPApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SERPApi()

    def tearDown(self) -> None:
        pass

    def test_search_cluster_group(self) -> None:
        """Test case for search_cluster_group

        Search Cluster Group
        """
        pass

    def test_search_cluster_query(self) -> None:
        """Test case for search_cluster_query

        Search Cluster Query
        """
        pass

    def test_serp_cluster_add_group(self) -> None:
        """Test case for serp_cluster_add_group

        Serp Cluster Add Group
        """
        pass

    def test_serp_cluster_add_queries(self) -> None:
        """Test case for serp_cluster_add_queries

        Serp Cluster Add Queries
        """
        pass

    def test_serp_cluster_bulk_delete_queries(self) -> None:
        """Test case for serp_cluster_bulk_delete_queries

        Serp Cluster Bulk Delete Queries
        """
        pass

    def test_serp_cluster_delete_all(self) -> None:
        """Test case for serp_cluster_delete_all

        Serp Cluster Delete All
        """
        pass

    def test_serp_cluster_delete_group(self) -> None:
        """Test case for serp_cluster_delete_group

        Serp Cluster Delete Group
        """
        pass

    def test_serp_cluster_delete_query(self) -> None:
        """Test case for serp_cluster_delete_query

        Serp Cluster Delete Query
        """
        pass

    def test_serp_cluster_get_bulk_query_intersections(self) -> None:
        """Test case for serp_cluster_get_bulk_query_intersections

        Serp Cluster Get Bulk Query Intersections
        """
        pass

    def test_serp_cluster_get_query_intersections(self) -> None:
        """Test case for serp_cluster_get_query_intersections

        Serp Cluster Get Query Intersections
        """
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
