"""PyQt main window for Magic Square puzzle."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from src.boundary.screen.constants import (
    CELL_MAX_VALUE,
    CELL_MIN_VALUE,
    CLEAR_BUTTON_LABEL,
    GRID_DIMENSION,
    LOAD_SAMPLE_BUTTON_LABEL,
    RESULT_PLACEHOLDER,
    SAMPLE_G1,
    SOLVE_BUTTON_LABEL,
    WINDOW_TITLE,
)
from src.boundary.screen.grid_adapter import read_grid_from_cell_values
from src.boundary.screen.puzzle_presenter import PresentationResult, PuzzlePresenter


class MainWindow(QMainWindow):
    """Main application window with 4x4 grid input and solve controls."""

    def __init__(self, presenter: PuzzlePresenter) -> None:
        """Initialize window with injected presenter.

        Args:
            presenter: Formats boundary solve outcomes for display.
        """
        super().__init__()
        self._presenter = presenter
        self._spin_boxes: list[list[QSpinBox]] = []
        self._result_label = QLabel(RESULT_PLACEHOLDER)
        self._build_ui()

    def _build_ui(self) -> None:
        """Construct widgets and layout."""
        self.setWindowTitle(WINDOW_TITLE)
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)

        grid_layout = QGridLayout()
        for row in range(GRID_DIMENSION):
            row_boxes: list[QSpinBox] = []
            for col in range(GRID_DIMENSION):
                spin = QSpinBox()
                spin.setRange(CELL_MIN_VALUE, CELL_MAX_VALUE)
                spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
                spin.setMinimumWidth(52)
                grid_layout.addWidget(spin, row, col)
                row_boxes.append(spin)
            self._spin_boxes.append(row_boxes)
        root.addLayout(grid_layout)

        button_row = QHBoxLayout()
        solve_btn = QPushButton(SOLVE_BUTTON_LABEL)
        solve_btn.clicked.connect(self._on_solve_clicked)
        sample_btn = QPushButton(LOAD_SAMPLE_BUTTON_LABEL)
        sample_btn.clicked.connect(self._on_load_sample_clicked)
        clear_btn = QPushButton(CLEAR_BUTTON_LABEL)
        clear_btn.clicked.connect(self._on_clear_clicked)
        button_row.addWidget(solve_btn)
        button_row.addWidget(sample_btn)
        button_row.addWidget(clear_btn)
        root.addLayout(button_row)

        self._result_label.setWordWrap(True)
        self._result_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        root.addWidget(self._result_label)

    def _read_grid_from_ui(self) -> list[list[int]]:
        """Collect current spin box values as a 4x4 grid."""
        cells = [
            [spin.value() for spin in row_boxes]
            for row_boxes in self._spin_boxes
        ]
        return read_grid_from_cell_values(cells)

    def _set_grid_in_ui(self, grid: list[list[int]]) -> None:
        """Populate spin boxes from a 4x4 grid."""
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                self._spin_boxes[row_index][col_index].setValue(value)

    def _show_result(self, result: PresentationResult) -> None:
        """Display presentation result in the result label."""
        self._result_label.setText(result.text)

    def _on_solve_clicked(self) -> None:
        """Handle Solve button click."""
        grid = self._read_grid_from_ui()
        result = self._presenter.present(grid)
        self._show_result(result)

    def _on_load_sample_clicked(self) -> None:
        """Load G1 sample puzzle into the grid."""
        self._set_grid_in_ui(SAMPLE_G1)
        self._result_label.setText(RESULT_PLACEHOLDER)

    def _on_clear_clicked(self) -> None:
        """Reset grid and result display."""
        empty = [[CELL_MIN_VALUE] * GRID_DIMENSION for _ in range(GRID_DIMENSION)]
        self._set_grid_in_ui(empty)
        self._result_label.setText(RESULT_PLACEHOLDER)
