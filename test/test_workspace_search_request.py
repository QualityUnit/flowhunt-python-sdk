# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.workspace_search_request import WorkspaceSearchRequest

class TestWorkspaceSearchRequest(unittest.TestCase):
    """WorkspaceSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceSearchRequest:
        """Test WorkspaceSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceSearchRequest`
        """
        model = WorkspaceSearchRequest()
        if include_optional:
            return WorkspaceSearchRequest(
                name = ''
            )
        else:
            return WorkspaceSearchRequest(
        )
        """

    def testWorkspaceSearchRequest(self):
        """Test WorkspaceSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
