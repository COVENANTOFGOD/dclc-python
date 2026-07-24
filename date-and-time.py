
#Exercise 10: Convert String Into Datetime Object

from datetime import datetime

date_string = "20 January, 2025"

dt = datetime.strptime(date_string, "%d %B, %Y")

print("DateTime object:", dt)