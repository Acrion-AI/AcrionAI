#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/8/18
@Author  : mashenquan
@File    : test_text_to_image.py
@Desc    : Unit tests.
"""
import base64

import openai
import pytest
from pydantic import BaseModel

from acrionai.config2 import Config
from acrionai.learn.text_to_image import text_to_image
from acrionai.tools.acrionai_text_to_image import AcrionAIText2Image
from acrionai.tools.openai_text_to_image import OpenAIText2Image
from acrionai.utils.s3 import S3


@pytest.mark.asyncio
async def test_text_to_image(mocker):
    # mock
    mocker.patch.object(AcrionAIText2Image, "text_2_image", return_value=b"mock AcrionAIText2Image")
    mocker.patch.object(OpenAIText2Image, "text_2_image", return_value=b"mock OpenAIText2Image")
    mocker.patch.object(S3, "cache", return_value="http://mock/s3")

    config = Config.default()
    assert config.acrionai_tti_url

    data = await text_to_image("Panda emoji", size_type="512x512", config=config)
    assert "base64" in data or "http" in data


@pytest.mark.asyncio
async def test_openai_text_to_image(mocker):
    # mocker
    mock_url = mocker.Mock()
    mock_url.url.return_value = "http://mock.com/0.png"

    class _MockData(BaseModel):
        data: list

    mock_data = _MockData(data=[mock_url])
    mocker.patch.object(openai.resources.images.AsyncImages, "generate", return_value=mock_data)
    mock_post = mocker.patch("aiohttp.ClientSession.get")
    mock_response = mocker.AsyncMock()
    mock_response.status = 200
    mock_response.read.return_value = base64.b64encode(b"success")
    mock_post.return_value.__aenter__.return_value = mock_response
    mocker.patch.object(S3, "cache", return_value="http://mock.s3.com/0.png")

    config = Config.default()
    config.acrionai_tti_url = None
    assert config.get_openai_llm()

    data = await text_to_image("Panda emoji", size_type="512x512", config=config)
    assert "base64" in data or "http" in data


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
