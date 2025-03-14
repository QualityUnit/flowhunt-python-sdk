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
from flowhunt.models.log_entry_level import LogEntryLevel
from flowhunt.models.log_entry_type import LogEntryType
from typing import Optional, Set
from typing_extensions import Self

class LogResponse(BaseModel):
    """
    LogResponse
    """ # noqa: E501
    log_id: StrictStr = Field(description="Unique identifier for the log entry")
    log_type: LogEntryType = Field(description="Type of log (e.g., 'system', 'application', 'user')")
    category_id: Optional[StrictStr] = None
    log_level: LogEntryLevel = Field(description="Log level (e.g., 'info', 'warning', 'error', 'debug')")
    message: StrictStr = Field(description="Log message content")
    created_at: datetime = Field(description="Timestamp when the log was created")
    metadata: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["log_id", "log_type", "category_id", "log_level", "message", "created_at", "metadata"]

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
        """Create an instance of LogResponse from a JSON string"""
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
        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LogResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "log_id": obj.get("log_id"),
            "log_type": obj.get("log_type"),
            "category_id": obj.get("category_id"),
            "log_level": obj.get("log_level"),
            "message": obj.get("message"),
            "created_at": obj.get("created_at"),
            "metadata": obj.get("metadata")
        })
        return _obj


