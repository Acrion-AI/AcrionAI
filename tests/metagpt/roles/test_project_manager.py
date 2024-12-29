#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/12 10:23
@Author  : alexanderwu
@File    : test_project_manager.py
"""
import pytest

from acrionai.logs import logger
from acrionai.roles import ProjectManager
from tests.acrionai.roles.mock import MockMessages


@pytest.mark.asyncio
async def test_project_manager(context):
    project_manager = ProjectManager(context=context)
    rsp = await project_manager.run(MockMessages.system_design)
    logger.info(rsp)