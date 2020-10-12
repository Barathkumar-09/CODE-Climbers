day=''' Enter the number of the day:
        1.sunday
        2.Monday
        3.Tuesday
        4.Wednesday
        5.Thrusday
        6.Friday
        7.Saturday'''
print (day)
a=input()
a=float(a)
b=int(a)
if(b==1):
    print(b," is SUNDAY")
elif(b==2):
    print(b," is MONDAY")
elif(b==3):
    print(b," is TUESDAY")
elif(b==4):
    print(b," is WEDNESDAY")
elif(b==5):
    print(b," is THRUSDAY")
elif(b==6):
    print(b," is FRIDAY")
elif(b==7):
    print(b," is SATURDAY")
else:
    print("WRONG INPUT!!")
