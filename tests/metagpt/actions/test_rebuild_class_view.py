#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/20
@Author  : mashenquan
@File    : test_rebuild_class_view.py
@Desc    : Unit tests for rebuild_class_view.py
"""
from pathlib import Path

import pytest

from acrionai.actions.rebuild_class_view import RebuildClassView
from acrionai.llm import LLM


@pytest.mark.asyncio
async def test_rebuild(context):
    action = RebuildClassView(
        name="RedBean",
        i_context=str(Path(__file__).parent.parent.parent.parent / "acrionai"),
        llm=LLM(),
        context=context,
    )
    await action.run()
    rows = await action.graph_db.select()
    assert rows
    assert context.repo.docs.graph_repo.changed_files


@pytest.mark.parametrize(
    ("path", "direction", "diff", "want"),
    [
        ("acrionai/software_company.py", "=", ".", "acrionai/software_company.py"),
        ("acrionai/software_company.py", "+", "AcrionAI", "AcrionAI/acrionai/software_company.py"),
        ("acrionai/software_company.py", "-", "acrionai", "software_company.py"),
    ],
)
def test_align_path(path, direction, diff, want):
    res = RebuildClassView._align_root(path=path, direction=direction, diff_path=diff)
    assert res == want


@pytest.mark.parametrize(
    ("path_root", "package_root", "want_direction", "want_diff"),
    [
        ("/Users/x/github/AcrionAI/acrionai", "/Users/x/github/AcrionAI/acrionai", "=", "."),
        ("/Users/x/github/AcrionAI", "/Users/x/github/AcrionAI/acrionai", "-", "acrionai"),
        ("/Users/x/github/AcrionAI/acrionai", "/Users/x/github/AcrionAI", "+", "acrionai"),
        (
            "/Users/x/github/AcrionAI-env/lib/python3.9/site-packages/moviepy",
            "/Users/x/github/AcrionAI-env/lib/python3.9/site-packages/",
            "+",
            "moviepy",
        ),
    ],
)
def test_diff_path(path_root, package_root, want_direction, want_diff):
    direction, diff = RebuildClassView._diff_path(path_root=Path(path_root), package_root=Path(package_root))
    assert direction == want_direction
    assert diff == want_diff


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
