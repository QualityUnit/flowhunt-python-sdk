# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.image_ft_response import ImageFTResponse

class TestImageFTResponse(unittest.TestCase):
    """ImageFTResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageFTResponse:
        """Test ImageFTResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageFTResponse`
        """
        model = ImageFTResponse()
        if include_optional:
            return ImageFTResponse(
                ft_type = i,
                ft_id = '123e4567-e89b-12d3-a456-426614174000',
                name = 'Fine tuning 1'
            )
        else:
            return ImageFTResponse(
                ft_type = i,
                ft_id = '123e4567-e89b-12d3-a456-426614174000',
                name = 'Fine tuning 1',
        )
        """

    def testImageFTResponse(self):
        """Test ImageFTResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
