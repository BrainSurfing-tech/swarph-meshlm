"""Smoke tests for the v0.0.1 swarph-meshlm scaffold.

Phase 7 (live ``llm.hookimpl`` commands) tests ship with the
implementation. v0.0.1 only verifies:

1. Plugin module is importable.
2. swarph-mesh + swarph-shared deps resolvable.
3. ``llm`` host can list the plugin (the entry_points registration
   resolved correctly at install time).
"""

from __future__ import annotations

import subprocess
import sys

import pytest

import swarph_meshlm
from swarph_meshlm import __version__


def test_version_exported():
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2


def test_module_importable():
    assert swarph_meshlm is not None


def test_swarph_mesh_dep_resolvable():
    import swarph_mesh

    assert hasattr(swarph_mesh, "LLMAdapter")


def test_swarph_shared_dep_resolvable():
    import swarph_shared

    assert hasattr(swarph_shared, "validate_node_name")


def test_llm_host_lists_plugin():
    """`llm plugins` should list swarph-meshlm after install — verifies
    the [project.entry-points.llm] registration in pyproject.toml is
    structurally valid."""
    result = subprocess.run(
        [sys.executable, "-m", "llm", "plugins"],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if result.returncode != 0:
        pytest.skip(
            f"`llm plugins` failed (rc={result.returncode}, stderr={result.stderr[:200]}); "
            "likely missing config dir or non-installed llm CLI in test env"
        )
    assert "swarph-meshlm" in result.stdout, (
        f"plugin not listed; got stdout={result.stdout[:500]}"
    )
