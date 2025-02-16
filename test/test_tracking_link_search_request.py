# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.tracking_link_search_request import TrackingLinkSearchRequest

class TestTrackingLinkSearchRequest(unittest.TestCase):
    """TrackingLinkSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackingLinkSearchRequest:
        """Test TrackingLinkSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackingLinkSearchRequest`
        """
        model = TrackingLinkSearchRequest()
        if include_optional:
            return TrackingLinkSearchRequest(
                src_link_id = '',
                dst_link_id = '',
                from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                to_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                include_expired = True,
                page = 1.0,
                page_size = 1.0
            )
        else:
            return TrackingLinkSearchRequest(
        )
        """

    def testTrackingLinkSearchRequest(self):
        """Test TrackingLinkSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
