"""gradebook.data — hardcoded sample grade records.

This module exists so the rest of the package has data to work on without
needing any file I/O. In a real project this might be a database query or
an API call; here it's just a Python list of dicts.
"""

RECORDS: list[dict] = [
    {"name": "Alice",   "subject": "Math",    "score": 88},
    {"name": "Alice",   "subject": "Science", "score": 92},
    {"name": "Alice",   "subject": "English", "score": 79},
    {"name": "Bob",     "subject": "Math",    "score": 72},
    {"name": "Bob",     "subject": "Science", "score": 85},
    {"name": "Bob",     "subject": "English", "score": 90},
    {"name": "Charlie", "subject": "Math",    "score": 95},
    {"name": "Charlie", "subject": "Science", "score": 88},
    {"name": "Charlie", "subject": "English", "score": 91},
    {"name": "Diana",   "subject": "Math",    "score": 60},
    {"name": "Diana",   "subject": "Science", "score": 70},
    {"name": "Diana",   "subject": "English", "score": 65},
]
from gradebook import data  # assuming your file is gradebook/data.py

def build_gradebook(records):
    report = {}

    for rec in records:
        name = rec["name"]
        subject = rec["subject"]
        score = rec["score"]

        # Initialize student entry if not present
        if name not in report:
            report[name] = {
                "subjects": {},
                "total": 0,
                "count": 0
            }

        # Add subject score
        report[name]["subjects"][subject] = score
        report[name]["total"] += score
        report[name]["count"] += 1

    # Compute average and grade
    for name, info in report.items():
        avg = info["total"] / info["count"]
        info["average"] = avg

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"

        info["grade"] = grade

    return report


# Example usage
report = build_gradebook(data.RECORDS)
for student, details in report.items():
    print(student, details)
