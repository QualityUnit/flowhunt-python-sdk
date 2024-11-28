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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SerpClusterQueryIntersectionsRequest(BaseModel):
    """
    SerpClusterQueryIntersectionsRequest
    """ # noqa: E501
    post_back_url: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    group_name: Optional[StrictStr] = Field(default='', description="Group name of cluster")
    group_id: Optional[StrictStr] = None
    live_mode: Optional[StrictBool] = None
    max_position: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["post_back_url", "query", "country", "language", "location", "group_name", "group_id", "live_mode", "max_position"]

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
        """Create an instance of SerpClusterQueryIntersectionsRequest from a JSON string"""
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

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if group_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_id is None and "group_id" in self.model_fields_set:
            _dict['group_id'] = None

        # set to None if live_mode (nullable) is None
        # and model_fields_set contains the field
        if self.live_mode is None and "live_mode" in self.model_fields_set:
            _dict['live_mode'] = None

        # set to None if max_position (nullable) is None
        # and model_fields_set contains the field
        if self.max_position is None and "max_position" in self.model_fields_set:
            _dict['max_position'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpClusterQueryIntersectionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "post_back_url": obj.get("post_back_url"),
            "query": obj.get("query"),
            "country": obj.get("country"),
            "language": obj.get("language"),
            "location": obj.get("location"),
            "group_name": obj.get("group_name") if obj.get("group_name") is not None else '',
            "group_id": obj.get("group_id"),
            "live_mode": obj.get("live_mode"),
            "max_position": obj.get("max_position")
        })
        return _obj


