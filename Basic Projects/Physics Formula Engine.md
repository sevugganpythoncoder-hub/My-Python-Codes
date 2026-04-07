# All libraries used:
import math
import json
# Save and load:
def load_settings():
    try:
        with open("Formula.json","r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDEcodeError):
        return "History not Found/Appended"
def save_settings(Data):
    with open("Formula.json", "w") as f:
        return json.dump(Data,f)

History = []
# Formula Calculator:
while True:
    print("\n---Physics laws calculator---")
    print("Ohm's law(V = I * R)")
    print("Mirror Formula(1/f = 1/v - 1/u):")
    print("Lens Formula(1/f = 1/v + 1/u):")
    print("Snells law(n = sin(i)/ sin(r))")
    print("Power law(P = V * I):")
    print("Save and exit:")
    ask = int(input("Which of the following Laws Would you like to use?  Press[1,2,3,4,5,6]:"))
# Ohm's Law
    if ask == 1:
        print("\n Ohm's law")
        I = float(input("Enter value of Current(I):"))
        R = float(input("Enter value of Resistance(R):"))
        result = I * R
        print(f" V : {result}")
        History.append(result)
        print("Data Appended")
# Mirror Formulas:
    elif ask == 2:
        print("\n Mirror formula")
        F =  float(input("Enter value of Focal length:"))
        v1 = float(input("Enter value of Image Distance:"))
        u = float(input("Enter value of Object distance:"))
        C = input("Is mirror concave or convex?:").upper()
        if C == "CONCAVE":
            result = (1/-F - (-1/v1) - 1/u)
            print(result)
        else:
            result = (1/F - (1/v1) - 1/-u)
            print(result)
        History.append(result)
        print("Data Appended")     
    elif ask == 3:
        print("\n Lens Formula:")
        f =  float(input("Enter value of Focal length:"))
        v2 = float(input("Enter value of Image Distance:"))
        u1 = float(input("Enter value of Object distance:"))
        result = 1/f- 1/v2 + 1/u
        print(result)
        History.append(result)
        print("Data Appended")
  # Smell's law
    elif ask == 4:
        print("\n Snells Law:")
        i = float(input("Enter angle of Incidence:"))
        r = float(input("Enter angle of refraction::"))
        a = math.radians(i)
        b = math.radians(r)
        n = math.sin(a)/ math.sin(b)
        print(f" n : {n}")
        History.append(result)
        print("Data Appended")
# Power's law
    elif ask == 5:
        print("Power's Law:")
        V3 = float(input("Enter value of V:"))
        I  = float(input("Enter value of I:"))
        result = V3 * I
        print(f"Power : {result}")
        History.append(result)
        print("Data Appended")
# save and exit
    elif ask == 6:
        print("Save and exit")
        save_settings(History)
        print("Settings saved!")
        break
    
