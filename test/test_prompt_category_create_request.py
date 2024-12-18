# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.prompt_category_create_request import PromptCategoryCreateRequest

class TestPromptCategoryCreateRequest(unittest.TestCase):
    """PromptCategoryCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PromptCategoryCreateRequest:
        """Test PromptCategoryCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PromptCategoryCreateRequest`
        """
        model = PromptCategoryCreateRequest()
        if include_optional:
            return PromptCategoryCreateRequest(
                cat_name = 'Category1',
                color = '#FF0000',
                description = ''
            )
        else:
            return PromptCategoryCreateRequest(
                cat_name = 'Category1',
                color = '#FF0000',
        )
        """

    def testPromptCategoryCreateRequest(self):
        """Test PromptCategoryCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
