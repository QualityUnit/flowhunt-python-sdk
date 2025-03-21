# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.flow_invoke_request import FlowInvokeRequest

class TestFlowInvokeRequest(unittest.TestCase):
    """FlowInvokeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowInvokeRequest:
        """Test FlowInvokeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowInvokeRequest`
        """
        model = FlowInvokeRequest()
        if include_optional:
            return FlowInvokeRequest(
                post_back_url = '',
                human_input = '',
                variables = {
                    'key' : null
                    }
            )
        else:
            return FlowInvokeRequest(
                human_input = '',
        )
        """

    def testFlowInvokeRequest(self):
        """Test FlowInvokeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
