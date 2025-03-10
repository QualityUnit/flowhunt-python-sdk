# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.google_ads_source_tracking_code_examples_response import GoogleAdsSourceTrackingCodeExamplesResponse

class TestGoogleAdsSourceTrackingCodeExamplesResponse(unittest.TestCase):
    """GoogleAdsSourceTrackingCodeExamplesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleAdsSourceTrackingCodeExamplesResponse:
        """Test GoogleAdsSourceTrackingCodeExamplesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleAdsSourceTrackingCodeExamplesResponse`
        """
        model = GoogleAdsSourceTrackingCodeExamplesResponse()
        if include_optional:
            return GoogleAdsSourceTrackingCodeExamplesResponse(
                examples = [
                    flowhunt.models.google_ads_source_tracking_code_example.GoogleAdsSourceTrackingCodeExample(
                        customer_id = '', 
                        customer_name = '', 
                        tracking_code = '', 
                        description = '', )
                    ]
            )
        else:
            return GoogleAdsSourceTrackingCodeExamplesResponse(
                examples = [
                    flowhunt.models.google_ads_source_tracking_code_example.GoogleAdsSourceTrackingCodeExample(
                        customer_id = '', 
                        customer_name = '', 
                        tracking_code = '', 
                        description = '', )
                    ],
        )
        """

    def testGoogleAdsSourceTrackingCodeExamplesResponse(self):
        """Test GoogleAdsSourceTrackingCodeExamplesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
