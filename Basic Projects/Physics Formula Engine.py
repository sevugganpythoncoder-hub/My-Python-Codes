# All libraries used:
import math
import json
# Save and load:
def load_settings():
    try:
        with open("Formula.json","r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return []
def save_settings(Data):
    with open("Formula.json", "w") as f:
        return json.dump(Data,f)
        
History = load_settings()

# Formula Calculator:
while True:
    print("\n---Physics laws calculator---")
    print("1) Ohm's law(V = I * R)")
    print("2) Mirror Formula(1/f = 1/v - 1/u):")
    print("3) Lens Formula(1/f = 1/v + 1/u):")
    print("4) Snells law(n = sin(i)/ sin(r))")
    print("5) Power law(P = V * I):")
    print("6) Save and exit:")
    print("7) Clear History")
    try:
        ask = int(input("Which of the following Laws Would you like to use?  Press[1,2,3,4,5,6]:"))
    except ValueError:
        print("Enter A correct number")
        continue
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
        f =  float(input("Enter value of Focal length:"))
        u = float(input("Enter value of Object distance:"))
        denominator =  (1/f) - (1/u)
        if denominator == 0:
            print("Image distance is at Infinity!")
            History.append("Infinity")
        else:
            v = 1/ denominator 
            print(round(v, 2))
            History.append(round(v, 2))
            print("Data Appended") 
    elif ask == 3:
        print("\n Lens Formula:")
        f =  float(input("Enter value of Focal length:"))
        u1 = float(input("Enter value of Object distance:"))
        denominator = (1/f) + (1/u1)
        if denominator == 0:
            print("Image Distance is at infinity!")
            History.append("Infinity")
        else:
            v = 1 / denominator
            print(round(v, 2))
            History.append(round(v, 2))
            print("Data Appended")  
  # Snell's law
    elif ask == 4:
        print("\n Snells Law:")
        i = float(input("Enter angle of Incidence:"))
        r = float(input("Enter angle of refraction::"))
        a = math.radians(i)
        b = math.radians(r)
        n = math.sin(a)/ math.sin(b)
        print(f" n : {n}")
        History.append(n)
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
        print(f"Final History log :{History}")
        print("Settings saved!")
        break
    elif ask == 7:
        Del = input("WARINING YOU ARE ABOUT TO CLEAR HISTORY would you liketo proceed?[Y/N]:").upper()
        if Del == "Y":
            History = []
            continue
        else:
            pass
