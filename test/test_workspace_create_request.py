# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.workspace_create_request import WorkspaceCreateRequest

class TestWorkspaceCreateRequest(unittest.TestCase):
    """WorkspaceCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceCreateRequest:
        """Test WorkspaceCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceCreateRequest`
        """
        model = WorkspaceCreateRequest()
        if include_optional:
            return WorkspaceCreateRequest(
                name = ''
            )
        else:
            return WorkspaceCreateRequest(
                name = '',
        )
        """

    def testWorkspaceCreateRequest(self):
        """Test WorkspaceCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
