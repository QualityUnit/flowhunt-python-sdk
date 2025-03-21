# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.serp_cluster_add_query_request import SerpClusterAddQueryRequest

class TestSerpClusterAddQueryRequest(unittest.TestCase):
    """SerpClusterAddQueryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpClusterAddQueryRequest:
        """Test SerpClusterAddQueryRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpClusterAddQueryRequest`
        """
        model = SerpClusterAddQueryRequest()
        if include_optional:
            return SerpClusterAddQueryRequest(
                post_back_url = '',
                queries = [
                    flowhunt.models.serp_keyword.SerpKeyword(
                        keyword_id = '', 
                        keyword = '', 
                        language = '', 
                        country = '', 
                        search_engine = 'G', )
                    ],
                customer_id = '',
                campaign_id = '',
                group_id = '',
                group_name = ''
            )
        else:
            return SerpClusterAddQueryRequest(
                queries = [
                    flowhunt.models.serp_keyword.SerpKeyword(
                        keyword_id = '', 
                        keyword = '', 
                        language = '', 
                        country = '', 
                        search_engine = 'G', )
                    ],
        )
        """

    def testSerpClusterAddQueryRequest(self):
        """Test SerpClusterAddQueryRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
