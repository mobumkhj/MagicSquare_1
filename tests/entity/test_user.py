import uuid

import pytest


def test_user_create_generates_id_when_missing() -> None:
    # Arrange
    from src.entity.user import User

    # Act
    user = User.create(display_name="Alice")

    # Assert
    assert isinstance(user.user_id, uuid.UUID)
    assert user.display_name == "Alice"


def test_user_create_rejects_blank_display_name() -> None:
    # Arrange
    from src.entity.user import User

    # Act / Assert
    with pytest.raises(ValueError, match="display_name"):
        User.create(display_name="   ")


def test_user_create_rejects_too_long_display_name() -> None:
    # Arrange
    from src.entity.user import User

    # Act / Assert
    with pytest.raises(ValueError, match="display_name"):
        User.create(display_name="a" * (User.MAX_DISPLAY_NAME_LEN + 1))


def test_user_rename_returns_new_instance_and_keeps_id() -> None:
    # Arrange
    from src.entity.user import User

    original = User.create(display_name="Alice")

    # Act
    renamed = original.rename("Bob")

    # Assert
    assert renamed.user_id == original.user_id
    assert renamed.display_name == "Bob"
    assert renamed is not original

