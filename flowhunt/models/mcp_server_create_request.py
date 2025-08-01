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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flowhunt.models.mcp_sub_server_binding import MCPSubServerBinding
from typing import Optional, Set
from typing_extensions import Self

class MCPServerCreateRequest(BaseModel):
    """
    Request schema for creating a new MCP server
    """ # noqa: E501
    name: StrictStr = Field(description="Name of the MCP server")
    is_active: Optional[StrictBool] = Field(default=True, description="Whether the MCP server is active")
    server_configuration: List[MCPSubServerBinding] = Field(description="List of subserver bindings for the MCP server configuration")
    __properties: ClassVar[List[str]] = ["name", "is_active", "server_configuration"]

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
        """Create an instance of MCPServerCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in server_configuration (list)
        _items = []
        if self.server_configuration:
            for _item_server_configuration in self.server_configuration:
                if _item_server_configuration:
                    _items.append(_item_server_configuration.to_dict())
            _dict['server_configuration'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MCPServerCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "is_active": obj.get("is_active") if obj.get("is_active") is not None else True,
            "server_configuration": [MCPSubServerBinding.from_dict(_item) for _item in obj["server_configuration"]] if obj.get("server_configuration") is not None else None
        })
        return _obj


