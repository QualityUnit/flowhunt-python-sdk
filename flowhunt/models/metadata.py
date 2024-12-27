# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from flowhunt.models.flow_session_loading_metadata import FlowSessionLoadingMetadata
from flowhunt.models.flow_session_message_metadata import FlowSessionMessageMetadata
from flowhunt.models.flow_session_task_response_metadata import FlowSessionTaskResponseMetadata
from flowhunt.models.flow_session_tool_call_metadata import FlowSessionToolCallMetadata
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

METADATA_ANY_OF_SCHEMAS = ["FlowSessionLoadingMetadata", "FlowSessionMessageMetadata", "FlowSessionTaskResponseMetadata", "FlowSessionToolCallMetadata"]

class Metadata(BaseModel):
    """
    Metadata
    """

    # data type: FlowSessionMessageMetadata
    anyof_schema_1_validator: Optional[FlowSessionMessageMetadata] = None
    # data type: FlowSessionLoadingMetadata
    anyof_schema_2_validator: Optional[FlowSessionLoadingMetadata] = None
    # data type: FlowSessionToolCallMetadata
    anyof_schema_3_validator: Optional[FlowSessionToolCallMetadata] = None
    # data type: FlowSessionTaskResponseMetadata
    anyof_schema_4_validator: Optional[FlowSessionTaskResponseMetadata] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[FlowSessionLoadingMetadata, FlowSessionMessageMetadata, FlowSessionTaskResponseMetadata, FlowSessionToolCallMetadata]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "FlowSessionLoadingMetadata", "FlowSessionMessageMetadata", "FlowSessionTaskResponseMetadata", "FlowSessionToolCallMetadata" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = Metadata.model_construct()
        error_messages = []
        # validate data type: FlowSessionMessageMetadata
        if not isinstance(v, FlowSessionMessageMetadata):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FlowSessionMessageMetadata`")
        else:
            return v

        # validate data type: FlowSessionLoadingMetadata
        if not isinstance(v, FlowSessionLoadingMetadata):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FlowSessionLoadingMetadata`")
        else:
            return v

        # validate data type: FlowSessionToolCallMetadata
        if not isinstance(v, FlowSessionToolCallMetadata):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FlowSessionToolCallMetadata`")
        else:
            return v

        # validate data type: FlowSessionTaskResponseMetadata
        if not isinstance(v, FlowSessionTaskResponseMetadata):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FlowSessionTaskResponseMetadata`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in Metadata with anyOf schemas: FlowSessionLoadingMetadata, FlowSessionMessageMetadata, FlowSessionTaskResponseMetadata, FlowSessionToolCallMetadata. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[FlowSessionMessageMetadata] = None
        try:
            instance.actual_instance = FlowSessionMessageMetadata.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[FlowSessionLoadingMetadata] = None
        try:
            instance.actual_instance = FlowSessionLoadingMetadata.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[FlowSessionToolCallMetadata] = None
        try:
            instance.actual_instance = FlowSessionToolCallMetadata.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[FlowSessionTaskResponseMetadata] = None
        try:
            instance.actual_instance = FlowSessionTaskResponseMetadata.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Metadata with anyOf schemas: FlowSessionLoadingMetadata, FlowSessionMessageMetadata, FlowSessionTaskResponseMetadata, FlowSessionToolCallMetadata. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], FlowSessionLoadingMetadata, FlowSessionMessageMetadata, FlowSessionTaskResponseMetadata, FlowSessionToolCallMetadata]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


