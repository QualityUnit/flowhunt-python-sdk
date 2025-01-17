# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.grid_column_update_request import GridColumnUpdateRequest

class TestGridColumnUpdateRequest(unittest.TestCase):
    """GridColumnUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridColumnUpdateRequest:
        """Test GridColumnUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridColumnUpdateRequest`
        """
        model = GridColumnUpdateRequest()
        if include_optional:
            return GridColumnUpdateRequest(
                name = '',
                position = 56,
                data_type = 'T',
                data_type_options = '',
                input_columns = [
                    ''
                    ],
                executor_type = 'S',
                executor_flow_id = '',
                executor_input_template = ''
            )
        else:
            return GridColumnUpdateRequest(
        )
        """

    def testGridColumnUpdateRequest(self):
        """Test GridColumnUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
