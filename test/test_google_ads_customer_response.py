# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.google_ads_customer_response import GoogleAdsCustomerResponse

class TestGoogleAdsCustomerResponse(unittest.TestCase):
    """GoogleAdsCustomerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoogleAdsCustomerResponse:
        """Test GoogleAdsCustomerResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoogleAdsCustomerResponse`
        """
        model = GoogleAdsCustomerResponse()
        if include_optional:
            return GoogleAdsCustomerResponse(
                workspace_id = '',
                customer_id = 56,
                customer_name = '',
                language_code = '',
                country = '',
                min_queries = 56,
                cluster_strength = 56,
                min_impressions = 56,
                min_clicks = 56,
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                next_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cron_settings = '',
                action_type = 'I',
                ga_measurement_id = ''
            )
        else:
            return GoogleAdsCustomerResponse(
                workspace_id = '',
                customer_id = 56,
                customer_name = '',
                language_code = '',
                country = '',
                min_queries = 56,
                cluster_strength = 56,
                min_impressions = 56,
                min_clicks = 56,
                action_type = 'I',
        )
        """

    def testGoogleAdsCustomerResponse(self):
        """Test GoogleAdsCustomerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
