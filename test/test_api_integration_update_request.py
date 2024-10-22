# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.api_integration_update_request import ApiIntegrationUpdateRequest

class TestApiIntegrationUpdateRequest(unittest.TestCase):
    """ApiIntegrationUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiIntegrationUpdateRequest:
        """Test ApiIntegrationUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiIntegrationUpdateRequest`
        """
        model = ApiIntegrationUpdateRequest()
        if include_optional:
            return ApiIntegrationUpdateRequest(
                servers = [
                    ''
                    ],
                name = '0',
                description = '',
                secret = None,
                endpoints = [
                    flowhunt-python-sdk.models.api_endpoint_create_request.ApiEndpointCreateRequest(
                        path = '/api', 
                        method = GET, 
                        parameters = [
                            None
                            ], 
                        request_body = flowhunt-python-sdk.models.request_body.request_body(), 
                        success_response = flowhunt-python-sdk.models.success_response.success_response(), 
                        description = 'API Endpoint', 
                        security_scheme = [
                            ''
                            ], )
                    ]
            )
        else:
            return ApiIntegrationUpdateRequest(
        )
        """

    def testApiIntegrationUpdateRequest(self):
        """Test ApiIntegrationUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
