# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.schedule_response import ScheduleResponse

class TestScheduleResponse(unittest.TestCase):
    """ScheduleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleResponse:
        """Test ScheduleResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleResponse`
        """
        model = ScheduleResponse()
        if include_optional:
            return ScheduleResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                schedule_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                url = 'https://example.com',
                frequency = D,
                schedule_type = D,
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = N,
                status_message = '',
                cnt_scheduled = 56,
                cnt_completed = 56,
                cnt_failed = 56,
                with_screenshot = 'Y',
                with_browser = 'Y',
                follow_links = 'Y',
                with_proxy_rotation = 'Y',
                disallow_urls = '',
                filter_urls = ''
            )
        else:
            return ScheduleResponse(
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                schedule_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                url = 'https://example.com',
                frequency = D,
                schedule_type = D,
                status = N,
                cnt_scheduled = 56,
                cnt_completed = 56,
                cnt_failed = 56,
                with_screenshot = 'Y',
                with_browser = 'Y',
                follow_links = 'Y',
                with_proxy_rotation = 'Y',
        )
        """

    def testScheduleResponse(self):
        """Test ScheduleResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
