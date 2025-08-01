# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IntegrationSlug(str, Enum):
    """
    IntegrationSlug
    """

    """
    allowed enum values
    """
    SHOPIFY_INTEGRATION = 'shopify_integration'
    SLACK_INTEGRATION = 'slack_integration'
    HUBSPOT_INTEGRATION = 'hubspot_integration'
    LIVEAGENT_INTEGRATION = 'liveagent_integration'
    HUBSPOT_WIDGET_INTEGRATION = 'hubspot_widget_integration'
    LIVECHAT_INTEGRATION = 'livechat_integration'
    SMARTSUPP_INTEGRATION = 'smartsupp_integration'
    FRESHCHAT_INTEGRATION = 'freshchat_integration'
    TAWK_INTEGRATION = 'tawk_integration'
    GOOGLE_INTEGRATION = 'google_integration'
    WORDPRESS_INTEGRATION = 'wordpress_integration'
    GMAIL_INTEGRATION = 'gmail_integration'
    INSTAGRAM_INTEGRATION = 'instagram_integration'
    MICROSOFT_OUTLOOK_INTEGRATION = 'microsoft_outlook_integration'
    ODOO_INTEGRATION = 'odoo_integration'
    GOOGLE_CALENDAR_INTEGRATION = 'google_calendar_integration'
    GOOGLE_ADS_INTEGRATION = 'google_ads_integration'
    GOOGLE_DOCS_INTEGRATION = 'google_docs_integration'
    GOOGLE_DRIVE_INTEGRATION = 'google_drive_integration'
    GOOGLE_SHEETS_INTEGRATION = 'google_sheets_integration'
    GOOGLE_TASKS_INTEGRATION = 'google_tasks_integration'
    GOOGLE_MEET_INTEGRATION = 'google_meet_integration'
    GOOGLE_SLIDES_INTEGRATION = 'google_slides_integration'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IntegrationSlug from a JSON string"""
        return cls(json.loads(json_str))


