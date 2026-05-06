import random
import json

# MAIN CODE
# Settings
try:
    total_overs = int(input("How many over's match?: "))
except ValueError:
    total_overs = 1
    
max_wickets = 3

def setup_team(team_name):
    print(f"\n--- Enter 4 Players for {team_name} ---")
    return [{"Name": input(f"Player {i+1}: "), "Runs": 0, "Balls": 0} for i in range(4)]

def play_innings(batting_team, team_name, target=None):
    print(f"\n" + "="*40 + f"\nINNINGS: {team_name}")
    if target: print(f"TARGET TO WIN: {target}")
    
    striker_idx, non_striker_idx, next_player_idx = 0, 1, 2
    total_runs, wickets, legal_balls_bowled = 0, 0, 0
    total_balls_to_bowl = total_overs * 6
    
    current_bowler = "" 
    last_bowled_over = 0 
    
    while legal_balls_bowled < total_balls_to_bowl:
        if wickets >= max_wickets:
            print("--- ALL OUT! ---")
            break
            
        current_over = (legal_balls_bowled // 6) + 1
        ball_in_over = (legal_balls_bowled % 6) + 1
        
        if ball_in_over == 1 and last_bowled_over < current_over:
            current_bowler = input(f"\nWho is bowling Over {current_over}?: ")
            last_bowled_over = current_over
        
        print(f"\n{current_over}.{ball_in_over} | Bowler: {current_bowler} to {batting_team[striker_idx]['Name']}")
        action = input("Enter Runs (0-6), 'W', 'WD', or 'NB': ").upper()
        
        # --- ACTIONS SECTION ---
        if action == 'WD':
            total_runs += 1
            print(f"WIDE! 1 run added. Re-bowl.")
            continue 

        elif action == 'NB':
            total_runs += 1
            print(f"NO BALL! 1 run added. FREE HIT / LIFE!")
            next_action = input("What happened on the NB? (Runs or 'W' for no out): ").upper()
            if next_action == 'W':
                print("LUCKY! It was a No Ball, so you are NOT OUT!")
            else:
                try:
                    r = int(next_action)
                    total_runs += r
                    batting_team[striker_idx]["Runs"] += r
                    if r in [1, 3]:
                        striker_idx, non_striker_idx = non_striker_idx, striker_idx
                except: pass
            continue

        elif action == 'W':
            wickets += 1
            legal_balls_bowled += 1
            batting_team[striker_idx]["Balls"] += 1
            if wickets < max_wickets:
                print(f"OUT! {current_bowler} gets the wicket! New Batsman: {batting_team[next_player_idx]['Name']}")
                striker_idx = next_player_idx
                next_player_idx += 1
            
            if legal_balls_bowled % 6 == 0 and legal_balls_bowled != total_balls_to_bowl:
                striker_idx, non_striker_idx = non_striker_idx, striker_idx
            continue

        else:
            # Handle Normal Runs
            try:
                runs = int(action)
                total_runs += runs
                batting_team[striker_idx]["Runs"] += runs
                batting_team[striker_idx]["Balls"] += 1
                legal_balls_bowled += 1
                
                if runs in [1, 3]:
                    striker_idx, non_striker_idx = non_striker_idx, striker_idx
                
                if legal_balls_bowled % 6 == 0 and legal_balls_bowled != total_balls_to_bowl:
                    striker_idx, non_striker_idx = non_striker_idx, striker_idx

                if target and total_runs >= target:
                    break
            except ValueError:
                print("Invalid input!")

    return total_runs, wickets

def show_scorecard(team_name, players, total):
    print(f"\n--- SCORECARD: {team_name} ({total} runs) ---")
    print(f"{'Name':<15} {'Runs':<5} {'Balls':<5} {'SR':<5}")
    for p in players:
        sr = (p['Runs'] / p['Balls'] * 100) if p['Balls'] > 0 else 0.0
        print(f"{p['Name']:<15} {p['Runs']:<5} {p['Balls']:<5} {sr:<5.2f}")

# --- EXECUTION ---
t_a_name = input("Team A (Batting First): ")
t_b_name = input("Team B (Bowling First): ")
t_a_p = setup_team(t_a_name)
t_b_p = setup_team(t_b_name)

s1, w1 = play_innings(t_a_p, t_a_name)
s2, w2 = play_innings(t_b_p, t_b_name, s1+1)

res = f"{t_b_name} won" if s2 > s1 else (f"{t_a_name} won" if s1 > s2 else "Tie")

show_scorecard(t_a_name, t_a_p, s1)
show_scorecard(t_b_name, t_b_p, s2)
print(f"\n***** {res.upper()} *****")

# --- THE SAVE BLOCK ---
match_data = {
    "match_info": {
        "teams": [t_a_name, t_b_name],
        "winner": res,
        "overs": total_overs
    },
    "scorecards": {
        t_a_name: t_a_p,
        t_b_name: t_b_p
    }
}

with open("match_save.json", "w") as f:
    json.dump(match_data, f, indent=4)

print("\n[SYSTEM] Match saved to match_save.json. Archive Complete.")
