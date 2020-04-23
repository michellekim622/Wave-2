import datetime

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
monthname = input("Enter the name of month: ")

if monthname == "February":
    currentYear = int(datetime.datetime.today().year)
    if (currentYear%4==0):
        print("number of days: 29 days")
    else: 
        print("number of days : 28 days")
elif monthname in ("April", "June", "September", "November"):
   print("number of days: 30 days")

elif monthname in ("January", "March", "May", "July", "August", "October", "December"):   
   print("number of days: 31 days")

else:
   print("Wrong month name")
