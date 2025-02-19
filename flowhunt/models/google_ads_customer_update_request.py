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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flowhunt.models.google_ads_action_type import GoogleAdsActionType
from typing import Optional, Set
from typing_extensions import Self

class GoogleAdsCustomerUpdateRequest(BaseModel):
    """
    GoogleAdsCustomerUpdateRequest
    """ # noqa: E501
    language_code: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    min_queries: Optional[StrictInt] = None
    cluster_strength: Optional[StrictInt] = None
    min_impressions: Optional[StrictInt] = None
    min_clicks: Optional[StrictInt] = None
    cron_settings: Optional[StrictStr] = None
    action_type: Optional[GoogleAdsActionType] = None
    ga_measurement_id: Optional[StrictStr] = None
    ga_api_secret: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["language_code", "country", "min_queries", "cluster_strength", "min_impressions", "min_clicks", "cron_settings", "action_type", "ga_measurement_id", "ga_api_secret"]

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
        """Create an instance of GoogleAdsCustomerUpdateRequest from a JSON string"""
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
        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if min_queries (nullable) is None
        # and model_fields_set contains the field
        if self.min_queries is None and "min_queries" in self.model_fields_set:
            _dict['min_queries'] = None

        # set to None if cluster_strength (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_strength is None and "cluster_strength" in self.model_fields_set:
            _dict['cluster_strength'] = None

        # set to None if min_impressions (nullable) is None
        # and model_fields_set contains the field
        if self.min_impressions is None and "min_impressions" in self.model_fields_set:
            _dict['min_impressions'] = None

        # set to None if min_clicks (nullable) is None
        # and model_fields_set contains the field
        if self.min_clicks is None and "min_clicks" in self.model_fields_set:
            _dict['min_clicks'] = None

        # set to None if cron_settings (nullable) is None
        # and model_fields_set contains the field
        if self.cron_settings is None and "cron_settings" in self.model_fields_set:
            _dict['cron_settings'] = None

        # set to None if action_type (nullable) is None
        # and model_fields_set contains the field
        if self.action_type is None and "action_type" in self.model_fields_set:
            _dict['action_type'] = None

        # set to None if ga_measurement_id (nullable) is None
        # and model_fields_set contains the field
        if self.ga_measurement_id is None and "ga_measurement_id" in self.model_fields_set:
            _dict['ga_measurement_id'] = None

        # set to None if ga_api_secret (nullable) is None
        # and model_fields_set contains the field
        if self.ga_api_secret is None and "ga_api_secret" in self.model_fields_set:
            _dict['ga_api_secret'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleAdsCustomerUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language_code": obj.get("language_code"),
            "country": obj.get("country"),
            "min_queries": obj.get("min_queries"),
            "cluster_strength": obj.get("cluster_strength"),
            "min_impressions": obj.get("min_impressions"),
            "min_clicks": obj.get("min_clicks"),
            "cron_settings": obj.get("cron_settings"),
            "action_type": obj.get("action_type"),
            "ga_measurement_id": obj.get("ga_measurement_id"),
            "ga_api_secret": obj.get("ga_api_secret")
        })
        return _obj


