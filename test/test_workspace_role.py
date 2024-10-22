# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.workspace_role import WorkspaceRole

class TestWorkspaceRole(unittest.TestCase):
    """WorkspaceRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkspaceRole:
        """Test WorkspaceRole
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkspaceRole`
        """
        model = WorkspaceRole()
        if include_optional:
            return WorkspaceRole(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_name = 'My Company 1',
                owner_name = 'John Doe',
                owner_email = 'john.doe@gmail.com',
                role = 'A'
            )
        else:
            return WorkspaceRole(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_name = 'My Company 1',
                owner_name = 'John Doe',
                owner_email = 'john.doe@gmail.com',
                role = 'A',
        )
        """

    def testWorkspaceRole(self):
        """Test WorkspaceRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()