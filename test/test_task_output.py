# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.task_output import TaskOutput

class TestTaskOutput(unittest.TestCase):
    """TaskOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskOutput:
        """Test TaskOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskOutput`
        """
        model = TaskOutput()
        if include_optional:
            return TaskOutput(
                description = '',
                name = '',
                expected_output = '',
                summary = '',
                raw = '',
                pydantic = flowhunt.models.base_model.BaseModel(),
                json_dict = {
                    'key' : null
                    },
                agent = '',
                output_format = 'json'
            )
        else:
            return TaskOutput(
                description = '',
                agent = '',
        )
        """

    def testTaskOutput(self):
        """Test TaskOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
