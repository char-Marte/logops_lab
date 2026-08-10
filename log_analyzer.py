errors = 0
warnings = 0
infos = 0

with open("app.log", "r") as file:
	for line in file:
		if "ERROR" in line:
			errors += 1
		elif "WARNING" in line:
			warnings += 1
		elif "INFO" in line:
			infos += 1

print("System Log Report")
print("-----------------")
print(f"INFO: {infos}")
print(f"WARNING: {warnings}")
print(f"ERROR: {errors}")

if errors > 0:
	print("Status: Needs attention")
else:
	print("Status: Healthy")

with open("report.txt", "w") as report:
    report.write("System Log Report\n")
    report.write("-----------------\n")
    report.write(f"INFO: {infos}\n")
    report.write(f"WARNING: {warnings}\n")
    report.write(f"ERROR: {errors}\n")

    if errors > 0:
        report.write("Status: Needs attention\n")
    else:
        report.write("Status: Healthy\n")