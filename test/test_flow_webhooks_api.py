# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.flow_webhooks_api import FlowWebhooksApi


class TestFlowWebhooksApi(unittest.TestCase):
    """FlowWebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FlowWebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_execute_webhook(self) -> None:
        """Test case for execute_webhook

        Execute Webhook
        """
        pass

    def test_execute_webhook_from_flow(self) -> None:
        """Test case for execute_webhook_from_flow

        Execute Webhook From Flow
        """
        pass

    def test_poll_webhook_response(self) -> None:
        """Test case for poll_webhook_response

        Poll Webhook Response
        """
        pass


if __name__ == '__main__':
    unittest.main()
