# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.grid_row_response import GridRowResponse

class TestGridRowResponse(unittest.TestCase):
    """GridRowResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridRowResponse:
        """Test GridRowResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridRowResponse`
        """
        model = GridRowResponse()
        if include_optional:
            return GridRowResponse(
                workspace_id = '',
                grid_id = '',
                row_id = '',
                created = 1.337,
                cells = [
                    flowhunt.models.grig_cell.GrigCell(
                        col_id = '', 
                        value_text = '', 
                        value_number = 1.337, 
                        value_date = 1.337, 
                        status = 'R', 
                        status_updated = 1.337, )
                    ]
            )
        else:
            return GridRowResponse(
                workspace_id = '',
                grid_id = '',
                row_id = '',
                created = 1.337,
        )
        """

    def testGridRowResponse(self):
        """Test GridRowResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()