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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ImageConvertRequest(BaseModel):
    """
    ImageConvertRequest
    """ # noqa: E501
    post_back_url: Optional[StrictStr] = None
    image_url: StrictStr = Field(description="Image URL to convert")
    format: StrictStr = Field(description="Image format to convert to")
    quality: Optional[Annotated[int, Field(le=100, strict=True, ge=10)]] = None
    __properties: ClassVar[List[str]] = ["post_back_url", "image_url", "format", "quality"]

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
        """Create an instance of ImageConvertRequest from a JSON string"""
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
        # set to None if post_back_url (nullable) is None
        # and model_fields_set contains the field
        if self.post_back_url is None and "post_back_url" in self.model_fields_set:
            _dict['post_back_url'] = None

        # set to None if quality (nullable) is None
        # and model_fields_set contains the field
        if self.quality is None and "quality" in self.model_fields_set:
            _dict['quality'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImageConvertRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "post_back_url": obj.get("post_back_url"),
            "image_url": obj.get("image_url"),
            "format": obj.get("format"),
            "quality": obj.get("quality")
        })
        return _obj


