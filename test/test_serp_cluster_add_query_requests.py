# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.serp_cluster_add_query_requests import SerpClusterAddQueryRequests

class TestSerpClusterAddQueryRequests(unittest.TestCase):
    """SerpClusterAddQueryRequests unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpClusterAddQueryRequests:
        """Test SerpClusterAddQueryRequests
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpClusterAddQueryRequests`
        """
        model = SerpClusterAddQueryRequests()
        if include_optional:
            return SerpClusterAddQueryRequests(
                requests = [
                    flowhunt.models.serp_cluster_add_query_request.SerpClusterAddQueryRequest(
                        post_back_url = '', 
                        query = '', 
                        country = '', 
                        language = '', 
                        location = '', 
                        group_name = '', 
                        group_id = '', 
                        count_urls = 56, )
                    ]
            )
        else:
            return SerpClusterAddQueryRequests(
                requests = [
                    flowhunt.models.serp_cluster_add_query_request.SerpClusterAddQueryRequest(
                        post_back_url = '', 
                        query = '', 
                        country = '', 
                        language = '', 
                        location = '', 
                        group_name = '', 
                        group_id = '', 
                        count_urls = 56, )
                    ],
        )
        """

    def testSerpClusterAddQueryRequests(self):
        """Test SerpClusterAddQueryRequests"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()