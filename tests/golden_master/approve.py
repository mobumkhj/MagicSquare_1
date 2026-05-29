"""Approve-pattern helper for Golden Master regression tests."""

from __future__ import annotations

import difflib
import os
from pathlib import Path

from tests.golden_master.parser import extract_section
from tests.golden_master.scenarios import GoldenScenario
from tests.golden_master.serializer import (
    format_scenario_block,
    render_golden_master_document,
)

DEFAULT_EXPECTED_PATH = Path("tests/golden_master_expected.txt")
APPROVE_ENV_VAR = "GOLDEN_MASTER_APPROVE"


def _should_approve() -> bool:
    """Return whether baseline regeneration is explicitly requested."""
    return os.environ.get(APPROVE_ENV_VAR, "").strip() in {"1", "true", "yes"}


def write_baseline(path: Path, content: str) -> None:
    """Write Golden Master baseline content to disk.

    Args:
        path: Destination file path.
        content: Expected document text.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_unified_diff(expected: str, actual: str) -> str:
    """Build a unified diff between expected and actual baseline text.

    Args:
        expected: Approved baseline content.
        actual: Current solver output content.

    Returns:
        Unified diff text for pytest failure output.
    """
    diff_lines = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile="expected",
        tofile="actual",
    )
    return "".join(diff_lines)


def assert_matches_golden_master(
    path: Path = DEFAULT_EXPECTED_PATH,
) -> None:
    """Compare full solver document against the Golden Master baseline.

    When the baseline file is missing, or ``GOLDEN_MASTER_APPROVE=1`` is set,
    the current output is written as the new baseline.

    Args:
        path: Baseline file path.

    Raises:
        AssertionError: When actual output differs from the approved baseline.
    """
    actual = render_golden_master_document()

    if not path.exists() or _should_approve():
        write_baseline(path, actual)
        return

    expected = path.read_text(encoding="utf-8")
    if actual == expected:
        return

    diff = build_unified_diff(expected, actual)
    raise AssertionError(
        "Golden Master mismatch. "
        f"Set {APPROVE_ENV_VAR}=1 to regenerate baseline.\n\n{diff}"
    )


def normalize_block(text: str) -> str:
    """Normalize one scenario block for stable text comparison.

    Args:
        text: Scenario block text.

    Returns:
        Block text with trailing whitespace removed and one trailing newline.
    """
    return text.rstrip() + "\n"


def assert_scenario_matches_golden_master(
    scenario: GoldenScenario,
    path: Path = DEFAULT_EXPECTED_PATH,
) -> None:
    """Compare one scenario block against the Golden Master baseline.

    When the baseline file is missing, the full document is written.
    When a section is missing, the full document is refreshed.

    Args:
        scenario: Scenario under test.
        path: Baseline file path.

    Raises:
        AssertionError: When actual scenario output differs from baseline.
    """
    actual_block = normalize_block(format_scenario_block(scenario))
    full_document = render_golden_master_document()

    if not path.exists() or _should_approve():
        write_baseline(path, full_document)
        return

    expected_document = path.read_text(encoding="utf-8")
    expected_block_raw = extract_section(expected_document, scenario.test_id)

    if expected_block_raw is None:
        write_baseline(path, full_document)
        return

    expected_block = normalize_block(expected_block_raw)

    if actual_block == expected_block:
        return

    diff = build_unified_diff(expected_block, actual_block)
    raise AssertionError(
        f"{scenario.test_id} Golden Master mismatch. "
        f"Set {APPROVE_ENV_VAR}=1 to regenerate baseline.\n\n{diff}"
    )
