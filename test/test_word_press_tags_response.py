# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.word_press_tags_response import WordPressTagsResponse

class TestWordPressTagsResponse(unittest.TestCase):
    """WordPressTagsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WordPressTagsResponse:
        """Test WordPressTagsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WordPressTagsResponse`
        """
        model = WordPressTagsResponse()
        if include_optional:
            return WordPressTagsResponse(
                id = 56,
                name = '',
                slug = '',
                description = '',
                link = '',
                count = 56
            )
        else:
            return WordPressTagsResponse(
                id = 56,
                name = '',
                slug = '',
                description = '',
                link = '',
                count = 56,
        )
        """

    def testWordPressTagsResponse(self):
        """Test WordPressTagsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
