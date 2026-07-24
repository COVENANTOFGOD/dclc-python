#Exercise 1: Print Current Date and Time

from datetime import datetime

now = datetime.now()

print("Current date and time:", now)



#Exercise 2: Format DateTime

from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%b-%Y %I:%M:%S %p")

print("Formatted:", formatted)



#Exercise 3: Find Day of Week

from datetime import datetime

date = datetime(2025, 1, 15)

day = date.strftime("%A")

print("Day of the week:", day)


#Exercise 4: Convert Datetime into String

from datetime import datetime

dt = datetime(2025, 6, 15, 10, 30, 45)

date_string = dt.strftime("%Y-%m-%d, %H:%M:%S")

print("DateTime as string:", date_string)



#Exercise 5: Extract Components

from datetime import datetime

dt = datetime(2025, 8, 20, 14, 35, 50)

print("Year:", dt.year)
print("Month:", dt.month)
print("Day:", dt.day)
print("Hour:", dt.hour)
print("Minute:", dt.minute)
print("Second:", dt.second)



#Exercise 6: Print Time with AM/PM

from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%I:%M %p")

print("Current time:", formatted_time)



#Exercise 7: Print Current Time in Milliseconds

from datetime import datetime

current_time = datetime.now()

formatted = current_time.strftime("%H:%M:%S.%f")[:-3]

print("Current time with milliseconds:", formatted)


#Exercise 8: Get the Day of the Year

from datetime import datetime

date = datetime(2025, 3, 15)

day_number = date.timetuple().tm_yday

print("Day of the year:", day_number)


#Exercise 9: Combine Date and Time Objects

from datetime import date, time, datetime

d = date(2025, 5, 20)
t = time(9, 45, 0)

combined = datetime.combine(d, t)

print("Combined datetime:", combined)


#Exercise 10: Convert String Into Datetime Object

from datetime import datetime

date_string = "20 January, 2025"

dt = datetime.strptime(date_string, "%d %B, %Y")

print("DateTime object:", dt)