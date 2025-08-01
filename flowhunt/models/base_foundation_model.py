# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BaseFoundationModel(str, Enum):
    """
    BaseFoundationModel
    """

    """
    allowed enum values
    """
    FLUX_MINUS_DEV = 'flux-dev'
    FLUX_MINUS_SCHNELL = 'flux-schnell'
    STABLE_MINUS_DIFFUSION_MINUS_3_DOT_5_MINUS_MEDIUM = 'stable-diffusion-3.5-medium'
    STABLE_MINUS_DIFFUSION_MINUS_3_DOT_5_MINUS_LARGE_MINUS_TURBO = 'stable-diffusion-3.5-large-turbo'
    STABLE_MINUS_DIFFUSION_MINUS_3_DOT_5_MINUS_LARGE = 'stable-diffusion-3.5-large'
    IMAGEN_MINUS_3 = 'imagen-3'
    IMAGEN_MINUS_3_MINUS_FAST = 'imagen-3-fast'
    IDEOGRAM_MINUS_V2 = 'ideogram-v2'
    IDEOGRAM_MINUS_V2_MINUS_TURBO = 'ideogram-v2-turbo'
    IDEOGRAM_MINUS_V2A = 'ideogram-v2a'
    IDEOGRAM_MINUS_V2A_MINUS_TURBO = 'ideogram-v2a-turbo'
    IDEOGRAM_MINUS_V3_MINUS_QUALITY = 'ideogram-v3-quality'
    IDEOGRAM_MINUS_V3_MINUS_TURBO = 'ideogram-v3-turbo'
    IDEOGRAM_MINUS_V3_MINUS_BALANCED = 'ideogram-v3-balanced'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BaseFoundationModel from a JSON string"""
        return cls(json.loads(json_str))


