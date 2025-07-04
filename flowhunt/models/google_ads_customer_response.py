# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flowhunt.models.bool_char import BoolChar
from flowhunt.models.google_ads_action_type import GoogleAdsActionType
from typing import Optional, Set
from typing_extensions import Self

class GoogleAdsCustomerResponse(BaseModel):
    """
    GoogleAdsCustomerResponse
    """ # noqa: E501
    workspace_id: StrictStr = Field(description="Workspace ID")
    customer_id: StrictStr = Field(description="Google Ads Customer ID")
    customer_name: StrictStr = Field(description="Google Ads Customer Name")
    language_code: StrictStr = Field(description="Language Code")
    country: StrictStr = Field(description="Country Code")
    min_queries: StrictInt = Field(description="Minimum Queries")
    cluster_strength: StrictInt = Field(description="Cluster Strength")
    min_impressions: StrictInt = Field(description="Minimum Impressions")
    min_clicks: StrictInt = Field(description="Minimum Clicks")
    process_negative_keywords: Optional[BoolChar] = None
    last_update: Optional[datetime] = None
    next_update: Optional[datetime] = None
    cron_settings: Optional[StrictStr] = None
    action_type: GoogleAdsActionType = Field(description="Action Type")
    ga_measurement_id: Optional[StrictStr] = None
    ga_api_secret: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["workspace_id", "customer_id", "customer_name", "language_code", "country", "min_queries", "cluster_strength", "min_impressions", "min_clicks", "process_negative_keywords", "last_update", "next_update", "cron_settings", "action_type", "ga_measurement_id", "ga_api_secret"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GoogleAdsCustomerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if process_negative_keywords (nullable) is None
        # and model_fields_set contains the field
        if self.process_negative_keywords is None and "process_negative_keywords" in self.model_fields_set:
            _dict['process_negative_keywords'] = None

        # set to None if last_update (nullable) is None
        # and model_fields_set contains the field
        if self.last_update is None and "last_update" in self.model_fields_set:
            _dict['last_update'] = None

        # set to None if next_update (nullable) is None
        # and model_fields_set contains the field
        if self.next_update is None and "next_update" in self.model_fields_set:
            _dict['next_update'] = None

        # set to None if cron_settings (nullable) is None
        # and model_fields_set contains the field
        if self.cron_settings is None and "cron_settings" in self.model_fields_set:
            _dict['cron_settings'] = None

        # set to None if ga_measurement_id (nullable) is None
        # and model_fields_set contains the field
        if self.ga_measurement_id is None and "ga_measurement_id" in self.model_fields_set:
            _dict['ga_measurement_id'] = None

        # set to None if ga_api_secret (nullable) is None
        # and model_fields_set contains the field
        if self.ga_api_secret is None and "ga_api_secret" in self.model_fields_set:
            _dict['ga_api_secret'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleAdsCustomerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace_id": obj.get("workspace_id"),
            "customer_id": obj.get("customer_id"),
            "customer_name": obj.get("customer_name"),
            "language_code": obj.get("language_code"),
            "country": obj.get("country"),
            "min_queries": obj.get("min_queries"),
            "cluster_strength": obj.get("cluster_strength"),
            "min_impressions": obj.get("min_impressions"),
            "min_clicks": obj.get("min_clicks"),
            "process_negative_keywords": obj.get("process_negative_keywords"),
            "last_update": obj.get("last_update"),
            "next_update": obj.get("next_update"),
            "cron_settings": obj.get("cron_settings"),
            "action_type": obj.get("action_type"),
            "ga_measurement_id": obj.get("ga_measurement_id"),
            "ga_api_secret": obj.get("ga_api_secret")
        })
        return _obj


