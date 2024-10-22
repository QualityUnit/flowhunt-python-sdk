# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.prompt_create_request import PromptCreateRequest

class TestPromptCreateRequest(unittest.TestCase):
    """PromptCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PromptCreateRequest:
        """Test PromptCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PromptCreateRequest`
        """
        model = PromptCreateRequest()
        if include_optional:
            return PromptCreateRequest(
                cat_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                name = 'example.pdf',
                description = '',
                prompt_text = 'Prompt text',
                prompt_url = flowhunt-python-sdk.models.app_url.AppUrl(
                    parsed_url = [
                        null
                        ], 
                    url = '', )
            )
        else:
            return PromptCreateRequest(
                cat_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                name = 'example.pdf',
                prompt_text = 'Prompt text',
        )
        """

    def testPromptCreateRequest(self):
        """Test PromptCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()