"""Define app commons."""


class BooleanValue:
    """Parse a boolean value."""

    true_values = ("yes", "y", "true", "1")
    false_values = ("no", "n", "false", "0", "")

    @classmethod
    def parse(cls, value, default=False):
        """Return boolean value."""
        try:
            normalized_value = value.strip().lower()
        except Exception:
            normalized_value = str(default).lower()
        if normalized_value in cls.true_values:
            return True
        elif normalized_value in cls.false_values:
            return False
        else:
            raise ValueError("Cannot interpret " "boolean value {0!r}".format(value))


class IntegerValue:
    """Parse an integer value."""

    @classmethod
    def parse(cls, value):
        """Return integer value."""
        return int(value)
