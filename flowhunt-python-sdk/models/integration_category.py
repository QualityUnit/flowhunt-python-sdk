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


class IntegrationCategory(str, Enum):
    """
    IntegrationCategory
    """

    """
    allowed enum values
    """
    DEV_TOOLS = 'dev_tools'
    CRM = 'crm'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IntegrationCategory from a JSON string"""
        return cls(json.loads(json_str))


