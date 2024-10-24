# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.api_endpoint_update_request import ApiEndpointUpdateRequest

class TestApiEndpointUpdateRequest(unittest.TestCase):
    """ApiEndpointUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiEndpointUpdateRequest:
        """Test ApiEndpointUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiEndpointUpdateRequest`
        """
        model = ApiEndpointUpdateRequest()
        if include_optional:
            return ApiEndpointUpdateRequest(
                path = '0',
                method = 'GET',
                parameters = [
                    None
                    ],
                request_body = None,
                success_response = None,
                description = '0',
                security_scheme = [
                    ''
                    ]
            )
        else:
            return ApiEndpointUpdateRequest(
                path = '0',
                method = 'GET',
                description = '0',
        )
        """

    def testApiEndpointUpdateRequest(self):
        """Test ApiEndpointUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
