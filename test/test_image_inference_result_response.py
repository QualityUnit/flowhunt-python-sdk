# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.image_inference_result_response import ImageInferenceResultResponse

class TestImageInferenceResultResponse(unittest.TestCase):
    """ImageInferenceResultResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageInferenceResultResponse:
        """Test ImageInferenceResultResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageInferenceResultResponse`
        """
        model = ImageInferenceResultResponse()
        if include_optional:
            return ImageInferenceResultResponse(
                results = [
                    flowhunt.models.image_inference_response.ImageInferenceResponse(
                        url = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        prompt = '', )
                    ],
                status = '',
                error_message = ''
            )
        else:
            return ImageInferenceResultResponse(
                results = [
                    flowhunt.models.image_inference_response.ImageInferenceResponse(
                        url = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        prompt = '', )
                    ],
                status = '',
        )
        """

    def testImageInferenceResultResponse(self):
        """Test ImageInferenceResultResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
