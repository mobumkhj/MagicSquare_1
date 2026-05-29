"""Boundary response schemas and error contract constants."""

from __future__ import annotations

RESPONSE_TYPE_ERROR = "ERROR"
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."

E001_CODE = "E001"
E001_MESSAGE = "Matrix must be 4x4."
E002_CODE = "E002"
E002_MESSAGE = "Exactly 2 empty cells (0) are required."
E004_CODE = "E004"
E004_MESSAGE = "Each cell must be 0 or an integer from 1 to 16."
E005_CODE = "E005"
E005_MESSAGE = "Non-zero values must not duplicate."

DOMAIN_NO_SOLUTION_CODE = "DOMAIN_NO_SOLUTION"
DOMAIN_NO_SOLUTION_MESSAGE = "No valid magic square completion exists."
