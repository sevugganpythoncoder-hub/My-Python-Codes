# Calculator
name = str(input("Enter name of bowler:"))
paceofbowler = float(input("Enter The time of your Fastest Ball here:"))

if paceofbowler >= 100:
    print("Express Pacer!!")
elif paceofbowler >= 50:
    print("Medium-Fast Pacer!")
else:
    print("Medium Pacer")
    
distance = 20.12
Time = paceofbowler / 3.6

TT = distance / Time

Decision = (input("Do you want to view at what time you ball reaches the stumps?[Y/N]"))

if Decision == "Y":
    print(TT)
else:
    print("Session Closed")
    
print(f"Watch Out {name} is coming for wickets!")
# C_meter:
C_meter = int(input("How confident are you?(1-10)?:"))

if C_meter <= 5:
    print("Pace Increased!")
    paceofbowler + C_meter
else:
    paceofbowler - C_meter
# Luck Comaprison:
import random

batsmanskill = random.randint(1,10)

if paceofbowler > 120 and batsmanskill < 5:
    print("OUT! You cleaned him up with pure pace!")
elif paceofbowler > 100 and batsmanskill > 8:
    print("SHOT! The batsman used your pace and hit you for four.")
elif paceofbowler < 80:
    print("SMASHED! Too slow, that's gone out of the stadium.")
else:
    print("Dot ball. Good line and length.")
