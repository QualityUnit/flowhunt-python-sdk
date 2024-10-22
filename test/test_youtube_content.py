# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.youtube_content import YoutubeContent

class TestYoutubeContent(unittest.TestCase):
    """YoutubeContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> YoutubeContent:
        """Test YoutubeContent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `YoutubeContent`
        """
        model = YoutubeContent()
        if include_optional:
            return YoutubeContent(
                url = '',
                img_url = '',
                status_code = 56,
                created_at = 1.337,
                published_at = 1.337,
                title = '',
                lang = '',
                content_type = '',
                encoding = '',
                description = '',
                content = '',
                metadata = None,
                alt_content = [
                    ''
                    ],
                content_hash = '',
                author = '',
                channel_id = '',
                channel_url = '',
                channel_title = '',
                duration = 56,
                keywords = [
                    ''
                    ],
                doc_type = 'PDF',
                credits = 56
            )
        else:
            return YoutubeContent(
        )
        """

    def testYoutubeContent(self):
        """Test YoutubeContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
