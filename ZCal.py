from datetime import datetime, timedelta
import csv

with open("days.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        dayList = list(row)

with open("extraDays.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        extraDays = list(row)

with open("months.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        monthList = list(row)

dateString = input("Enter a date(MM/DD/YY): ")
dateObject = datetime.strptime(dateString, "%m/%d/%Y")

dayOne = datetime(1969, 8, 29)
diff = dateObject - dayOne
intDiff = int(diff.days)
yearMod = intDiff%365

if yearMod>359:
    print(dateString + " is " + extraDays[yearMod-360] + " (gatha)")

else:
    month = monthList[int(yearMod/30)]
    day = dayList[int(yearMod%30)]
    print(dateString + " is " + day + " (" + month + ")")
