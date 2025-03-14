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
from flowhunt.models.google_ads_recommendation import GoogleAdsRecommendation
from typing import Optional, Set
from typing_extensions import Self

class GoogleAdsKeywordRecommendation(BaseModel):
    """
    GoogleAdsKeywordRecommendation
    """ # noqa: E501
    workspace_id: StrictStr = Field(description="Workspace ID")
    customer_id: StrictStr = Field(description="Customer ID")
    campaign_id: StrictStr = Field(description="Campaign ID")
    campaign_name: StrictStr = Field(description="Campaign Name")
    group_id: StrictStr = Field(description="Group ID")
    group_name: StrictStr = Field(description="Group Name")
    keyword_id: StrictStr = Field(description="Keyword ID")
    keyword: StrictStr = Field(description="Keyword")
    created_at: Optional[datetime] = None
    recommendations: Optional[List[GoogleAdsRecommendation]] = None
    __properties: ClassVar[List[str]] = ["workspace_id", "customer_id", "campaign_id", "campaign_name", "group_id", "group_name", "keyword_id", "keyword", "created_at", "recommendations"]

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
        """Create an instance of GoogleAdsKeywordRecommendation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recommendations (list)
        _items = []
        if self.recommendations:
            for _item_recommendations in self.recommendations:
                if _item_recommendations:
                    _items.append(_item_recommendations.to_dict())
            _dict['recommendations'] = _items
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if recommendations (nullable) is None
        # and model_fields_set contains the field
        if self.recommendations is None and "recommendations" in self.model_fields_set:
            _dict['recommendations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleAdsKeywordRecommendation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace_id": obj.get("workspace_id"),
            "customer_id": obj.get("customer_id"),
            "campaign_id": obj.get("campaign_id"),
            "campaign_name": obj.get("campaign_name"),
            "group_id": obj.get("group_id"),
            "group_name": obj.get("group_name"),
            "keyword_id": obj.get("keyword_id"),
            "keyword": obj.get("keyword"),
            "created_at": obj.get("created_at"),
            "recommendations": [GoogleAdsRecommendation.from_dict(_item) for _item in obj["recommendations"]] if obj.get("recommendations") is not None else None
        })
        return _obj


