from datetime import date, time, datetime
x= datetime.now()
print(x)
today = date.today()
now= datetime.now()
print("today's date is", today)
print("\ncurrent date and time is", now)
print("\ndate components", today.year, today.month, today.day)