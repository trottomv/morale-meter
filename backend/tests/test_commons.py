"""Define tests for app core commons."""

import pytest

from app.core.commons import BooleanValue, IntegerValue


def test_boolean_value():
    """Test boolean value."""
    value = BooleanValue.parse("True")
    assert value is True
    value = BooleanValue.parse("False")
    assert value is False
    value = BooleanValue.parse(None)
    assert value is False
    with pytest.raises(ValueError):
        value = BooleanValue.parse("test")


def test_integer_value():
    """Test integer value."""
    value = IntegerValue.parse("12")
    assert value == 12
