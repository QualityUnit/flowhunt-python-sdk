# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.google_ads_campaigns_response import GoogleAdsCampaignsResponse

class TestGoogleAdsCampaignsResponse(unittest.TestCase):
    """GoogleAdsCampaignsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleAdsCampaignsResponse:
        """Test GoogleAdsCampaignsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleAdsCampaignsResponse`
        """
        model = GoogleAdsCampaignsResponse()
        if include_optional:
            return GoogleAdsCampaignsResponse(
                campaigns = [
                    flowhunt.models.google_ads_campaign_response.GoogleAdsCampaignResponse(
                        workspace_id = '', 
                        customer_id = '', 
                        campaign_id = '', 
                        campaign_name = '', 
                        campaign_status = 0, 
                        language_code = '', 
                        country = '', 
                        last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        action_type = 'I', )
                    ]
            )
        else:
            return GoogleAdsCampaignsResponse(
                campaigns = [
                    flowhunt.models.google_ads_campaign_response.GoogleAdsCampaignResponse(
                        workspace_id = '', 
                        customer_id = '', 
                        campaign_id = '', 
                        campaign_name = '', 
                        campaign_status = 0, 
                        language_code = '', 
                        country = '', 
                        last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        action_type = 'I', )
                    ],
        )
        """

    def testGoogleAdsCampaignsResponse(self):
        """Test GoogleAdsCampaignsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
