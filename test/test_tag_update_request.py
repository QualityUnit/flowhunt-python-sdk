# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.tag_update_request import TagUpdateRequest

class TestTagUpdateRequest(unittest.TestCase):
    """TagUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagUpdateRequest:
        """Test TagUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagUpdateRequest`
        """
        model = TagUpdateRequest()
        if include_optional:
            return TagUpdateRequest(
                tag_name = '',
                tag_color = ''
            )
        else:
            return TagUpdateRequest(
        )
        """

    def testTagUpdateRequest(self):
        """Test TagUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
