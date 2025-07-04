# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.flow_search_request import FlowSearchRequest

class TestFlowSearchRequest(unittest.TestCase):
    """FlowSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSearchRequest:
        """Test FlowSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSearchRequest`
        """
        model = FlowSearchRequest()
        if include_optional:
            return FlowSearchRequest(
                flow_type = 'p',
                name = '',
                category_id = '',
                limit = 56,
                pagination = flowhunt.models.pagination.Pagination(
                    sorting_key_value = '', 
                    scroll_id = '', )
            )
        else:
            return FlowSearchRequest(
        )
        """

    def testFlowSearchRequest(self):
        """Test FlowSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
