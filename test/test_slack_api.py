# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.api.slack_api import SlackApi


class TestSlackApi(unittest.TestCase):
    """SlackApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SlackApi()

    def tearDown(self) -> None:
        pass

    def test_get_slack_channels(self) -> None:
        """Test case for get_slack_channels

        Get Slack Channels
        """
        pass

    def test_get_slack_workspaces(self) -> None:
        """Test case for get_slack_workspaces

        Get Slack Workspaces
        """
        pass


if __name__ == '__main__':
    unittest.main()
