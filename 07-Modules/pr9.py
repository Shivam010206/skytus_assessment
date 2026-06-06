from datetime import date

date1 = date(2026, 6, 1)
date2 = date(2026, 6, 10)

difference = date2 - date1

print("Difference =", difference.days, "days")