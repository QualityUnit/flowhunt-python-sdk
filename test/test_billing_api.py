# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingApi()

    def tearDown(self) -> None:
        pass

    def test_create_change_plan_portal(self) -> None:
        """Test case for create_change_plan_portal

        Create Change Plan Portal
        """
        pass

    def test_create_checkout(self) -> None:
        """Test case for create_checkout

        Create Checkout
        """
        pass

    def test_create_update_info_portal(self) -> None:
        """Test case for create_update_info_portal

        Create Update Info Portal
        """
        pass

    def test_get_pricing_plans(self) -> None:
        """Test case for get_pricing_plans

        Get Pricing Plans
        """
        pass

    def test_get_user_plan(self) -> None:
        """Test case for get_user_plan

        Get User Plan
        """
        pass

    def test_stripe_webhook(self) -> None:
        """Test case for stripe_webhook

        Stripe Webhook
        """
        pass


if __name__ == '__main__':
    unittest.main()