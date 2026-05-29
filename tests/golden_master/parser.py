"""Parse Golden Master baseline documents into scenario sections."""

from __future__ import annotations

import re

SECTION_HEADER_PATTERN = re.compile(r"^\[(GM-TC-\d+)\]\s*$", re.MULTILINE)


def extract_section(content: str, section_id: str) -> str | None:
    """Extract one scenario section block from a Golden Master document.

    Args:
        content: Full baseline document text.
        section_id: Section tag such as ``GM-TC-01``.

    Returns:
        Section block including the header, or None when missing.
    """
    matches = list(SECTION_HEADER_PATTERN.finditer(content))
    for index, match in enumerate(matches):
        if match.group(1) != section_id:
            continue

        start = match.start()
        if index + 1 < len(matches):
            end = matches[index + 1].start()
            block = content[start:end].rstrip()
            return block + "\n"

        return content[start:].rstrip() + "\n"

    return None
