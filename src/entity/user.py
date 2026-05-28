from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Self
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class User:
    """Domain user entity.

    This entity represents a user in the domain model.
    It is intentionally free of I/O concerns and external framework dependencies
    to comply with the ECB architecture (entity layer purity).

    Attributes:
        user_id: Stable identifier for the user.
        display_name: Human-readable name for presentation and audit purposes.
    """

    MAX_DISPLAY_NAME_LEN: ClassVar[int] = 50

    user_id: UUID
    display_name: str

    def __post_init__(self) -> None:
        normalized = self.display_name.strip()
        if not normalized:
            raise ValueError("display_name must not be blank")
        if len(normalized) > self.MAX_DISPLAY_NAME_LEN:
            raise ValueError(
                f"display_name must be <= {self.MAX_DISPLAY_NAME_LEN} characters"
            )
        object.__setattr__(self, "display_name", normalized)

    @classmethod
    def create(cls, display_name: str, user_id: UUID | None = None) -> Self:
        """Create a new user entity.

        Args:
            display_name: A non-blank user-facing name.
            user_id: Optional stable identifier. If omitted, a new UUID is generated.

        Returns:
            A validated `User` instance.

        Raises:
            ValueError: If `display_name` is blank or too long.
        """

        return cls(user_id=user_id or uuid4(), display_name=display_name)

    def rename(self, new_display_name: str) -> Self:
        """Return a new instance with an updated display name.

        Args:
            new_display_name: New non-blank display name.

        Returns:
            A new `User` instance with the same `user_id`.

        Raises:
            ValueError: If `new_display_name` is blank or too long.
        """

        return type(self)(user_id=self.user_id, display_name=new_display_name)

