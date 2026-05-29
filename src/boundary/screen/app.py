"""Application bootstrap for Magic Square PyQt GUI."""

from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from src.boundary.puzzle_boundary import PuzzleBoundary
from src.boundary.screen.main_window import MainWindow
from src.boundary.screen.puzzle_presenter import PuzzlePresenter
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase


def create_main_window() -> MainWindow:
    """Wire ECB layers and return the main window.

    Returns:
        Configured MainWindow ready to show.
    """
    use_case = SolveTwoBlanksUseCase()
    boundary = PuzzleBoundary(use_case=use_case)
    presenter = PuzzlePresenter(boundary=boundary)
    return MainWindow(presenter=presenter)


def run_app(argv: list[str] | None = None) -> int:
    """Start the Magic Square GUI application.

    Args:
        argv: Command-line arguments; defaults to sys.argv.

    Returns:
        Qt application exit code.
    """
    app = QApplication(argv if argv is not None else sys.argv)
    window = create_main_window()
    window.show()
    return app.exec()


def main() -> None:
    """Console entry point for setuptools scripts."""
    raise SystemExit(run_app())
