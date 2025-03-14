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
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyResponse(BaseModel):
    """
    ApiKeyResponse
    """ # noqa: E501
    workspace_id: StrictStr = Field(description="Workspace ID")
    api_key_id: StrictStr = Field(description="API Key ID")
    display_name: StrictStr = Field(description="Name of the API key")
    mask: StrictStr = Field(description="Masked API Key")
    last_used: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["workspace_id", "api_key_id", "display_name", "mask", "last_used", "valid_to"]

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
        """Create an instance of ApiKeyResponse from a JSON string"""
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
        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['last_used'] = None

        # set to None if valid_to (nullable) is None
        # and model_fields_set contains the field
        if self.valid_to is None and "valid_to" in self.model_fields_set:
            _dict['valid_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKeyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "workspace_id": obj.get("workspace_id"),
            "api_key_id": obj.get("api_key_id"),
            "display_name": obj.get("display_name"),
            "mask": obj.get("mask"),
            "last_used": obj.get("last_used"),
            "valid_to": obj.get("valid_to")
        })
        return _obj


