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
from flowhunt.models.tracking_click_id_names import TrackingClickIdNames
from flowhunt.models.tracking_source_types import TrackingSourceTypes
from typing import Optional, Set
from typing_extensions import Self

class TrackingSourceSearchRequest(BaseModel):
    """
    TrackingSourceSearchRequest
    """ # noqa: E501
    customer_id: Optional[StrictStr] = None
    source_type: Optional[TrackingSourceTypes] = None
    click_id: Optional[StrictStr] = None
    click_id_name: Optional[TrackingClickIdNames] = None
    utm_source: Optional[StrictStr] = None
    utm_medium: Optional[StrictStr] = None
    utm_campaign: Optional[StrictStr] = None
    utm_channel: Optional[StrictStr] = None
    from_date: Optional[datetime] = None
    to_date: Optional[datetime] = None
    include_expired: Optional[StrictBool] = None
    page: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    page_size: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None
    __properties: ClassVar[List[str]] = ["customer_id", "source_type", "click_id", "click_id_name", "utm_source", "utm_medium", "utm_campaign", "utm_channel", "from_date", "to_date", "include_expired", "page", "page_size"]

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
        """Create an instance of TrackingSourceSearchRequest from a JSON string"""
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
        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if source_type (nullable) is None
        # and model_fields_set contains the field
        if self.source_type is None and "source_type" in self.model_fields_set:
            _dict['source_type'] = None

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

        # set to None if utm_channel (nullable) is None
        # and model_fields_set contains the field
        if self.utm_channel is None and "utm_channel" in self.model_fields_set:
            _dict['utm_channel'] = None

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
        """Create an instance of TrackingSourceSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customer_id": obj.get("customer_id"),
            "source_type": obj.get("source_type"),
            "click_id": obj.get("click_id"),
            "click_id_name": obj.get("click_id_name"),
            "utm_source": obj.get("utm_source"),
            "utm_medium": obj.get("utm_medium"),
            "utm_campaign": obj.get("utm_campaign"),
            "utm_channel": obj.get("utm_channel"),
            "from_date": obj.get("from_date"),
            "to_date": obj.get("to_date"),
            "include_expired": obj.get("include_expired"),
            "page": obj.get("page"),
            "page_size": obj.get("page_size")
        })
        return _obj


