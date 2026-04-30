# All Modules used
import sys
import os
import datetime
import logging
import time
import random
import subprocess
import shutil
import platform
import socket
import json 

# Starting
print("NOTE THERE WILL BE A LOT OF BUG SINCE THIS IS ONLY THE BETA.If you have any suggestions Please Don't hesitate to text me in  my Githubpage(sevugganPythoncoder)")

date = datetime.datetime.now()
print(fr"""
Python CMD Copyright Access [V.1.1/v beta] [Future updates]
64-bit Python 3.14.x | {date}
Type 'Copyright' or 'help' for more info
""")

# Inputs
name = input("Enter name:")
print("\nStarting CMD.....")
time.sleep(4)

# Main CMD functions
def load_settings():
    try:
        with open("CMD.json","r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        
def save_settings(Data):
    with open("CMD.json","w") as f:
        json.dump(Data,f)

# Initialize logging correctly before the loop
logging.basicConfig(filename='ghost_mode.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
datas = load_settings()

while True:
    date = datetime.datetime.now()
    inputs = input(f"{os.getcwd()}>").lower().strip()
  # Exit
    if inputs == "exit":
        logging.info(f"{name} Exited the CMD at {date}")
        print("Logged info")
        time.sleep(3)
        sys.exit()
  # date and time        
    elif inputs == "date and time":
        print(f"Current Time: {date}")
        datas.append(str(date))
        save_settings(datas)
  # random  
    elif inputs == "random":
        choiceinp = input("Heads or Tails? ")
        choice = random.choice(["heads", "tails"]) 
        if choiceinp.lower() == choice:
            print("You won the toss!")
            logging.info(f"{name} won the toss")
            datas.append("Win")
            save_settings(datas)
        else:
            print(f"You lost. It was {choice}.")
            logging.info(f"{name} lost the toss")
            datas.append("Lose")
            save_settings(datas)
   # run [commands]
    elif inputs.startswith("run "):
        command = inputs[4:]
        subprocess.run(command, shell=True)
        logging.info(f"{name} executed system command: {command}")
        datas.append(command)
        save_settings(datas)
  # cd [command]
    elif inputs == "cd" or inputs.startswith("cd "):
        path = inputs[3:].strip()
        if not path:
            print("Exited Safely Due to error")
            print(os.getcwd())
        else:
            try:
                os.chdir(path)
                logging.info(f"{name} checked {path} at {date}")
                print(f"Moved to: {os.getcwd()}")
                datas.append(f"Changed to {path}")
                save_settings(datas)
            except FileNotFoundError:
                 print("Such file is not found in Directory")
                 logging.warning("File not found!!!")
            except Exception as e:
                 print(f"Error : {e}")
                 logging.warning("File Exception Error!!")
 # file [Source,destination]      
    elif inputs == "file":
        action = input("Type 'cp' to copy or 'mv' to move: ").strip().lower()
        source = input("Enter source path: ")
        destination = input("Enter destination path: ")
    
        try:
            if action == "cp":
                shutil.copy(source, destination)
                print("File copied successfully.")
            elif action == "mv":
                shutil.move(source, destination)
                print("File moved successfully.")
        
            datas.append(f"{action} from {source} to {destination}")
            save_settings(datas)
        
        except Exception as e:
            print(f"Error: {e}")
  # systemdata        
    elif inputs == "systemdata":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Device: {hostname}, Ip : {ip_address}")
        logging.info(f"Device: {hostname}, Ip : {ip_address}")
  # cmd history
    elif inputs == "cmd history":
        print(f"History : {datas}")
        datas.append("Checked CMD history")
        save_settings(datas)
  # help
    elif inputs == "help":
        print("\nPrinting All avaliable current commands....")
        time.sleep(3)
        print(""" -Exit: Exits the Cmd
                -Date and Time: Shows date and time
                -Random : Picks a random option
                -run [Command] : Execute system tasks
                -cd [Path] : Change directory
                -file [File] : Copies/moves Directories
                -systemdata: View IP/Hostname
                -cmd history: View session data
                """)
  # copyright
    elif inputs == "copyright":
        print("-" * 60)
        print("PYTHON COMMAND INTERFACE (PCI) - SYSTEM MANAGEMENT TOOL")
        print(f"Copyright (c) {datetime.datetime.now().year} {name}. All Rights Reserved.")
        print("-" * 60)
        print("""
        LEGAL NOTICE:
        This software is provided "as is", without warranty of any kind, 
        express or implied, including but not limited to the warranties 
        of merchantability, fitness for a particular purpose and 
        non-infringement. 

        In no event shall the authors or copyright holders be liable 
        for any claim, damages or other liability, whether in an action 
        of contract, tort or otherwise, arising from, out of or in 
        connection with the software or the use or other dealings in 
        the software.

        UNAUTHORIZED REPLICATION OR DISTRIBUTION OF THIS SOURCE CODE 
        IS STRICTLY PROHIBITED.
        """)
        print("-" * 60)
        input("Press ENTER to return to the terminal...")
    else:
        print("Command Not In Current Version of Python CMD or there is no existing command")
        
