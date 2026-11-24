"""Utilities for cleaning text names."""


def clean_name(raw):
    """Clean a name by collapsing whitespace and using title case."""
    return " ".join(raw.split()).title()

