# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.google_ads_analyze_keywords_request import GoogleAdsAnalyzeKeywordsRequest

class TestGoogleAdsAnalyzeKeywordsRequest(unittest.TestCase):
    """GoogleAdsAnalyzeKeywordsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleAdsAnalyzeKeywordsRequest:
        """Test GoogleAdsAnalyzeKeywordsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleAdsAnalyzeKeywordsRequest`
        """
        model = GoogleAdsAnalyzeKeywordsRequest()
        if include_optional:
            return GoogleAdsAnalyzeKeywordsRequest(
                customer_id = '',
                campaign_id = '',
                group_id = '',
                date_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                force_update = True
            )
        else:
            return GoogleAdsAnalyzeKeywordsRequest(
        )
        """

    def testGoogleAdsAnalyzeKeywordsRequest(self):
        """Test GoogleAdsAnalyzeKeywordsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
