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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from flowhunt.models.data import Data
from flowhunt.models.pointer_type import PointerType
from flowhunt.models.vector_document_type import VectorDocumentType
from typing import Optional, Set
from typing_extensions import Self

class VectorDocumentResponse(BaseModel):
    """
    VectorDocumentResponse
    """ # noqa: E501
    document_id: StrictStr = Field(description="Document ID")
    workspace_id: StrictStr = Field(description="Workspace ID")
    document_type: VectorDocumentType = Field(description="Document type")
    point_id: StrictStr = Field(description="Point ID")
    pointer_position: StrictInt = Field(description="Pointer position")
    pointer_type: PointerType = Field(description="Pointer type")
    schema_type: Optional[StrictStr] = None
    kb_key: StrictStr = Field(description="Knowledge key - schedule id or category id")
    vector: Optional[List[Union[StrictFloat, StrictInt]]]
    vector_id: StrictInt = Field(description="Vector ID")
    data: Optional[Data] = None
    __properties: ClassVar[List[str]] = ["document_id", "workspace_id", "document_type", "point_id", "pointer_position", "pointer_type", "schema_type", "kb_key", "vector", "vector_id", "data"]

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
        """Create an instance of VectorDocumentResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # set to None if schema_type (nullable) is None
        # and model_fields_set contains the field
        if self.schema_type is None and "schema_type" in self.model_fields_set:
            _dict['schema_type'] = None

        # set to None if vector (nullable) is None
        # and model_fields_set contains the field
        if self.vector is None and "vector" in self.model_fields_set:
            _dict['vector'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VectorDocumentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document_id": obj.get("document_id"),
            "workspace_id": obj.get("workspace_id"),
            "document_type": obj.get("document_type"),
            "point_id": obj.get("point_id"),
            "pointer_position": obj.get("pointer_position"),
            "pointer_type": obj.get("pointer_type"),
            "schema_type": obj.get("schema_type"),
            "kb_key": obj.get("kb_key"),
            "vector": obj.get("vector"),
            "vector_id": obj.get("vector_id"),
            "data": Data.from_dict(obj["data"]) if obj.get("data") is not None else None
        })
        return _obj

