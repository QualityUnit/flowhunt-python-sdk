# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.images_api import ImagesApi


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ImagesApi()

    def tearDown(self) -> None:
        pass

    def test_convert_image(self) -> None:
        """Test case for convert_image

        Convert Image
        """
        pass

    def test_get_screenshot(self) -> None:
        """Test case for get_screenshot

        Get Screenshot
        """
        pass

    def test_optimize_image(self) -> None:
        """Test case for optimize_image

        Optimize Image
        """
        pass


if __name__ == '__main__':
    unittest.main()