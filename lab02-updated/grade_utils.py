"""Reusable helpers for working with student records (GPA out of 5.00)."""


def letter_grade(gpa):
    """Return the letter grade corresponding to a GPA."""
    # TODO: your if/elif chain here
    if gpa>=4.50:
        return "A"
    elif gpa>=3.50:
        return "B"
    elif gpa>=2.50:
        return "C"
    elif gpa>=1.50:
        return "D"
    else:
        return "F"

