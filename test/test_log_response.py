# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.log_response import LogResponse

class TestLogResponse(unittest.TestCase):
    """LogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogResponse:
        """Test LogResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogResponse`
        """
        model = LogResponse()
        if include_optional:
            return LogResponse(
                log_id = '',
                log_type = 'S',
                category_id = '',
                log_level = 'I',
                message = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                metadata = {
                    'key' : null
                    }
            )
        else:
            return LogResponse(
                log_id = '',
                log_type = 'S',
                log_level = 'I',
                message = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testLogResponse(self):
        """Test LogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
