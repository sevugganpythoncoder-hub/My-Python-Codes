# Save data
import json
def load_settings():
    try:
        with open("Save.json","r") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return [{"Name" : "None","Balls_Played" : 0, "Runs_Scored" : 0,"Strike_rate" : "0","Wickets" : 0},{"Name2" : "None","Balls_Played2" : 0, "Runs_Scored2" : 0,"Strike_rate2" : "0","Wickets2" : 0}]
        
def save_settings(Data):
    with open("Save.json", "w") as f:
        json.dump(Data, f)

player_stats = [{"Name" : "None","Balls_Played" : 0, "Runs_Scored" : 0,"Strike_rate" : "0","Wickets" : 0},{"Name2" : "None","Balls_Played2" : 0, "Runs_Scored2" : 0,"Strike_rate2" : "0","Wickets2" : 0}]
# User inputs and Cricket Simulation:
Name = input("Enter Person In strike:")
Name2 = input("Enter Person In Non-striker's end:")

player_stats[0]["Name"] = Name
player_stats[1]["Name2"] = Name2


Decision = input("Do you want to look at striker's stats?[Y/N]").upper()

if Decision == "Y":
    print(player_stats[0])
else:
    print("Next Step")

Total_runs2 = 0
Total_runs3 = 0
for i in range(1,7):
    Userinput = int(input(f"How many runs in ball {i}?"))
    Total_runs2 += Userinput
WicketsChecker = input("Are any wickets taken this over?[Y/N]")

if WicketsChecker == "Y":
    print(f"{player_stats[0]["Name"]} is OUT")
    print(f"{player_stats[1]["Name2"]} is on strike!")
    for i in range(1,7):
        Userinput2 = int(input(f"How many runs in ball {i}?"))
        Total_runs3 += Userinput2
WicketsChecker = input("Are any wickets taken this over?[Y/N]")
if WicketsChecker == "Y":
    print("ALL OUT")
    short = input("Would you like to view team stats?[Y/N]").upper()
    if short == "Y":
        print(f"Total Runs scored by {player_stats[0]["Name"]} is {Total_runs2}")
        print(f"Total Runs scored by {player_stats[1]["Name2"]} is {Total_runs3}")
player_stats[0]["Runs_Scored"] = Total_runs2
player_stats[1]["Runs_Scored2"] = Total_runs3

Balls_played = 6
player_stats[0]["Balls_Played"] = Balls_played
player_stats[1]["Balls_Played2"] = Balls_played
economy1 = Total_runs2/ Balls_played
economy2 = Total_runs3 / Balls_played
player_stats[0]["Economy"] = economy1
player_stats[1]["Economy2"] = economy2

strike_rate = Total_runs2 / Balls_played * 100
strike_rate2 = Total_runs3 / Balls_played * 100
player_stats[0]["Strike_rate"] = strike_rate
player_stats[1]["Strike_rate2"] = strike_rate2

# --- FINAL SUMMARY ---
Decision2 = input("\nWould you like to view the full match summary? [Y/N]: ").upper()

if Decision2 == "Y":
    print("\n--- MATCH SUMMARY ---")
    print(f"Striker ({player_stats[0]['Name']}): {Total_runs2} runs, SR: {strike_rate}")
    print(f"Non-Striker ({player_stats[1]['Name2']}): {Total_runs3} runs, SR: {strike_rate2}")
    print("Full Data Object:", player_stats)

# --- THE SAVE ---
Decision3 = input("\nWould you like to save this performance to your career file? [Y/N]: ").upper()

if Decision3 == "Y":
    save_settings(player_stats)
    print("✅ Stats successfully saved to Save.json! Career updated.")
else:
    print("❌ Data not saved. Session ended.")  
