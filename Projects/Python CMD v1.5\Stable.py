# All Modules used
import sys
import os
import datetime
import logging#Install
import time
import random
import subprocess#install
import shutil
import platform
import socket
import json 
import glob#install
import requests
import psutil#install

# Starting
print("""NOTE : All bugs have been Fixed up to current version,if there are still anymore I will try my best to cover them and this CMD may or may not recieve Future Updates.
     """)

print("\nFor best of use make sure to install some of the libraries.")

py = platform.python_version()
date = datetime.datetime.now()
print(fr"""
Python CMD Copyright Access [V.1.5/v Stable] [Future updates?]
64-bit Python {py} | {date}
Type 'Copyright' or 'help' or 'credits' for more info
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
                -file : Copies/moves Directories
                -systemdata: View IP/Hostname
                -cmd history: View session data
                -sysinfo : View OS and python version
                -where [file] : Shows where the given file is located
                del [Filename/dir name] : Deletes File/dir path(if admin)
                clear history : Clears Cache and CMD history
                ip-search : Fetches live Public External IP Address.
                weather : Checks Weather of desired city(bonus)
                sys-health : Checks {battery,cpu and RAM} components.
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
    elif inputs == "sysinfo":
        print(f"OS : {platform.system()} {platform.release()}")
        print(f"Current Version pf py : {py}")
        datas.append(f"{name} checked systeminfo")
        save_settings(datas)
    elif inputs.startswith("where "):
        pattern = inputs[6:].strip()
        found = False
        for root, dirs, files in os.walk(os.getcwd()):
            # Use glob.glob to match the pattern in each specific folder
            for match in glob.glob(os.path.join(root, pattern)):
                print(os.path.abspath(match))
                found = True
        if not found:
            print(f"INFO: Could not find '{pattern}' in {os.getcwd()} or subfolders.")
        datas.append(fr" {name} Deep searched: {pattern}")
        save_settings(datas)
    elif inputs.startswith("del "):
        filename = inputs[4:].strip()
        try:
            def deletefile(filename):
                try:
                    if os.path.exists(filename):
                        os.remove(filename)
                        print(fr"File {filename} has been {'.strip()'.title()}ed from the system OS")
                        logging.info(f"{name} deleted {filename}")
                    elif os.path.isdir(filename):
                        shutil.rmtree(filename)
                        print(f"Path {filename} has been {'.strip()'.title()}ed from system OS")
                    else:
                        print("ERROR : File Not Found".center(50,"-"))
                except PermissionError:
                    print(" ERROR : Access Denied (Run as Admin) ".center(50, "!"))

            deletefile(filename) 
            
        except Exception as exc:
             logging.info(f"{name} logged due to technical error ERROR NO: 0XCB39266")
             raise RuntimeError("Error : Exited system Due to Win error")
    elif inputs == "clear history":
        print(f"Clearing {name}'s CMD history....")
        time.sleep(10)
        datas = []
        save_settings(datas)
        print(datas)
        print("System cleared")
    elif inputs == "ip-search":
        print("\nFetching external System data....")
        time.sleep(5)
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            ip_data = response.json()
            print(f"Public IP Address: {ip_data['ip']}")
            datas.append(f"Used ip-search by {name}")
            save_settings(datas)
            logging.info(f"{name} fetched external IP successfully.")
        except requests.exceptions.RequestException as e:
            print(f"404 Error Failed To connect Successfully to server {e} ")
            logging.warning(fr"Exception Failed {e}")
    elif inputs == "weather":
        city = input("Check weather for which city?:")
        API = "8b4e2dab8c147748870c641bb2e35446"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
        try:
            print(f"Checking conditions for {city}...")
            time.sleep(7)
            response = requests.get(url)
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            print(f"--- Final Summary ---")
            print(f"Temp: {temp}°C | Conditions: {desc.title()}")
            print(f"Humidity: {humidity}%")
        
            datas.append(f"Checked weather by {name}: Current Temp {temp}C")
            save_settings(datas)
        except Exception as e:
            print(f"Error Could Not Access Server/Server down : {e}")
            time.sleep(3)
            logging.warning(f"Access to Server failed : {e}. At {date}")
    elif inputs == "sys-health":
        print("--- SYSTEM HEALTH DASHBOARD ---")
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"CPU Load: {cpu_usage}%")
            
            memory = psutil.virtual_memory()
            print(f"RAM Usage: {memory.percent}% ({memory.used // (1024**2)}MB / {memory.total // (1024**2)}MB)")
            total, used, free = shutil.disk_usage("/")
            print(f"Disk Space: {(used/total)*100:.1f}% used ({free // (1024**3)}GB Free)")
            
            battery = psutil.sensors_battery()
            if battery:
                #list comprehension
                print(f"Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Discharging)'}")
            logging.info(f"{name} performed a system health check.")
            datas.append("Performed sys-health check")
            save_settings(datas)
            print("-------------------------------")
            
        except PermissionError as e:
            logging.warning("User System Access denied.")
            print("Error could not access User System")
            
    elif inputs == "credits":
        print("--- CMD PROJECT CREDITS ---")
        print("Language       : Python 3.12")
        print("Build/Start Date     : Feb 2026")
        print("Status         : V.1.5 Build Stable")
        print("---------------------------")
        print("""Special thanks to the PSF for the core engine
         Also to my friends and People for helping me with this endeavour and I hope to finish this project soon.
        """)
        datas.append("Viewed Credits")
        save_settings(datas)
        
    else:
        print("Command Not In Current Version of Python CMD or there is no existing command")
        
        
