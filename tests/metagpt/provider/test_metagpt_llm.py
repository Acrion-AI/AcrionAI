#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/8/30
@Author  : mashenquan
@File    : test_acrionai_llm.py
"""
from acrionai.provider.acrionai_api import AcrionAILLM
from tests.acrionai.provider.mock_llm_config import mock_llm_config


def test_acrionai():
    llm = AcrionAILLM(mock_llm_config)
    assert llm


if __name__ == "__main__":
    test_acrionai()
