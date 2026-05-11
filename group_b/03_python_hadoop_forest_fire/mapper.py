import csv
import sys

reader = csv.reader(sys.stdin)
header = next(reader, None)

for row in reader:
    if not row:
        continue
    if len(row) < 13:
        continue
    month = row[2].strip().lower()
    area_str = row[12].strip()
    try:
        area = float(area_str)
    except ValueError:
        continue
    if not month:
        continue
    print(f"{month}\t{area}")
