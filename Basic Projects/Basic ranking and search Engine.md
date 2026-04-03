current_squad = [{"Name" : "Sevuggan", "PythonLevel" : 0,"Status" : "Junior"},{"Name" : "Mohammed", "PythonLevel" : 0, "Status" : "Junior"},{"Name" : "Cam", "PythonLevel" : 0,"Status" : "Junior"}]


# Ranking
def Update_progress(player,XpBoost):
    player["PythonLevel"] = player["PythonLevel"] + XpBoost
    
    if player["PythonLevel"] >= 30:
        player["Status"] = "Senior_Advisor"
    elif player["PythonLevel"] >= 20:
        player["Status"] = "Sub_Director"
    else:
        print("Junior")

for e in Current_squad:
    XpBoost = int(input(f"How much exp did {e["Name"]} get? :"),)
    Update_progress(e,XpBoost)
    
for person in Current_squad:
    print(f"{person["Name"]}'s XP gained is {person["Status"]}")
    
Searcher = input("\n Who do you want to look up?:")
# Search engine
found = False
for person in Current_squad:
    if Searcher == person["Name"]:
         print(f"Match found! {person["Name"]} is a {person["Status"]}!")
         found = True
if not found:
    print("player not in database...")
    
    

# Search engine 2:
while True:
    print("\n1. Update XP\n2. Search Player\n3. Exit")
    choice = input("What do you want to do? ")

    if choice == "1":
        retry = input("Who's XP do you want to modify??: ")
        new_XpBoost = int(input("Please ENTER the XP amount: ")) # Use int() for math!
        
        found = False
        for person in Current_squad: # YOU NEED THIS LOOP HERE
            if retry == person["Name"]:
                Update_progress(person, new_XpBoost) # Re-use your function!
                print(f"Updated! {person['Name']} is now {person['Status']}")
                found = True
        if not found:
            print("Name not found.")

    elif choice == "2":
        data = input("Which Player Do You want to search up? ")
        found = False
        for person in Current_squad: # AND THIS LOOP HERE
            if data == person["Name"]:
                print(f"Match found! {person['Name']} is a {person['Status']}")
                found = True
        if not found:
            print("Name not found.")
    elif choice == "3":
        print("Closing System... Goodbye!")
        break # This is the "Kill Switch" that stops the loop
    else:
        print("Invalid choice, try again!")
