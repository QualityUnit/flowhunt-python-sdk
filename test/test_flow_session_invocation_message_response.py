# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.flow_session_invocation_message_response import FlowSessionInvocationMessageResponse

class TestFlowSessionInvocationMessageResponse(unittest.TestCase):
    """FlowSessionInvocationMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSessionInvocationMessageResponse:
        """Test FlowSessionInvocationMessageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSessionInvocationMessageResponse`
        """
        model = FlowSessionInvocationMessageResponse()
        if include_optional:
            return FlowSessionInvocationMessageResponse(
                message_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                response_status = success,
                loading_indicator = flowhunt-python-sdk.models.flow_loading_indicator.FlowLoadingIndicator(
                    tool_name = '', 
                    loading_desc = '', 
                    icon = '', ),
                intermediate_responses = [
                    flowhunt-python-sdk.models.flow_message_response.FlowMessageResponse(
                        message_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 
                        session_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 
                        role = A, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = 'Hello', 
                        credits = 10, )
                    ],
                final_response = [
                    ''
                    ]
            )
        else:
            return FlowSessionInvocationMessageResponse(
                message_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                response_status = success,
        )
        """

    def testFlowSessionInvocationMessageResponse(self):
        """Test FlowSessionInvocationMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
