# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.api_key_response import ApiKeyResponse

class TestApiKeyResponse(unittest.TestCase):
    """ApiKeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeyResponse:
        """Test ApiKeyResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeyResponse`
        """
        model = ApiKeyResponse()
        if include_optional:
            return ApiKeyResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                api_key_id = '0x1d230dabdb5bc7cb',
                display_name = 'My API Key',
                mask = 'd71*****-****-****-****-*********384',
                last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiKeyResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                api_key_id = '0x1d230dabdb5bc7cb',
                display_name = 'My API Key',
                mask = 'd71*****-****-****-****-*********384',
        )
        """

    def testApiKeyResponse(self):
        """Test ApiKeyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
