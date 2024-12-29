#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 17:44
@Author  : alexanderwu
@File    : __init__.py
"""
from enum import Enum

from acrionai.actions.action import Action
from acrionai.actions.action_output import ActionOutput
from acrionai.actions.add_requirement import UserRequirement
from acrionai.actions.debug_error import DebugError
from acrionai.actions.design_api import WriteDesign
from acrionai.actions.design_api_review import DesignReview
from acrionai.actions.project_management import WriteTasks
from acrionai.actions.research import CollectLinks, WebBrowseAndSummarize, ConductResearch
from acrionai.actions.run_code import RunCode
from acrionai.actions.search_and_summarize import SearchAndSummarize
from acrionai.actions.write_code import WriteCode
from acrionai.actions.write_code_review import WriteCodeReview
from acrionai.actions.write_prd import WritePRD
from acrionai.actions.write_prd_review import WritePRDReview
from acrionai.actions.write_test import WriteTest
from acrionai.actions.di.execute_nb_code import ExecuteNbCode
from acrionai.actions.di.write_analysis_code import WriteAnalysisCode
from acrionai.actions.di.write_plan import WritePlan


class ActionType(Enum):
    """All types of Actions, used for indexing."""

    ADD_REQUIREMENT = UserRequirement
    WRITE_PRD = WritePRD
    WRITE_PRD_REVIEW = WritePRDReview
    WRITE_DESIGN = WriteDesign
    DESIGN_REVIEW = DesignReview
    WRTIE_CODE = WriteCode
    WRITE_CODE_REVIEW = WriteCodeReview
    WRITE_TEST = WriteTest
    RUN_CODE = RunCode
    DEBUG_ERROR = DebugError
    WRITE_TASKS = WriteTasks
    SEARCH_AND_SUMMARIZE = SearchAndSummarize
    COLLECT_LINKS = CollectLinks
    WEB_BROWSE_AND_SUMMARIZE = WebBrowseAndSummarize
    CONDUCT_RESEARCH = ConductResearch
    EXECUTE_NB_CODE = ExecuteNbCode
    WRITE_ANALYSIS_CODE = WriteAnalysisCode
    WRITE_PLAN = WritePlan


__all__ = [
    "ActionType",
    "Action",
    "ActionOutput",
]
