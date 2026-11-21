# Clinic Appointment CSV Cleaner

This Python program cleans up messy clinic appointment CSV files, removes duplicate entries, and standardizes formatting.

With my 20+ years' background in precision-heavy healthcare documentation and familiarity with the problems messy CSV files introduce, I have built this utility to handle common data-entry issues — like inconsistent capitalization, extra spaces, missing departments, and duplicate rows — without manual spreadsheet cleanup.

## What it does

* **Fixes text formatting:** Removes extra spaces and converts patient names and departments to consistent Title Case.
* **Removes duplicates:** Catches exact duplicate appointment rows and logs how many were removed.
* **Fills missing values:** Replaces blank departments with `Unassigned` and empty copay fields with `0.00`.
* **Standardizes currency:** Removes `$` signs and formats all copay amounts to two decimal places.

## How to run it

Ensure `sample_appointments.csv` is in the same folder as the script, then run:

```bash
python clean_appointments.py
```

The script reads `sample_appointments.csv` and creates a new file called `cleaned_appointments.csv`.

## Example

**Input (`sample_appointments.csv`):**
```text
patient_id,patient_name,visit_date,department,copay_amount
101,  jane doe ,2026-05-10,cardiology,$45.00
101,  jane doe ,2026-05-10,cardiology,$45.00
103,Emily   Clark,2026-05-11,,$25.50
```

**Output (`cleaned_appointments.csv`):**
```text
patient_id,patient_name,visit_date,department,copay_amount
101,Jane Doe,2026-05-10,Cardiology,45.00
103,Emily Clark,2026-05-11,Unassigned,25.50
```

I have developed this using Python 3.13 on Windows 11 (uses only built-in `csv` and `pathlib` modules).
