"""Shared golden-grid placeholders for Dual-Track RED skeleton tests."""

from __future__ import annotations

from typing import Final

# G0 — complete magic square (0-index int[4][4])
# G0: Final[list[list[int]]] = [
#     [16, 3, 2, 13],
#     [5, 10, 11, 8],
#     [9, 6, 7, 12],
#     [4, 15, 14, 1],
# ]

# G1 — partial puzzle, blanks at (2,2) and (3,3) 1-index; missing {7, 10}
G1: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

# G2 — PLACEHOLDER: Attempt A fails, Attempt B (reverse) succeeds
# G2: Final[list[list[int]]] | None = None  # TBD before GREEN

# G3 — PLACEHOLDER: Attempt A and B both fail (unsolvable)
# G3: Final[list[list[int]]] | None = None  # TBD before GREEN
