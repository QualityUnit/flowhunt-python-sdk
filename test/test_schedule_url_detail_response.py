# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.schedule_url_detail_response import ScheduleUrlDetailResponse

class TestScheduleUrlDetailResponse(unittest.TestCase):
    """ScheduleUrlDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleUrlDetailResponse:
        """Test ScheduleUrlDetailResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleUrlDetailResponse`
        """
        model = ScheduleUrlDetailResponse()
        if include_optional:
            return ScheduleUrlDetailResponse(
                schedule_id = '',
                domain_id = '',
                url_id = '',
                url = '',
                last_text_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                page_screenshot = flowhunt.models.url_screenshot_response.UrlScreenshotResponse(
                    original_image = '', 
                    thumbnail_image = '', ),
                url_title = '',
                url_meta_description = '',
                url_og_image = '',
                is_original_url = True,
                dest_url_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url_text = [
                    {
                        'key' : ''
                        }
                    ]
            )
        else:
            return ScheduleUrlDetailResponse(
                schedule_id = '',
                domain_id = '',
                url_id = '',
                url = '',
                last_text_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                page_screenshot = flowhunt.models.url_screenshot_response.UrlScreenshotResponse(
                    original_image = '', 
                    thumbnail_image = '', ),
                url_title = '',
                url_meta_description = '',
                url_og_image = '',
                is_original_url = True,
                dest_url_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url_text = [
                    {
                        'key' : ''
                        }
                    ],
        )
        """

    def testScheduleUrlDetailResponse(self):
        """Test ScheduleUrlDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
