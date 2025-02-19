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


class TransactionType(str, Enum):
    """
    TransactionType
    """

    """
    allowed enum values
    """
    G = 'G'
    K = 'K'
    V = 'V'
    S = 'S'
    T = 'T'
    D = 'D'
    M = 'M'
    F = 'F'
    I = 'I'
    C = 'C'
    A = 'A'
    Y = 'Y'
    E = 'E'
    X = 'X'
    P = 'P'
    W = 'W'
    O = 'O'
    N = 'N'
    FT_I = 'FT_I'
    DDG = 'DDG'
    CGD = 'CGD'
    CGS = 'CGS'
    RGS = 'RGS'
    UGS = 'UGS'
    IGI = 'IGI'
    TR = 'TR'
    FAT_GC = 'FAT_GC'
    SEQUENTIAL_AGENT = 'SEQUENTIAL_AGENT'
    SELF_MANAGED_AGENT = 'SELF_MANAGED_AGENT'
    TOOL_ARXIV = 'TOOL_ARXIV'
    TOOL_REDDIT = 'TOOL_REDDIT'
    TOOL_WIKIPEDIA = 'TOOL_WIKIPEDIA'
    TOOL_DALL_E = 'TOOL_DALL_E'
    TOOL_YOUTUBE_SEARCH = 'TOOL_YOUTUBE_SEARCH'
    TOOL_IFTTT_WEBHOOK = 'TOOL_IFTTT_WEBHOOK'
    TOOL_PUBMED = 'TOOL_PUBMED'
    TOOL_STACK_EXCHANGE = 'TOOL_STACK_EXCHANGE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionType from a JSON string"""
        return cls(json.loads(json_str))


