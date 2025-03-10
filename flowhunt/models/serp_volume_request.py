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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SerpVolumeRequest(BaseModel):
    """
    SerpVolumeRequest
    """ # noqa: E501
    post_back_url: Optional[StrictStr] = None
    keywords: List[StrictStr] = Field(description="List of queries")
    language_code: Optional[StrictStr] = None
    location_name: Optional[StrictStr] = None
    include_adult_keywords: Optional[StrictBool] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    __properties: ClassVar[List[str]] = ["post_back_url", "keywords", "language_code", "location_name", "include_adult_keywords", "date_from", "date_to"]

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
        """Create an instance of SerpVolumeRequest from a JSON string"""
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
        # set to None if post_back_url (nullable) is None
        # and model_fields_set contains the field
        if self.post_back_url is None and "post_back_url" in self.model_fields_set:
            _dict['post_back_url'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if include_adult_keywords (nullable) is None
        # and model_fields_set contains the field
        if self.include_adult_keywords is None and "include_adult_keywords" in self.model_fields_set:
            _dict['include_adult_keywords'] = None

        # set to None if date_from (nullable) is None
        # and model_fields_set contains the field
        if self.date_from is None and "date_from" in self.model_fields_set:
            _dict['date_from'] = None

        # set to None if date_to (nullable) is None
        # and model_fields_set contains the field
        if self.date_to is None and "date_to" in self.model_fields_set:
            _dict['date_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpVolumeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "post_back_url": obj.get("post_back_url"),
            "keywords": obj.get("keywords"),
            "language_code": obj.get("language_code"),
            "location_name": obj.get("location_name"),
            "include_adult_keywords": obj.get("include_adult_keywords"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to")
        })
        return _obj


