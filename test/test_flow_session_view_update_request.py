# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.flow_session_view_update_request import FlowSessionViewUpdateRequest

class TestFlowSessionViewUpdateRequest(unittest.TestCase):
    """FlowSessionViewUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowSessionViewUpdateRequest:
        """Test FlowSessionViewUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowSessionViewUpdateRequest`
        """
        model = FlowSessionViewUpdateRequest()
        if include_optional:
            return FlowSessionViewUpdateRequest(
                tags = [tag1, tag2]
            )
        else:
            return FlowSessionViewUpdateRequest(
        )
        """

    def testFlowSessionViewUpdateRequest(self):
        """Test FlowSessionViewUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
