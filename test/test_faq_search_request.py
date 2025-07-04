# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.faq_search_request import FaqSearchRequest

class TestFaqSearchRequest(unittest.TestCase):
    """FaqSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FaqSearchRequest:
        """Test FaqSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FaqSearchRequest`
        """
        model = FaqSearchRequest()
        if include_optional:
            return FaqSearchRequest(
                faq_id = '',
                status = 'N',
                cat_id = '',
                question = '',
                answer = '',
                parent_faq_id = '',
                faq_type = 'P',
                limit = 56,
                pagination = flowhunt.models.pagination.Pagination(
                    sorting_key_value = '', 
                    scroll_id = '', )
            )
        else:
            return FaqSearchRequest(
        )
        """

    def testFaqSearchRequest(self):
        """Test FaqSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
