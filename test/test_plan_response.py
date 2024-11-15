# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.plan_response import PlanResponse

class TestPlanResponse(unittest.TestCase):
    """PlanResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanResponse:
        """Test PlanResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanResponse`
        """
        model = PlanResponse()
        if include_optional:
            return PlanResponse(
                product_id = '',
                price_id = '',
                currency = '',
                amount = 56,
                recurring = True,
                name = '',
                description = '',
                popular = True,
                features = [
                    flowhunt.models.feature_response.FeatureResponse(
                        name = '', 
                        available = True, )
                    ],
                subscription_plan = 'S',
                self_hosted = True
            )
        else:
            return PlanResponse(
                product_id = '',
                price_id = '',
                currency = '',
                amount = 56,
                recurring = True,
                name = '',
                description = '',
                popular = True,
                features = [
                    flowhunt.models.feature_response.FeatureResponse(
                        name = '', 
                        available = True, )
                    ],
                subscription_plan = 'S',
        )
        """

    def testPlanResponse(self):
        """Test PlanResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
