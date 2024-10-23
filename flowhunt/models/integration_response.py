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
from flowhunt.models.integration_category import IntegrationCategory
from typing import Optional, Set
from typing_extensions import Self

class IntegrationResponse(BaseModel):
    """
    IntegrationResponse
    """ # noqa: E501
    slug: StrictStr = Field(description="The slug of the integration.")
    name: StrictStr = Field(description="The name of the integration.")
    description: StrictStr = Field(description="The description of the integration.")
    integrated_instance_cnt: StrictInt = Field(description="The number of integrated instances.")
    categories: List[IntegrationCategory] = Field(description="The categories of the integration.")
    alpha: Optional[StrictBool] = Field(default=False, description="Whether the integration is in alpha or not.")
    beta: Optional[StrictBool] = Field(default=False, description="Whether the integration is in beta or not.")
    public_flow_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["slug", "name", "description", "integrated_instance_cnt", "categories", "alpha", "beta", "public_flow_id"]

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
        """Create an instance of IntegrationResponse from a JSON string"""
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
        # set to None if public_flow_id (nullable) is None
        # and model_fields_set contains the field
        if self.public_flow_id is None and "public_flow_id" in self.model_fields_set:
            _dict['public_flow_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntegrationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "integrated_instance_cnt": obj.get("integrated_instance_cnt"),
            "categories": obj.get("categories"),
            "alpha": obj.get("alpha") if obj.get("alpha") is not None else False,
            "beta": obj.get("beta") if obj.get("beta") is not None else False,
            "public_flow_id": obj.get("public_flow_id")
        })
        return _obj

