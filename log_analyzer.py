import sys
import os


def analyze_log(file_path):
    infos = 0
    warnings = 0
    errors = 0

    if not os.path.exists(file_path):
        print(f"Error: file '{file_path}' not found.")
        return

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1
            elif "INFO" in line:
                infos += 1

    print("System Log Report")
    print("-----------------")
    print(f"File analyzed: {file_path}")
    print(f"INFO: {infos}")
    print(f"WARNING: {warnings}")
    print(f"ERROR: {errors}")

    if errors > 0:
        status = "Needs attention"
    else:
        status = "Healthy"

    print(f"Status: {status}")

    with open("report.md", "w") as report:
        report.write("# System Log Report\n\n")
        report.write(f"**File analyzed:** `{file_path}`\n\n")
        report.write(f"## Summary\n\n")
        report.write(f"- INFO: {infos}\n")
        report.write(f"- WARNING: {warnings}\n")
        report.write(f"- ERROR: {errors}\n\n")
        report.write(f"## Status\n\n")
        report.write(f"**{status}**\n")


def main():
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = "app.log"

    analyze_log(log_file)


main()