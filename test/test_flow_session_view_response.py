# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.flow_session_view_response import FlowSessionViewResponse

class TestFlowSessionViewResponse(unittest.TestCase):
    """FlowSessionViewResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSessionViewResponse:
        """Test FlowSessionViewResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSessionViewResponse`
        """
        model = FlowSessionViewResponse()
        if include_optional:
            return FlowSessionViewResponse(
                session_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                chatbot_id = '',
                flow_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                workspace_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_msg_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                msg_count = 56,
                credits = 56,
                chatbot_name = '',
                flow_name = '',
                tags = [
                    ''
                    ],
                duration = 56,
                ipaddress = '',
                url = ''
            )
        else:
            return FlowSessionViewResponse(
                session_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                flow_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                workspace_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testFlowSessionViewResponse(self):
        """Test FlowSessionViewResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
