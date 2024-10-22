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
from typing import Optional, Set
from typing_extensions import Self

class FlowSessionViewResponse(BaseModel):
    """
    FlowSessionViewResponse
    """ # noqa: E501
    session_id: StrictStr = Field(description="Session ID")
    chatbot_id: Optional[StrictStr] = None
    flow_id: StrictStr = Field(description="Flow ID")
    workspace_id: StrictStr = Field(description="Workspace ID")
    created_at: datetime = Field(description="Created at")
    last_msg_at: Optional[datetime] = None
    msg_count: Optional[StrictInt] = None
    credits: Optional[StrictInt] = None
    chatbot_name: Optional[StrictStr] = None
    flow_name: Optional[StrictStr] = None
    tags: Optional[List[StrictStr]] = None
    duration: Optional[StrictInt] = None
    ipaddress: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["session_id", "chatbot_id", "flow_id", "workspace_id", "created_at", "last_msg_at", "msg_count", "credits", "chatbot_name", "flow_name", "tags", "duration", "ipaddress", "url"]

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
        """Create an instance of FlowSessionViewResponse from a JSON string"""
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
        # set to None if chatbot_id (nullable) is None
        # and model_fields_set contains the field
        if self.chatbot_id is None and "chatbot_id" in self.model_fields_set:
            _dict['chatbot_id'] = None

        # set to None if last_msg_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_msg_at is None and "last_msg_at" in self.model_fields_set:
            _dict['last_msg_at'] = None

        # set to None if msg_count (nullable) is None
        # and model_fields_set contains the field
        if self.msg_count is None and "msg_count" in self.model_fields_set:
            _dict['msg_count'] = None

        # set to None if credits (nullable) is None
        # and model_fields_set contains the field
        if self.credits is None and "credits" in self.model_fields_set:
            _dict['credits'] = None

        # set to None if chatbot_name (nullable) is None
        # and model_fields_set contains the field
        if self.chatbot_name is None and "chatbot_name" in self.model_fields_set:
            _dict['chatbot_name'] = None

        # set to None if flow_name (nullable) is None
        # and model_fields_set contains the field
        if self.flow_name is None and "flow_name" in self.model_fields_set:
            _dict['flow_name'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if ipaddress (nullable) is None
        # and model_fields_set contains the field
        if self.ipaddress is None and "ipaddress" in self.model_fields_set:
            _dict['ipaddress'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowSessionViewResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "session_id": obj.get("session_id"),
            "chatbot_id": obj.get("chatbot_id"),
            "flow_id": obj.get("flow_id"),
            "workspace_id": obj.get("workspace_id"),
            "created_at": obj.get("created_at"),
            "last_msg_at": obj.get("last_msg_at"),
            "msg_count": obj.get("msg_count"),
            "credits": obj.get("credits"),
            "chatbot_name": obj.get("chatbot_name"),
            "flow_name": obj.get("flow_name"),
            "tags": obj.get("tags"),
            "duration": obj.get("duration"),
            "ipaddress": obj.get("ipaddress"),
            "url": obj.get("url")
        })
        return _obj

