from datetime import date , time , datetime
today = date.today()
now = datetime.now()
print("Today's date is " , today)
print("\nCurrent Date and Time is " , now)
print("\n Date components" , today.year,today.month,today.day)