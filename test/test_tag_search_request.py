# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.tag_search_request import TagSearchRequest

class TestTagSearchRequest(unittest.TestCase):
    """TagSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagSearchRequest:
        """Test TagSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagSearchRequest`
        """
        model = TagSearchRequest()
        if include_optional:
            return TagSearchRequest(
                tag_id = '',
                tag_name = '',
                limit = 56
            )
        else:
            return TagSearchRequest(
        )
        """

    def testTagSearchRequest(self):
        """Test TagSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
