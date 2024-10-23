# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.tag_response import TagResponse

class TestTagResponse(unittest.TestCase):
    """TagResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TagResponse:
        """Test TagResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TagResponse`
        """
        model = TagResponse()
        if include_optional:
            return TagResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                tag_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                tag_name = 'Tag1',
                tag_color = '#000000'
            )
        else:
            return TagResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                tag_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                tag_name = 'Tag1',
                tag_color = '#000000',
        )
        """

    def testTagResponse(self):
        """Test TagResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
