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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TrackingEventSearchRequest(BaseModel):
    """
    TrackingEventSearchRequest
    """ # noqa: E501
    event_name: Optional[StrictStr] = None
    conversion_action_id: Optional[StrictStr] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    include_expired: Optional[StrictBool] = None
    page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    page_size: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None
    __properties: ClassVar[List[str]] = ["event_name", "conversion_action_id", "from_date", "to_date", "include_expired", "page", "page_size"]

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
        """Create an instance of TrackingEventSearchRequest from a JSON string"""
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
        # set to None if event_name (nullable) is None
        # and model_fields_set contains the field
        if self.event_name is None and "event_name" in self.model_fields_set:
            _dict['event_name'] = None

        # set to None if conversion_action_id (nullable) is None
        # and model_fields_set contains the field
        if self.conversion_action_id is None and "conversion_action_id" in self.model_fields_set:
            _dict['conversion_action_id'] = None

        # set to None if from_date (nullable) is None
        # and model_fields_set contains the field
        if self.from_date is None and "from_date" in self.model_fields_set:
            _dict['from_date'] = None

        # set to None if to_date (nullable) is None
        # and model_fields_set contains the field
        if self.to_date is None and "to_date" in self.model_fields_set:
            _dict['to_date'] = None

        # set to None if include_expired (nullable) is None
        # and model_fields_set contains the field
        if self.include_expired is None and "include_expired" in self.model_fields_set:
            _dict['include_expired'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['page_size'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingEventSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_name": obj.get("event_name"),
            "conversion_action_id": obj.get("conversion_action_id"),
            "from_date": obj.get("from_date"),
            "to_date": obj.get("to_date"),
            "include_expired": obj.get("include_expired"),
            "page": obj.get("page"),
            "page_size": obj.get("page_size")
        })
        return _obj


