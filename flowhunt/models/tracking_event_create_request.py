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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from flowhunt.models.tracking_event_data import TrackingEventData
from typing import Optional, Set
from typing_extensions import Self

class TrackingEventCreateRequest(BaseModel):
    """
    TrackingEventCreateRequest
    """ # noqa: E501
    event_name: StrictStr = Field(description="The name of the event")
    unique_id: Optional[StrictStr] = None
    event_value: Optional[Union[StrictFloat, StrictInt]] = None
    currency: Optional[StrictStr] = None
    event_data: Optional[List[TrackingEventData]] = None
    link_ids: Optional[List[StrictStr]] = None
    valid_until: Optional[datetime] = None
    conversion_action_id: Optional[StrictStr] = None
    include_in_conversions_metric: Optional[StrictBool] = None
    with_address: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["event_name", "unique_id", "event_value", "currency", "event_data", "link_ids", "valid_until", "conversion_action_id", "include_in_conversions_metric", "with_address"]

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
        """Create an instance of TrackingEventCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in event_data (list)
        _items = []
        if self.event_data:
            for _item_event_data in self.event_data:
                if _item_event_data:
                    _items.append(_item_event_data.to_dict())
            _dict['event_data'] = _items
        # set to None if unique_id (nullable) is None
        # and model_fields_set contains the field
        if self.unique_id is None and "unique_id" in self.model_fields_set:
            _dict['unique_id'] = None

        # set to None if event_value (nullable) is None
        # and model_fields_set contains the field
        if self.event_value is None and "event_value" in self.model_fields_set:
            _dict['event_value'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if event_data (nullable) is None
        # and model_fields_set contains the field
        if self.event_data is None and "event_data" in self.model_fields_set:
            _dict['event_data'] = None

        # set to None if link_ids (nullable) is None
        # and model_fields_set contains the field
        if self.link_ids is None and "link_ids" in self.model_fields_set:
            _dict['link_ids'] = None

        # set to None if valid_until (nullable) is None
        # and model_fields_set contains the field
        if self.valid_until is None and "valid_until" in self.model_fields_set:
            _dict['valid_until'] = None

        # set to None if conversion_action_id (nullable) is None
        # and model_fields_set contains the field
        if self.conversion_action_id is None and "conversion_action_id" in self.model_fields_set:
            _dict['conversion_action_id'] = None

        # set to None if include_in_conversions_metric (nullable) is None
        # and model_fields_set contains the field
        if self.include_in_conversions_metric is None and "include_in_conversions_metric" in self.model_fields_set:
            _dict['include_in_conversions_metric'] = None

        # set to None if with_address (nullable) is None
        # and model_fields_set contains the field
        if self.with_address is None and "with_address" in self.model_fields_set:
            _dict['with_address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingEventCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_name": obj.get("event_name"),
            "unique_id": obj.get("unique_id"),
            "event_value": obj.get("event_value"),
            "currency": obj.get("currency"),
            "event_data": [TrackingEventData.from_dict(_item) for _item in obj["event_data"]] if obj.get("event_data") is not None else None,
            "link_ids": obj.get("link_ids"),
            "valid_until": obj.get("valid_until"),
            "conversion_action_id": obj.get("conversion_action_id"),
            "include_in_conversions_metric": obj.get("include_in_conversions_metric"),
            "with_address": obj.get("with_address")
        })
        return _obj


