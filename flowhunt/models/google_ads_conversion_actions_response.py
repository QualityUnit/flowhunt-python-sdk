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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from flowhunt.models.google_ads_conversion_action import GoogleAdsConversionAction
from typing import Optional, Set
from typing_extensions import Self

class GoogleAdsConversionActionsResponse(BaseModel):
    """
    GoogleAdsConversionActionsResponse
    """ # noqa: E501
    conversion_actions: List[GoogleAdsConversionAction] = Field(description="List of conversion actions")
    __properties: ClassVar[List[str]] = ["conversion_actions"]

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
        """Create an instance of GoogleAdsConversionActionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conversion_actions (list)
        _items = []
        if self.conversion_actions:
            for _item_conversion_actions in self.conversion_actions:
                if _item_conversion_actions:
                    _items.append(_item_conversion_actions.to_dict())
            _dict['conversion_actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleAdsConversionActionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conversion_actions": [GoogleAdsConversionAction.from_dict(_item) for _item in obj["conversion_actions"]] if obj.get("conversion_actions") is not None else None
        })
        return _obj


