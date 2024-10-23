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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flowhunt.models.flow_loading_indicator import FlowLoadingIndicator
from flowhunt.models.flow_message_response import FlowMessageResponse
from flowhunt.models.flow_session_status import FlowSessionStatus
from typing import Optional, Set
from typing_extensions import Self

class FlowSessionInvocationMessageResponse(BaseModel):
    """
    FlowSessionInvocationMessageResponse
    """ # noqa: E501
    message_id: StrictStr = Field(description="Message ID")
    response_status: FlowSessionStatus = Field(description="Response status")
    loading_indicator: Optional[FlowLoadingIndicator] = None
    intermediate_responses: Optional[List[FlowMessageResponse]] = Field(default=None, description="Intermediate responses")
    final_response: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["message_id", "response_status", "loading_indicator", "intermediate_responses", "final_response"]

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
        """Create an instance of FlowSessionInvocationMessageResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loading_indicator
        if self.loading_indicator:
            _dict['loading_indicator'] = self.loading_indicator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in intermediate_responses (list)
        _items = []
        if self.intermediate_responses:
            for _item_intermediate_responses in self.intermediate_responses:
                if _item_intermediate_responses:
                    _items.append(_item_intermediate_responses.to_dict())
            _dict['intermediate_responses'] = _items
        # set to None if loading_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.loading_indicator is None and "loading_indicator" in self.model_fields_set:
            _dict['loading_indicator'] = None

        # set to None if final_response (nullable) is None
        # and model_fields_set contains the field
        if self.final_response is None and "final_response" in self.model_fields_set:
            _dict['final_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlowSessionInvocationMessageResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message_id": obj.get("message_id"),
            "response_status": obj.get("response_status"),
            "loading_indicator": FlowLoadingIndicator.from_dict(obj["loading_indicator"]) if obj.get("loading_indicator") is not None else None,
            "intermediate_responses": [FlowMessageResponse.from_dict(_item) for _item in obj["intermediate_responses"]] if obj.get("intermediate_responses") is not None else None,
            "final_response": obj.get("final_response")
        })
        return _obj

