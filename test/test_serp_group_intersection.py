# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.serp_group_intersection import SerpGroupIntersection

class TestSerpGroupIntersection(unittest.TestCase):
    """SerpGroupIntersection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpGroupIntersection:
        """Test SerpGroupIntersection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpGroupIntersection`
        """
        model = SerpGroupIntersection()
        if include_optional:
            return SerpGroupIntersection(
                workspace_id = '',
                customer_id = 56,
                campaign_id = 56,
                group_id = 56,
                unique_group_id = '',
                intersections_count = 56
            )
        else:
            return SerpGroupIntersection(
                workspace_id = '',
                customer_id = 56,
                campaign_id = 56,
                group_id = 56,
                intersections_count = 56,
        )
        """

    def testSerpGroupIntersection(self):
        """Test SerpGroupIntersection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
