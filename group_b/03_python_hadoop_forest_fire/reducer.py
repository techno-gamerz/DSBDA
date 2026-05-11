import sys

current_month = None
sum_area = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 2:
        continue
    month, area_str = parts
    try:
        area = float(area_str)
    except ValueError:
        continue

    if current_month is None:
        current_month = month

    if month != current_month:
        avg = sum_area / count if count else 0.0
        print(f"{current_month}\t{avg:.4f}")
        current_month = month
        sum_area = 0.0
        count = 0

    sum_area += area
    count += 1

if current_month is not None:
    avg = sum_area / count if count else 0.0
    print(f"{current_month}\t{avg:.4f}")
