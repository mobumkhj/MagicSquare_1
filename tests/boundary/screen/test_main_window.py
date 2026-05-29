"""Main window smoke tests with pytest-qt."""

from __future__ import annotations

from unittest.mock import MagicMock

from typing import Any

import pytest

pytest.importorskip("PyQt6")
pytest.importorskip("pytestqt")

from PyQt6.QtWidgets import QApplication

from src.boundary.screen.main_window import MainWindow
from src.boundary.screen.puzzle_presenter import PresentationResult, PuzzlePresenter

pytestmark = pytest.mark.usefixtures("qapp")


@pytest.fixture(scope="session")
def qapp() -> QApplication:
    """Shared QApplication for widget tests."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestMainWindow:
    """Smoke tests for MainWindow widget interactions."""

    def test_solve_button_triggers_presenter(self, qtbot: Any) -> None:
        """Solve action calls presenter and shows result text."""
        # Given: mock presenter returning success
        mock_presenter = MagicMock(spec=PuzzlePresenter)
        mock_presenter.present.return_value = PresentationResult(
            is_success=True,
            text="Solution: (2, 2) = 10, (3, 3) = 7 [2, 2, 10, 3, 3, 7]",
            solution=[2, 2, 10, 3, 3, 7],
        )
        window = MainWindow(presenter=mock_presenter)
        qtbot.addWidget(window)

        # When: load sample and solve
        window._on_load_sample_clicked()
        window._on_solve_clicked()

        # Then: presenter was called with G1 grid
        mock_presenter.present.assert_called_once()
        called_grid = mock_presenter.present.call_args[0][0]
        assert called_grid[1][1] == 0
        assert "Solution:" in window._result_label.text()

    def test_window_has_sixteen_spin_boxes(self, qtbot: Any) -> None:
        """Main window contains 4x4 spin box grid."""
        # Given: presenter mock
        mock_presenter = MagicMock(spec=PuzzlePresenter)
        window = MainWindow(presenter=mock_presenter)
        qtbot.addWidget(window)

        # Then: 16 spin boxes
        assert len(window._spin_boxes) == 4
        assert all(len(row) == 4 for row in window._spin_boxes)
