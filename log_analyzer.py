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

    with open("report.txt", "w") as report:
        report.write("System Log Report\n")
        report.write("-----------------\n")
        report.write(f"File analyzed: {file_path}\n")
        report.write(f"INFO: {infos}\n")
        report.write(f"WARNING: {warnings}\n")
        report.write(f"ERROR: {errors}\n")
        report.write(f"Status: {status}\n")


def main():
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        log_file = "app.log"

    analyze_log(log_file)


main()