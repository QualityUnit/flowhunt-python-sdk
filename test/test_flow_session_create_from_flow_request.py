# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.flow_session_create_from_flow_request import FlowSessionCreateFromFlowRequest

class TestFlowSessionCreateFromFlowRequest(unittest.TestCase):
    """FlowSessionCreateFromFlowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSessionCreateFromFlowRequest:
        """Test FlowSessionCreateFromFlowRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSessionCreateFromFlowRequest`
        """
        model = FlowSessionCreateFromFlowRequest()
        if include_optional:
            return FlowSessionCreateFromFlowRequest(
                url = '',
                lang = '',
                access_token = '',
                refresh_token = '',
                username = '',
                password = '',
                variables = {
                    'key' : ''
                    },
                flow_id = ''
            )
        else:
            return FlowSessionCreateFromFlowRequest(
                flow_id = '',
        )
        """

    def testFlowSessionCreateFromFlowRequest(self):
        """Test FlowSessionCreateFromFlowRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
