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
print("""NOTE : ------------------------------------------------------------------
PYTHON COMMAND INTERFACE (PCI) | v2.0 FINAL STABLE BUILD
Status: Completed
------------------------------------------------------------------
NOTE: This tool is optimized for System Recovery and Management. 
All core features (Process Kill, Disk List, Sys-Health) are active.
This CMD will no longer recieve Updates.
------------------------------------------------------------------
     """)

print("\nFor best of use make sure to install some of the libraries.[Ignore If not using a raw .py file]")

py = platform.python_version()
date = datetime.datetime.now()
print(fr"""
Python CMD Copyright Access [V.2.1/v Professional Stable] [Future updates?]
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
        print("Thank You for choosing Python CMD.")
        print("Exiting...")
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
                -del [Filename/dir name] : Deletes File/dir path(if admin)
                -clear history : Clears Cache and CMD history
                -ip-search : Fetches live Public External IP Address.
                -weather : Checks Weather of desired city(bonus)
                -sys-health : Checks {battery,cpu and RAM} components.
                -processlist : Shows the first 25 Processes Running in User's PC.
                -pykill : Kills The given Process.
                -disk-list : Shows Avaliable Disk Partitions In User's PC.
                -start : Creates a new instance of PythonCMD.
                -system restore : Creates a backup of the current folder used by python cmd.For more info type help['system restore']
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
        pattern = inputs[6:].strip().lower()
        found = False
        for root, dirs, files in os.walk(os.getcwd()):
            for item in files + dirs:
                if pattern in item.lower(): # Case-insensitive check
                    print(os.path.abspath(os.path.join(root, item)))
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
        print("End Date :            May 2026")
        print("Status         : V.2.0 Professional Build Stable(Completed)")
        print("---------------------------")
        print("""Special thanks to the PSF for the core engine
         Also to my friends and People for helping me with this endeavour and I Hope This project Helps Everybody
         Thank You.
        """)
        datas.append("Viewed Credits")
        save_settings(datas)
    elif inputs.startswith("pykill "):
        proc_name = inputs[7:]
        found = False
        print(fr"Searching for processes Matching name {proc_name}...")
        for proc in psutil.process_iter(["pid","name"]):

            try:
                if proc_name.lower() in proc.info["name"].lower():
                    print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})...")
                    proc.kill()
                    found = True

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if found:
            print("Process(es) terminated.")
            logging.info(f"{name} killed process: {proc_name} at {date}")
            datas.append(f"{name} Killed {proc_name} Successfully!")
            save_settings(datas)

        else:
            print(f"No Process named {proc_name}/process Unkilllable")
            logging.warning(f"{name} tried to kill {proc_name} at {date}")
            
    elif inputs == "processlist":
        print(f"{'PID':<8} {'Status':<12} {'Name'}")
        print("-" * 30)
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                # Print the first 25 processes
                print(f"{proc.info['pid']:<8} {proc.info['status']:<12} {proc.info['name']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    elif inputs == "disk-list":
        print(f"{'Device':<15} {'Mount':<10} {'Type':<10} {'Total (GB)':<10}")
        print("-" * 50)
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                print(f"{part.device:<15} {part.mountpoint:<10} {part.fstype:<10} {usage.total // (1024**3):<10}")
            except (PermissionError, OSError):
                continue

    elif inputs.strip() == "start":
        try:
            current_file = os.path.abspath(sys.argv[0])
        
            if current_file.endswith(".exe"):
                # Exe files usually have their own loop, so this should stay open
                subprocess.Popen([current_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
                logging.info(f"Created instance  by {name} using .exe")
            else:
                # For .py files, we wrap it in a 'cmd /k' call
                # '/k' tells the console to "run this command and STAY OPEN"
                subprocess.Popen(
                f'cmd /k "{sys.executable} {current_file}"', 
                creationflags=subprocess.CREATE_NEW_CONSOLE
                ) 
                logging.info(f"Created instance  by {name} using .py")
            
            print("INFO: Launching new PythonCMD instance...")
            datas.append(fr" {name} Opened a new instance")
        except Exception as e:
            print(f"ERROR: Could not start new instance: {e}")
            logging.warning(f"Python CMD Failed To open Instance : {e}")
            
    elif inputs.startswith("del "):
        filename = inputs[4:].strip()
        try:
            def deletefile(target):
                try:
                    # 1. Check if it's a Directory (Folder) FIRST
                    if os.path.isdir(target):
                        shutil.rmtree(target)
                        print(f"Path {target} has been removed from system OS")
                        logging.info(f"{name} deleted folder {target}")
                
                   # 2. Check if it's a File SECOND
                    elif os.path.isfile(target):
                        os.remove(target)
                        print(f"File {target} has been removed from the system OS")
                        logging.info(f"{name} deleted file {target}")
                
                    else:
                        print("ERROR : File/Path Not Found".center(50,"-"))
            
                except PermissionError:
                    print(" ERROR : Access Denied (Run as Admin) ".center(50, "!"))

                deletefile(filename) 
        
        except Exception as exc:
            logging.info(f"{name} logged due to technical error ERROR NO: 0XCB39266")
            # Optional: change to print(exc) if you don't want the app to close on error
            raise RuntimeError("Error : Exited system Due to Win error")
    elif inputs.strip() == "system restore":
        try:
            # 1. Define what to back up (Current working directory)
            source = os.getcwd()
        
            # 2. Create a unique folder name using the date and time
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_folder = f"Restore_Point_{now}"
        
            print(f"INFO: Initializing System Restore Point: {backup_folder}...")
        
            # 3. Copy everything. 
            # ignore_patterns ensures we don't back up the backup folder itself!
            shutil.copytree(source, backup_folder, ignore=shutil.ignore_patterns('Restore_Point_*', 'build', 'dist'))
        
            print(f"SUCCESS: Snapshot created at {backup_folder}".center(50, "="))
            datas.append(fr" {name} Created System Restore Point: {now}")
            save_settings(datas)
        except (Exception as e):
            print("ERROR: System Restore Call Not accepted/Failed")
            logging.warning(f"SYSTEM RESTORE FAILURE")
    elif inputs == "help['systemrestore']":
        print("INFO : ['Systemrestore']")
        print("USE : Creates a Carbon Copy of the folder the user is using to run pythoncmd. ")
        print(fr"For E.g: if the user runs the CMD in C:\users\[yourname]\[dirpath] it will create a copy of that folder")
        print(f"\n NOTE: This Command is for Educational/Emergency Purposes only. This command although Enforced with safety features Can drain your system Space Very quickly as well as Potentially Damage the system.")
        print("Use the command When needed and Wisely.You have been Warned.")
    else:
        print("Command Not In Current Version of Python CMD or there is no existing command")
        
        
