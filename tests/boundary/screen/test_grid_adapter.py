"""Screen grid adapter — 4x4 cell values to puzzle matrix."""

from __future__ import annotations

import pytest

from src.boundary.screen.grid_adapter import read_grid_from_cell_values
from src.entity.constants import GRID_SIZE


class TestGridAdapter:
    """Convert UI cell values into boundary grid contract."""

    def test_read_grid_from_cell_values_returns_4x4_matrix(self) -> None:
        """Valid 4x4 cell values map to list[list[int]] grid."""
        # Given: 4x4 cell values including two blanks (0)
        cells = [
            [16, 3, 2, 13],
            [5, 0, 11, 8],
            [9, 6, 0, 12],
            [4, 15, 14, 1],
        ]

        # When: read_grid_from_cell_values(cells)
        grid = read_grid_from_cell_values(cells)

        # Then: grid matches input shape and values
        assert len(grid) == GRID_SIZE
        assert all(len(row) == GRID_SIZE for row in grid)
        assert grid == cells

    def test_read_grid_from_cell_values_rejects_wrong_row_count(self) -> None:
        """Non-4 row input raises ValueError."""
        # Given: 3 rows only
        cells = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

        # When / Then: ValueError
        with pytest.raises(ValueError, match="4x4"):
            read_grid_from_cell_values(cells)

    def test_read_grid_from_cell_values_rejects_wrong_column_count(self) -> None:
        """Jagged row raises ValueError."""
        # Given: one row with 3 columns
        cells = [
            [1, 2, 3, 4],
            [5, 6, 7],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]

        # When / Then: ValueError
        with pytest.raises(ValueError, match="4x4"):
            read_grid_from_cell_values(cells)
