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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flowhunt.models.google_ads_action_type import GoogleAdsActionType
from flowhunt.models.google_ads_group_status import GoogleAdsGroupStatus
from typing import Optional, Set
from typing_extensions import Self

class GoogleAdsGroupResponse(BaseModel):
    """
    GoogleAdsGroupResponse
    """ # noqa: E501
    workspace_id: StrictStr = Field(description="Workspace ID")
    customer_id: StrictStr = Field(description="Google Ads Customer ID")
    campaign_id: StrictStr = Field(description="Google Ads Campaign ID")
    group_id: StrictStr = Field(description="Google Ads Group")
    group_name: StrictStr = Field(description="Google Ads Group Name")
    group_status: GoogleAdsGroupStatus = Field(description="Group Status")
    last_update: Optional[datetime] = None
    action_type: GoogleAdsActionType = Field(description="Action Type")
    language_code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["workspace_id", "customer_id", "campaign_id", "group_id", "group_name", "group_status", "last_update", "action_type", "language_code", "country"]

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
        """Create an instance of GoogleAdsGroupResponse from a JSON string"""
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
        # set to None if last_update (nullable) is None
        # and model_fields_set contains the field
        if self.last_update is None and "last_update" in self.model_fields_set:
            _dict['last_update'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleAdsGroupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace_id": obj.get("workspace_id"),
            "customer_id": obj.get("customer_id"),
            "campaign_id": obj.get("campaign_id"),
            "group_id": obj.get("group_id"),
            "group_name": obj.get("group_name"),
            "group_status": obj.get("group_status"),
            "last_update": obj.get("last_update"),
            "action_type": obj.get("action_type"),
            "language_code": obj.get("language_code"),
            "country": obj.get("country")
        })
        return _obj


