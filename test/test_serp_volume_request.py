# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.serp_volume_request import SerpVolumeRequest

class TestSerpVolumeRequest(unittest.TestCase):
    """SerpVolumeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SerpVolumeRequest:
        """Test SerpVolumeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SerpVolumeRequest`
        """
        model = SerpVolumeRequest()
        if include_optional:
            return SerpVolumeRequest(
                post_back_url = '',
                keywords = [
                    ''
                    ],
                language_code = '',
                location_name = '',
                include_adult_keywords = True,
                date_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                date_to = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return SerpVolumeRequest(
                keywords = [
                    ''
                    ],
        )
        """

    def testSerpVolumeRequest(self):
        """Test SerpVolumeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
