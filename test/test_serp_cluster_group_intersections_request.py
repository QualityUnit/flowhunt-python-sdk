# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.serp_cluster_group_intersections_request import SerpClusterGroupIntersectionsRequest

class TestSerpClusterGroupIntersectionsRequest(unittest.TestCase):
    """SerpClusterGroupIntersectionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpClusterGroupIntersectionsRequest:
        """Test SerpClusterGroupIntersectionsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpClusterGroupIntersectionsRequest`
        """
        model = SerpClusterGroupIntersectionsRequest()
        if include_optional:
            return SerpClusterGroupIntersectionsRequest(
                customer_id = 56,
                campaign_id = 56,
                group_id = 56,
                min_cluster_strength = 56,
                suggest_other_matching_keywords = True
            )
        else:
            return SerpClusterGroupIntersectionsRequest(
                customer_id = 56,
        )
        """

    def testSerpClusterGroupIntersectionsRequest(self):
        """Test SerpClusterGroupIntersectionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
