"""Shared golden-grid placeholders for Dual-Track RED skeleton tests."""

from __future__ import annotations

from typing import Final

G0: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

G1: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

G2: Final[list[list[int]]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 0],
]

G3: Final[list[list[int]]] = [
    [11, 15, 0, 2],
    [10, 3, 4, 12],
    [14, 0, 9, 5],
    [1, 7, 16, 13],
]
