#!/usr/bin/env python3
"""Generate or refresh the Golden Master baseline file."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.golden_master.approve import DEFAULT_EXPECTED_PATH, write_baseline
from tests.golden_master.serializer import render_golden_master_document


def main() -> int:
    """Write the current solver output to the Golden Master baseline file.

    Returns:
        Process exit code (0 on success).
    """
    content = render_golden_master_document()
    write_baseline(DEFAULT_EXPECTED_PATH, content)
    print(f"Wrote Golden Master baseline to {DEFAULT_EXPECTED_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
