#!/usr/bin/env python3
# Flight Parser – Grade 7 Version
# Clean version, simple, no -j or -q support
# python src/flight_parser.py -h
# python src/flight_parser.py -i src/db.csv
# python src/flight_parser.py -d src/flights/

import argparse
import json
import os
from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M"


def is_comment_line(line):
    return line.strip().startswith("#")


def is_blank_line(line):
    return line.strip() == ""


def parse_datetime(value):
    try:
        return datetime.strptime(value, DATETIME_FORMAT)
    except ValueError:
        return None


def validate_row(fields):
    issues = []

    if len(fields) != 6:
        issues.append("missing required fields")
        return False, issues

    flight_id, origin, destination, dep_str, arr_str, price_str = [
        f.strip() for f in fields
    ]

    # flight_id
    if not (2 <= len(flight_id) <= 8 and flight_id.isalnum()):
        if len(flight_id) > 8:
            issues.append("flight_id too long (more than 8 characters)")
        else:
            issues.append("invalid flight_id (must be 2-8 alphanumeric characters)")

    # origin
    if origin == "":
        issues.append("missing origin field")
    elif not (len(origin) == 3 and origin.isupper() and origin.isalpha()):
        issues.append("invalid origin code")

    # destination
    if destination == "":
        issues.append("missing destination field")
    elif not (
        len(destination) == 3 and destination.isupper() and destination.isalpha()
    ):
        issues.append("invalid destination code")

    # datetimes
    dep_dt = parse_datetime(dep_str)
    arr_dt = parse_datetime(arr_str)

    if dep_dt is None:
        issues.append("invalid departure datetime")
    if arr_dt is None:
        issues.append("invalid arrival datetime")

    if dep_dt and arr_dt and arr_dt <= dep_dt:
        issues.append("arrival before departure")

    # price
    try:
        price_val = float(price_str)
        if price_val <= 0:
            issues.append("negative price value")
    except ValueError:
        issues.append("invalid price value")
        price_val = None

    if issues:
        return False, issues

    return True, {
        "flight_id": flight_id,
        "origin": origin,
        "destination": destination,
        "departure_datetime": dep_str,
        "arrival_datetime": arr_str,
        "price": price_val,
    }


def parse_and_validate_csv_files(csv_files):
    valid = []
    errors = []

    for csv_path in csv_files:
        with open(csv_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line_text = line.rstrip("\n")

                if is_blank_line(line_text):
                    continue

                if line_no == 1 and line_text.lower().startswith("flight_id,"):
                    continue

                if is_comment_line(line_text):
                    errors.append(
                        (
                            f"Line {line_no}",
                            line_text,
                            "comment line, ignored for data parsing",
                        )
                    )
                    continue

                fields = line_text.split(",")
                is_valid, result = validate_row(fields)

                if is_valid:
                    valid.append(result)
                else:
                    explanation = ", ".join(result)
                    errors.append((f"Line {line_no}", line_text, explanation))

    return valid, errors


def write_db_json(flights, output_path="db.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(flights, f, indent=4)


def write_errors_txt(error_entries, output_path="errors.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        for line_info, line_text, explanation in error_entries:
            f.write(f"{line_info}: {line_text} -> {explanation}\n")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Flight schedule parser (Grade 7 version)"
    )
    parser.add_argument("-i", metavar="file.csv", help="Parse a single CSV file")
    parser.add_argument(
        "-d", metavar="folder/", help="Parse all CSV files inside a folder"
    )
    parser.add_argument(
        "-o", metavar="out.json", help="Custom output filename for db.json"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    csv_files = []

    # single file
    if args.i:
        csv_files.append(args.i)

    # folder mode
    if args.d:
        for name in os.listdir(args.d):
            if name.lower().endswith(".csv"):
                csv_files.append(os.path.join(args.d, name))

    if not csv_files:
        print("No CSV files provided. Use -i file.csv or -d folder/")
        return

    valid_flights, errors = parse_and_validate_csv_files(csv_files)

    # output JSON
    out_path = args.o if args.o else "db.json"
    write_db_json(valid_flights, out_path)

    # errors output
    write_errors_txt(errors)

    print(f"Finished parsing.")
    print(f"Valid flights saved to: {out_path}")
    print(f"Errors saved to: errors.txt")


if __name__ == "__main__":
    main()
