# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.api_integration_response import ApiIntegrationResponse

class TestApiIntegrationResponse(unittest.TestCase):
    """ApiIntegrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiIntegrationResponse:
        """Test ApiIntegrationResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiIntegrationResponse`
        """
        model = ApiIntegrationResponse()
        if include_optional:
            return ApiIntegrationResponse(
                integration_id = '123e4567-e89b-12d3-a456-426614174000',
                servers = [https://api.com],
                name = 'API Integration',
                description = 'API Integration',
                secret = None
            )
        else:
            return ApiIntegrationResponse(
                integration_id = '123e4567-e89b-12d3-a456-426614174000',
                servers = [https://api.com],
                name = 'API Integration',
                description = 'API Integration',
                secret = None,
        )
        """

    def testApiIntegrationResponse(self):
        """Test ApiIntegrationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()