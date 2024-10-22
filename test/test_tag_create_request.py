# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.tag_create_request import TagCreateRequest

class TestTagCreateRequest(unittest.TestCase):
    """TagCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagCreateRequest:
        """Test TagCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagCreateRequest`
        """
        model = TagCreateRequest()
        if include_optional:
            return TagCreateRequest(
                tag_name = 'Tag1',
                tag_color = '#FF0000'
            )
        else:
            return TagCreateRequest(
                tag_name = 'Tag1',
                tag_color = '#FF0000',
        )
        """

    def testTagCreateRequest(self):
        """Test TagCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
