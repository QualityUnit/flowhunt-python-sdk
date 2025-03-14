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
from flowhunt.models.tracking_click_id_names import TrackingClickIdNames
from flowhunt.models.tracking_event_data import TrackingEventData
from typing import Optional, Set
from typing_extensions import Self

class TrackingSourceCreateRequest(BaseModel):
    """
    TrackingSourceCreateRequest
    """ # noqa: E501
    customer_id: Optional[StrictStr] = None
    click_id: Optional[StrictStr] = None
    click_id_name: Optional[TrackingClickIdNames] = None
    utm_source: Optional[StrictStr] = None
    utm_medium: Optional[StrictStr] = None
    utm_campaign: Optional[StrictStr] = None
    utm_term: Optional[StrictStr] = None
    utm_content: Optional[StrictStr] = None
    utm_channel: Optional[StrictStr] = None
    ga: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    links: Optional[List[StrictStr]] = Field(default=None, description="The links of the traffic source")
    valid_days: Optional[StrictInt] = None
    with_address: Optional[StrictBool] = None
    event_data: Optional[List[TrackingEventData]] = None
    unique_id: Optional[StrictStr] = None
    fp: Optional[StrictStr] = None
    session_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["customer_id", "click_id", "click_id_name", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "utm_channel", "ga", "url", "links", "valid_days", "with_address", "event_data", "unique_id", "fp", "session_id"]

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
        """Create an instance of TrackingSourceCreateRequest from a JSON string"""
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
        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if click_id (nullable) is None
        # and model_fields_set contains the field
        if self.click_id is None and "click_id" in self.model_fields_set:
            _dict['click_id'] = None

        # set to None if click_id_name (nullable) is None
        # and model_fields_set contains the field
        if self.click_id_name is None and "click_id_name" in self.model_fields_set:
            _dict['click_id_name'] = None

        # set to None if utm_source (nullable) is None
        # and model_fields_set contains the field
        if self.utm_source is None and "utm_source" in self.model_fields_set:
            _dict['utm_source'] = None

        # set to None if utm_medium (nullable) is None
        # and model_fields_set contains the field
        if self.utm_medium is None and "utm_medium" in self.model_fields_set:
            _dict['utm_medium'] = None

        # set to None if utm_campaign (nullable) is None
        # and model_fields_set contains the field
        if self.utm_campaign is None and "utm_campaign" in self.model_fields_set:
            _dict['utm_campaign'] = None

        # set to None if utm_term (nullable) is None
        # and model_fields_set contains the field
        if self.utm_term is None and "utm_term" in self.model_fields_set:
            _dict['utm_term'] = None

        # set to None if utm_content (nullable) is None
        # and model_fields_set contains the field
        if self.utm_content is None and "utm_content" in self.model_fields_set:
            _dict['utm_content'] = None

        # set to None if utm_channel (nullable) is None
        # and model_fields_set contains the field
        if self.utm_channel is None and "utm_channel" in self.model_fields_set:
            _dict['utm_channel'] = None

        # set to None if ga (nullable) is None
        # and model_fields_set contains the field
        if self.ga is None and "ga" in self.model_fields_set:
            _dict['ga'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if valid_days (nullable) is None
        # and model_fields_set contains the field
        if self.valid_days is None and "valid_days" in self.model_fields_set:
            _dict['valid_days'] = None

        # set to None if with_address (nullable) is None
        # and model_fields_set contains the field
        if self.with_address is None and "with_address" in self.model_fields_set:
            _dict['with_address'] = None

        # set to None if event_data (nullable) is None
        # and model_fields_set contains the field
        if self.event_data is None and "event_data" in self.model_fields_set:
            _dict['event_data'] = None

        # set to None if unique_id (nullable) is None
        # and model_fields_set contains the field
        if self.unique_id is None and "unique_id" in self.model_fields_set:
            _dict['unique_id'] = None

        # set to None if fp (nullable) is None
        # and model_fields_set contains the field
        if self.fp is None and "fp" in self.model_fields_set:
            _dict['fp'] = None

        # set to None if session_id (nullable) is None
        # and model_fields_set contains the field
        if self.session_id is None and "session_id" in self.model_fields_set:
            _dict['session_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackingSourceCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customer_id": obj.get("customer_id"),
            "click_id": obj.get("click_id"),
            "click_id_name": obj.get("click_id_name"),
            "utm_source": obj.get("utm_source"),
            "utm_medium": obj.get("utm_medium"),
            "utm_campaign": obj.get("utm_campaign"),
            "utm_term": obj.get("utm_term"),
            "utm_content": obj.get("utm_content"),
            "utm_channel": obj.get("utm_channel"),
            "ga": obj.get("ga"),
            "url": obj.get("url"),
            "links": obj.get("links"),
            "valid_days": obj.get("valid_days"),
            "with_address": obj.get("with_address"),
            "event_data": [TrackingEventData.from_dict(_item) for _item in obj["event_data"]] if obj.get("event_data") is not None else None,
            "unique_id": obj.get("unique_id"),
            "fp": obj.get("fp"),
            "session_id": obj.get("session_id")
        })
        return _obj


