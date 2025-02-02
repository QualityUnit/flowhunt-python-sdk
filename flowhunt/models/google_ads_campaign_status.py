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


class GoogleAdsCampaignStatus(int, Enum):
    """
    The possible statuses of an ad group.
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_4 = 4

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GoogleAdsCampaignStatus from a JSON string"""
        return cls(json.loads(json_str))


