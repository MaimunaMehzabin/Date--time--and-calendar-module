import calendar

yy = int(input("Enter your birth year : "))
mm = int(input("Enter your birth month (as integer) : "))

month = calendar.month(yy, mm)

print(month)