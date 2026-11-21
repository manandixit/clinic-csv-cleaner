import csv
from pathlib import Path

MEDICAL_ACRONYMS = {"ENT", "ICU", "ER", "NICU", "OBGYN"}


def clean_text(text: str) -> str:
    """Remove extra spaces and convert text to Title Case while preserving medical acronyms."""
    if not text:
        return ""
    words = text.strip().split()
    formatted_words = [
        word.upper() if word.upper() in MEDICAL_ACRONYMS else word.title()
        for word in words
    ]
    return " ".join(formatted_words)


def clean_currency(amount: str) -> str:
    """Standardize currency values to a clean two-decimal format."""
    if not amount or not amount.strip():
        return "0.00"
    numeric_str = amount.replace("$", "").replace(",", "").strip()
    try:
        return f"{float(numeric_str):.2f}"
    except ValueError:
        return "0.00"


def process_csv(input_path: Path, output_path: Path) -> None:
    """Read raw clinic CSV data, clean records, remove duplicates, and save."""
    seen_records = set()
    cleaned_rows = []
    duplicates_removed = 0

    with input_path.open(mode="r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        if not fieldnames:
            print("Error: The input CSV file is empty.")
            return

        for row in reader:
            patient_id = row.get("patient_id", "").strip()
            patient_name = clean_text(row.get("patient_name", ""))
            visit_date = row.get("visit_date", "").strip()
            department = clean_text(row.get("department", "")) or "Unassigned"
            copay = clean_currency(row.get("copay_amount", ""))

            # Create a unique tuple to track duplicate entries
            record_signature = (patient_id, patient_name, visit_date, department)

            if record_signature in seen_records:
                duplicates_removed += 1
                continue

            seen_records.add(record_signature)
            cleaned_rows.append(
                {
                    "patient_id": patient_id,
                    "patient_name": patient_name,
                    "visit_date": visit_date,
                    "department": department,
                    "copay_amount": copay,
                }
            )

    with output_path.open(mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print(f"Cleanup complete! Saved {len(cleaned_rows)} records to '{output_path}'.")
    print(f"Removed {duplicates_removed} duplicate record(s).")


if __name__ == "__main__":
    input_file = Path("sample_appointments.csv")
    output_file = Path("cleaned_appointments.csv")

    if input_file.exists():
        process_csv(input_file, output_file)
    else:
        print(f"Input file '{input_file}' not found.")
