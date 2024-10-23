# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.api_endpoint_create_request import ApiEndpointCreateRequest

class TestApiEndpointCreateRequest(unittest.TestCase):
    """ApiEndpointCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiEndpointCreateRequest:
        """Test ApiEndpointCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiEndpointCreateRequest`
        """
        model = ApiEndpointCreateRequest()
        if include_optional:
            return ApiEndpointCreateRequest(
                path = '/api',
                method = GET,
                parameters = [
                    None
                    ],
                request_body = None,
                success_response = None,
                description = 'API Endpoint',
                security_scheme = [
                    ''
                    ]
            )
        else:
            return ApiEndpointCreateRequest(
                path = '/api',
                method = GET,
                description = 'API Endpoint',
        )
        """

    def testApiEndpointCreateRequest(self):
        """Test ApiEndpointCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
