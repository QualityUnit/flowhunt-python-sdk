# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.grig_cell import GrigCell

class TestGrigCell(unittest.TestCase):
    """GrigCell unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GrigCell:
        """Test GrigCell
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GrigCell`
        """
        model = GrigCell()
        if include_optional:
            return GrigCell(
                col_id = '',
                value_text = '',
                value_number = 1.337,
                value_date = 1.337,
                status = 'R',
                status_updated = 1.337
            )
        else:
            return GrigCell(
                col_id = '',
        )
        """

    def testGrigCell(self):
        """Test GrigCell"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
