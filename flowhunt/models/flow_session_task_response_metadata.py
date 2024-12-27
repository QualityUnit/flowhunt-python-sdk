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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FlowSessionTaskResponseMetadata(BaseModel):
    """
    FlowSessionTaskResponseMetadata
    """ # noqa: E501
    task_name: Optional[StrictStr]
    task_input: Optional[StrictStr]
    agent: Optional[StrictStr]
    task_response: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["task_name", "task_input", "agent", "task_response"]

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
        """Create an instance of FlowSessionTaskResponseMetadata from a JSON string"""
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
        # set to None if task_name (nullable) is None
        # and model_fields_set contains the field
        if self.task_name is None and "task_name" in self.model_fields_set:
            _dict['task_name'] = None

        # set to None if task_input (nullable) is None
        # and model_fields_set contains the field
        if self.task_input is None and "task_input" in self.model_fields_set:
            _dict['task_input'] = None

        # set to None if agent (nullable) is None
        # and model_fields_set contains the field
        if self.agent is None and "agent" in self.model_fields_set:
            _dict['agent'] = None

        # set to None if task_response (nullable) is None
        # and model_fields_set contains the field
        if self.task_response is None and "task_response" in self.model_fields_set:
            _dict['task_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowSessionTaskResponseMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_name": obj.get("task_name"),
            "task_input": obj.get("task_input"),
            "agent": obj.get("agent"),
            "task_response": obj.get("task_response")
        })
        return _obj


