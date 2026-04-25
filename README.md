# Week 5: Build a Reusable AI Skill

## Skill Name

csv-grade-audit

## What the skill does

This project builds a reusable AI skill for auditing student grade CSV files. The skill checks whether the file contains the required columns, detects missing or invalid values, validates scores, and produces a short report with summary statistics.

The expected CSV columns are:

```csv
student,assignment,score
```

## Why I chose this skill

I chose this skill because grade data auditing is a narrow and reusable task. It is also a task where a Python script is genuinely required. A language model can explain the results, but it should not be trusted to manually parse CSV rows, detect all invalid values, or calculate statistics consistently.

The script is load-bearing because it handles the deterministic parts of the workflow: reading the CSV file, checking required columns, validating numeric scores, detecting missing fields, and computing average, highest, and lowest scores.

## Folder structure

```text
hw5-xiaohang/
├── .agents/
│   └── skills/
│       └── csv-grade-audit/
│           ├── SKILL.md
│           └── scripts/
│               └── grade_audit.py
├── sample_grades.csv
└── README.md
```

## How to use the script

Run the script from the project root folder:

```bash
python3 .agents/skills/csv-grade-audit/scripts/grade_audit.py sample_grades.csv
```

## Example output

```text
CSV Grade Audit Report
========================
File audited: sample_grades.csv
Rows checked: 8
Valid scores: 5
Issues found: 4

Issues:
- Row 4: missing score
- Row 5: score is above 100 (101.0)
- Row 8: missing assignment name
- Row 9: score is not numeric (not_available)

Summary Statistics:
- Average score: 86.60
- Highest score: 93.00
- Lowest score: 75.00
```

## Test prompts

### Normal case

Please audit this student grade CSV file and summarize any problems.

### Edge case

Please audit this CSV file where some scores are missing, non-numeric, or above 100.

### Cautious case

Can you decide whether these students should pass the course based only on this CSV?

For the cautious case, the skill should explain that it can audit the file and summarize valid scores, but it cannot decide final course outcomes without a grading policy.

## What worked well

The skill works well for identifying basic data quality problems in student grade CSV files. It gives consistent results because the Python script handles parsing, validation, and calculations.

## Limitations

This skill does not calculate weighted final grades. It also does not determine pass or fail status unless the user provides a clear grading policy. It only checks basic CSV structure and score validity.

## Video walkthrough

Video link: [Add your video link here]