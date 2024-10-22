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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ChatbotCreateRequest(BaseModel):
    """
    ChatbotCreateRequest
    """ # noqa: E501
    title: Annotated[str, Field(strict=True, max_length=100)]
    description: Optional[StrictStr] = None
    flow_id: Optional[StrictStr] = Field(default=None, description="Chatbot Flow ID")
    status: Annotated[str, Field(strict=True, max_length=1)]
    url_suffix: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    theme: Optional[Annotated[str, Field(strict=True, max_length=1)]] = None
    max_window_size: Optional[Annotated[str, Field(strict=True, max_length=32)]] = None
    msg_rpm: Optional[StrictInt] = None
    msg_ip_rpm: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["title", "description", "flow_id", "status", "url_suffix", "theme", "max_window_size", "msg_rpm", "msg_ip_rpm"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['A', 'I']):
            raise ValueError("must be one of enum values ('A', 'I')")
        return value

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
        """Create an instance of ChatbotCreateRequest from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if url_suffix (nullable) is None
        # and model_fields_set contains the field
        if self.url_suffix is None and "url_suffix" in self.model_fields_set:
            _dict['url_suffix'] = None

        # set to None if theme (nullable) is None
        # and model_fields_set contains the field
        if self.theme is None and "theme" in self.model_fields_set:
            _dict['theme'] = None

        # set to None if max_window_size (nullable) is None
        # and model_fields_set contains the field
        if self.max_window_size is None and "max_window_size" in self.model_fields_set:
            _dict['max_window_size'] = None

        # set to None if msg_rpm (nullable) is None
        # and model_fields_set contains the field
        if self.msg_rpm is None and "msg_rpm" in self.model_fields_set:
            _dict['msg_rpm'] = None

        # set to None if msg_ip_rpm (nullable) is None
        # and model_fields_set contains the field
        if self.msg_ip_rpm is None and "msg_ip_rpm" in self.model_fields_set:
            _dict['msg_ip_rpm'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatbotCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "flow_id": obj.get("flow_id"),
            "status": obj.get("status"),
            "url_suffix": obj.get("url_suffix"),
            "theme": obj.get("theme"),
            "max_window_size": obj.get("max_window_size"),
            "msg_rpm": obj.get("msg_rpm"),
            "msg_ip_rpm": obj.get("msg_ip_rpm")
        })
        return _obj


