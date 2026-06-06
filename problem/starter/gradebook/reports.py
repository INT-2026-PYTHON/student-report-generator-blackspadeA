"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
"""gradebook.reports — build a printable report from grade records."""

# ✅ Use relative import to pull functions from sibling stats module
from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    lines = []

    # Total records
    lines.append(f"Total records: {len(records)}")

    # Subjects offered (sorted)
    subjects = sorted(subjects_offered(records))
    lines.append("Subjects offered: " + ", ".join(subjects))

    # Average score per student (alphabetical order)
    averages = average_per_student(records)
    lines.append("Average scores:")
    for name in sorted(averages.keys()):
        lines.append(f"  {name}: {averages[name]:.2f}")

    # Top scorer
    name, avg = top_scorer(records)
    lines.append(f"Top scorer: {name} ({avg:.2f})")

    # Passing students (>= 60.0)
    passing = passing_students(records, threshold=60.0)
    lines.append("Passing students: " + ", ".join(sorted(passing)))

    # Join into a single string
    return "\n".join(lines)
