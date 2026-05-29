"""Entry point: python -m src.boundary.screen"""

from __future__ import annotations

import sys

from src.boundary.screen.app import run_app

if __name__ == "__main__":
    sys.exit(run_app())
