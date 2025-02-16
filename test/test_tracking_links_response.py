# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.tracking_links_response import TrackingLinksResponse

class TestTrackingLinksResponse(unittest.TestCase):
    """TrackingLinksResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackingLinksResponse:
        """Test TrackingLinksResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackingLinksResponse`
        """
        model = TrackingLinksResponse()
        if include_optional:
            return TrackingLinksResponse(
                links = [
                    flowhunt.models.tracking_link_response.TrackingLinkResponse(
                        src_link_id = '', 
                        dst_link_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valid_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return TrackingLinksResponse(
                links = [
                    flowhunt.models.tracking_link_response.TrackingLinkResponse(
                        src_link_id = '', 
                        dst_link_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valid_until = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testTrackingLinksResponse(self):
        """Test TrackingLinksResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
