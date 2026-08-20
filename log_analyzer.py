import argparse
import os


def analyze_log(file_path, level):
    infos = 0
    warnings = 0
    errors = 0
    filtered_lines = []

    if not os.path.exists(file_path):
        print(f"Error: file '{file_path}' not found.")
        return None

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()

            if "ERROR" in clean_line:
                errors += 1
            elif "WARNING" in clean_line:
                warnings += 1
            elif "INFO" in clean_line:
                infos += 1

            if level == "ALL" or level in clean_line:
                filtered_lines.append(clean_line)

    if errors > 0:
        status = "Needs attention"
    else:
        status = "Healthy"

    return {
        "file_path": file_path,
        "level": level,
        "infos": infos,
        "warnings": warnings,
        "errors": errors,
        "status": status,
        "filtered_lines": filtered_lines,
    }


def print_report(result):
    print("System Log Report")
    print("-----------------")
    print(f"File analyzed: {result['file_path']}")
    print(f"Filter level: {result['level']}")
    print(f"INFO: {result['infos']}")
    print(f"WARNING: {result['warnings']}")
    print(f"ERROR: {result['errors']}")
    print(f"Status: {result['status']}")

    print("\nFiltered events:")
    for line in result["filtered_lines"]:
        print(f"- {line}")


def generate_markdown_report(result, output_file):
    with open(output_file, "w") as report:
        report.write("# System Log Report\n\n")
        report.write(f"**File analyzed:** `{result['file_path']}`\n\n")
        report.write(f"**Filter level:** `{result['level']}`\n\n")

        report.write("## Summary\n\n")
        report.write(f"- INFO: {result['infos']}\n")
        report.write(f"- WARNING: {result['warnings']}\n")
        report.write(f"- ERROR: {result['errors']}\n\n")

        report.write("## Status\n\n")
        report.write(f"**{result['status']}**\n\n")

        report.write("## Filtered Events\n\n")

        if result["filtered_lines"]:
            for line in result["filtered_lines"]:
                report.write(f"- `{line}`\n")
        else:
            report.write("No events found for this filter.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze log files and generate a Markdown report."
    )

    parser.add_argument(
        "logfile",
        nargs="?",
        default="app.log",
        help="Path to the log file to analyze. Default: app.log",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="report.md",
        help="Output Markdown report file. Default: report.md",
    )

    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR", "ALL"],
        default="ALL",
        help="Filter events by level. Options: INFO, WARNING, ERROR, ALL. Default: ALL",
    )

    args = parser.parse_args()

    result = analyze_log(args.logfile, args.level)

    if result is None:
        return

    print_report(result)
    generate_markdown_report(result, args.output)

    print(f"\nReport generated: {args.output}")


main()