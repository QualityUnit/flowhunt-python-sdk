# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.flow_session_view_search_request import FlowSessionViewSearchRequest

class TestFlowSessionViewSearchRequest(unittest.TestCase):
    """FlowSessionViewSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSessionViewSearchRequest:
        """Test FlowSessionViewSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSessionViewSearchRequest`
        """
        model = FlowSessionViewSearchRequest()
        if include_optional:
            return FlowSessionViewSearchRequest(
                chatbot_id = '',
                flow_id = '',
                tags = [
                    ''
                    ],
                limit = 56,
                created_at_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return FlowSessionViewSearchRequest(
        )
        """

    def testFlowSessionViewSearchRequest(self):
        """Test FlowSessionViewSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
