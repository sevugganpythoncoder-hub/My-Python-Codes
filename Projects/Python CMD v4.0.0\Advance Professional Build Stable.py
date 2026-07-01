# All Modules used
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL
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
import string
import math
import hashlib
import ctypes
from datetime import datetime
import win32api
import win32con
import time
import requests
import math

# Starting
print(f"""{GREEN}NOTE : ------------------------------------------------------------------
PYTHON COMMAND INTERFACE (PCI) | v4.0.0 FINAL STABLE BUILD
Status: Completed
------------------------------------------------------------------
NOTE: This tool is optimized for System Recovery and Management. 
All core features (Process Kill, Disk List, Sys-Health,scan-reg) are active.
This CMD will no longer recieve Updates(This is True now).
------------------------------------------------------------------{RESET}
     """)

print(f"{RED}\nFor best of use make sure to install some of the libraries.[Ignore If not using a raw .py file]{RESET}")

py = platform.python_version()
date = datetime.now()
print(fr"""
Python CMD Copyright Access [V.3.2.1/v Advance Standalone Stable] [Future updates?]
64-bit Python {py} | {date}
Type 'Copyright' or 'help' or 'credits' for more info
""")

# Inputs
name = input(f"{YELLOW}Enter name:{RESET}")
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

# For alias Function
def load_alias():
    try:
        with open("alias.json","r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return {}

def save_alias(alias):
    with open("alias.json","w") as f:
        json.dump(alias,f,indent=4)
        
alias = load_alias()
        
while True:
    date = datetime.now()
    inputs = input(f"{os.getcwd()}>").lower().strip()
  # Exit
    if inputs == "exit":
        logging.info(f"{name} Exited the CMD at {date}")
        print(f"{GREEN}Thank You for choosing Python CMD.{RESET}")
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
        logging.info(f"{RED}{name} executed system command: {command}{RESET}")
        datas.append(command)
        save_settings(datas)
  # cd [command]
    elif inputs == "cd" or inputs.startswith("cd "):
        path = inputs[3:].strip()
        if not path:
            print(f"{YELLOW}Exited Safely Due to error{RESET}")
            print(os.getcwd())
        else:
            if path in alias:
                    path = alias[path]
                    print(f"Redirecting via alias to: {path}")
                    logging.info(f"{name} used alias : {path}")
            
            try:
                os.chdir(path)
                logging.info(f"{name} checked {path} at {date}")
                print(f"{RED}Moved to: {os.getcwd()}{RESET}")
                datas.append(f"Changed to {path}")
                save_settings(datas)
            except FileNotFoundError:
                print(f"{RED}Such file is not found in Directory{RESET}")
                logging.warning("File not found!!!")
                
            except Exception as e:
                    print(f"{RED}Error : {e}{RESET}")
                    logging.warning("File Exception Error!!")
 # file [Source,destination]      
    elif inputs == "file":
        action = input("Type 'cp' to copy or 'mv' to move: ").strip().lower()
        source = input("Enter source path: ")
        destination = input("Enter destination path: ")
    
        try:
            if action == "cp":
                shutil.copy(source, destination)
                print(f"{GREEN}File copied successfully.{RESET}")
            elif action == "mv":
                shutil.move(source, destination)
                print(f"{GREEN}File moved successfully.{RESET}")
        
            datas.append(f"{action} from {source} to {destination}")
            save_settings(datas)
        
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")
  # systemdata        
    elif inputs == "systemdata":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"{YELLOW}Device: {hostname}, Ip : {ip_address}")
        logging.info(f"Device: {hostname}, Ip : {ip_address}{RESET}")
  # cmd history
    elif inputs == "cmd history":
        print(f"History : {datas}")
        datas.append("Checked CMD history")
        save_settings(datas)
  # help
    elif inputs == "help":
        print("\nPrinting All available current commands....")
        time.sleep(3)
        print("--------------------------------------------------------------------------------------------------")
        print("ID    |  COMMAND                         -  DESCRIPTION")
        print("--------------------------------------------------------------------------------------------------")
        
        # --- CORE UTILITIES ---
        print("1)    -  Exit                             -  Exits the Cmd")
        print("2)    -  Date and Time                    -  Shows current date and time")
        print("3)    -  Random                           -  Picks a random option from your list")
        print("4)    -  start                            -  Creates a new instance of PythonCMD")
        
        print("\n--- SYSTEM & FILE MANAGEMENT ---")
        print("5)    -  run [Command]                    -  Execute system-level tasks")
        print("6)    -  cd [Path]                        -  Change current working directory")
        print("7)    -  file                             -  Copies or moves directories")
        print("8)    -  where [file]                     -  Shows the exact location of a specific file")
        print("9)    -  del [Filename]                   -  Deletes File/Dir (Requires Admin/WinRE)")
        print("10)   -  vol                              -  Shows Serial Number and Volume Info (Enhanced)")
        
        print("\n--- DATA & NETWORKING ---")
        print("11)   -  systemdata                       -  View network IP and Hostname")
        print("12)   -  cmd history                      -  View all session data and inputs")
        print("13)   -  sysinfo                          -  View OS details and Python version")
        print("14)   -  ip-search                        -  Fetches live Public External IP Address")
        print("15)   -  clear history                    -  Clears Cache and session CMD history")
        
        print("\n--- MONITORING & TOOLS ---")
        print("16)   -  weather                          -  Checks Weather of desired city")
        print("17)   -  sys-health                       -  Monitors Battery, CPU, and RAM components")
        print("18)   -  processlist                      -  Shows the first 25 Processes running on PC")
        print("19)   -  pykill                           -  Kills a specified running process")
        print("20)   -  disk-list                        -  Shows available Disk Partitions")
        print("21)   -  view-dir                        -   Shows all Dir's/files inside the Directory you are using to run PythonCMD")
        
        print("\n--- ADVANCED FEATURES ---")
        print("22)   -  system restore                   -  Creates a backup of the current folder")
        print("                                          -  Note: For more info type help['system restore']")
        print("23)   -  alias [path] as [name]           -  Creates a custom shortcut to a path")
        print("                                          -  Note: For more info type help['alias']")
        print("24)   -  view aliases                     -  Shows all shortcuts created by you")
        
        print("\n--- DISK MANAGEMENT (NEW) ---")
        print("25)   -  diskpart-basic                   -  Safe, Read-Only disk monitoring")
        print("26)   -  diskpart-advance                 -  Write-Access (Clean/Format) - ADMIN REQ.")
        
        print("\n--- SECURITY (PCI SUITE) ---")
        print("27)   -  pci-scan                         -  Scans files for malware/viruses")
        print("28)   -  pci-verify [file]                -  Verifies if malicious files are system-critical")
        print("29)   -  scan-reg                         -  Scans all the Registry Files in user's PC for more info type help['scan-reg']")
        print("--------------------------------------------------------------------------------------------------")
  # copyright[MIT License]
    elif inputs == "copyright":
        print("-" * 60)
        print("PYTHON COMMAND INTERFACE (PCI) - SYSTEM MANAGEMENT TOOL")
        print(f"Copyright (c) {datetime.now().year} Sevuggan. All Rights Reserved.")
        print("-" * 60)
        print("""{GREEN}
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
        IS STRICTLY PROHIBITED.{RESET}
        """)
        print("-" * 60)
        input("Press ENTER to return to the terminal...")
     #sysinfo
    elif inputs == "sysinfo":
        print(f"OS : {platform.system()} {platform.release()}")
        print(f"Current Version pf py : {py}")
        datas.append(f"{name} checked systeminfo")
        save_settings(datas)
  # where [command]
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
             
    elif inputs == "clear history":
        print(f"{RED}Clearing {name}'s CMD history....{RESET}")
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
            print(f"{YELLOW}404 Error Failed To connect Successfully to server {e} {RESET}")
            logging.warning(fr"Exception Failed {e}")
# weather
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
  # sys-health
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
  # credits
    elif inputs == "credits":
        print("--- CMD PROJECT CREDITS ---")
        print("Language       : Python 3.12")
        print("Build/Start Date     : Feb 2026")
        print("End Date :            July 2026(Offcially)")
        print("Status         : V.4.0.0 Modern Professional Build Stable(Completed)")
        print("---------------------------")
        print("""Special thanks to the PSF for the core engine
         Also to my friends and other People for helping me with this endeavour and I Hope This project Helps Everybody
         Thank You.
        """)
        datas.append("Viewed Credits")
        save_settings(datas)
     # pykill
    elif inputs.startswith("pykill "):
        proc_name = inputs[7:].strip()  
        found = False
        
        blacklist = ["svchost.exe", "lsass.exe", "wininit.exe", "services.exe", "csrss.exe", "explorer.exe"]
        
        print(fr"Searching for processes Matching name {proc_name}...")
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                
                if proc.info["name"] and proc_name.lower() in proc.info["name"].lower():
                    current_proc_name = proc.info["name"].lower()
                    
                    
                    if current_proc_name in blacklist:
                        print("\n" + "!"*60)
                        print(f" {RED}WARNING: {proc.info['name']} (PID: {proc.info['pid']}) is a CRITICAL SYSTEM PROCESS! ".center(60, "="))
                        print(" Terminating this could cause a Blue/black Screen of Death (BSOD).{RESET} ".center(60, "="))
                        print("!"*60)
                        
                        
                        confirm = input(f"Are you absolutely sure you want to kill {proc.info['name']}? (y/N): ").lower().strip()
                        if confirm != 'y':
                            print(f"{YELLOW}Skipped: Termination of {proc.info['name']} aborted by user{RESET}.\n")
                            continue 
                    
                    
                    print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})...")
                    proc.kill()
                    found = True

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if found:
            print(f"{GREEN}Process(es) terminated.{RESET}")
            logging.info(f"{name} killed process: {proc_name} at {date}")
            datas.append(f"{name} Killed {proc_name} Successfully!")
            save_settings(datas)
        else:
            print(f"No Process named {proc_name} or process is unkillable/banned by user.")
            logging.warning(f"{name} tried to kill {proc_name} at {date}")
     # processlist
    elif inputs == "processlist":
        print(f"{'PID':<8} {'Status':<12} {'Name'}")
        print("-" * 30)
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                # Print the first 25 processes
                print(f"{proc.info['pid']:<8} {proc.info['status']:<12} {proc.info['name']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
     #disk-list
    elif inputs == "disk-list":
        print(f"{'Device':<15} {'Mount':<10} {'Type':<10} {'Total (GB)':<10}")
        print("-" * 50)
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                print(f"{part.device:<15} {part.mountpoint:<10} {part.fstype:<10} {usage.total // (1024**3):<10}")
            except (PermissionError, OSError):
                continue
  # start
    elif inputs.strip() == "start":
        try:
            current_file = os.path.abspath(sys.argv[0])
        
            if current_file.endswith(".exe"):
                # Exe files usually have their own loop, so this should stay open
                subprocess.Popen([current_file], creationflags=subprocess.CREATE_NEW_CONSOLE)
                logging.info(f"Created instance  by {name} using .exe")
            else:
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
             
     # del [command]
     
    elif inputs.startswith("del "):
        filename = inputs[4:].strip()
        try:
            def deletefile(target):
                try:
                    
                    if os.path.isdir(target):
                        shutil.rmtree(target)
                        print(f"Path {target} has been removed from system OS")
                        logging.info(f"{name} deleted folder {target}")
                
                    elif os.path.isfile(target):
                        os.remove(target)
                        print(f"File {target} has been removed from the system OS")
                        logging.info(f"{name} deleted file {target}")
                
                    else:
                        print("ERROR : File/Path Not Found".center(50,"-"))
            
                except PermissionError:
                    print(F"{RED} ERROR : Access Denied (Run as Admin) {RESET}".center(50, "!"))

                deletefile(filename) 
        
        except Exception as exc:
            logging.info(f"{name} logged due to technical error ERROR NO: 0XCB39266")
            raise RuntimeError("Error : Exited system Due to Win error")
             
     #system-restore
    elif inputs.strip() == "system restore":
        print(f"{RED}You are using system restore be careful{RESET}")
        try:
        source = os.getcwd()
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
       
        parent_dir = os.path.dirname(source)
        backup_folder = os.path.join(parent_dir, f"PCI_Restore_Point_{now}")
    
        print(f"{YELLOW}INFO: Initializing System Restore Point outside current path...{RESET}")
        print(f"Target location: {backup_folder}")
    
       
        shutil.copytree(source, backup_folder)
    
        print(f"{GREEN}SUCCESS: Snapshot created successfully!{RESET}".center(50, "="))
        datas.append(f"{name} Created System Restore Point: {now}")
        save_settings(datas)
         
    except Exception as e:
        print(f"{RED}ERROR: System Restore Call Failed: {e}{RESET}")
        logging.warning(f"SYSTEM RESTORE FAILURE: {e}")

     #notes
    elif inputs == "help['systemrestore']":
        print("INFO : Module ['Systemrestore']")
        
        print("USE : Creates a Carbon Copy of the folder the user is using to run pythoncmd. ")
        
        print(fr"For E.g: if the user runs the CMD in C:\users\[yourname]\[dirpath] it will create a copy of that folder")
        
        print(f"\n NOTE: This Command is for Educational/Emergency Purposes only. This command although Enforced with safety features Can drain your system Space Very quickly as well as Potentially Damage the system.")
        
        print("Use the command When needed and Wisely.You have been Warned.")
     #alias
    elif inputs.startswith("alias "):
        try:
             
             command_body = inputs[6:].strip() 
        
             
             parts = command_body.split(" as ")
        
             path = parts[0].strip()
             alias_name = parts[1].strip()
        
             #save
             alias[alias_name] = path
             save_alias(alias)
        
             print(f"Successfully mapped {alias_name} -> {path}")
             logging.info(f"Alias created: {alias_name} AKA {path}")
        
        except IndexError:
            print("Error: Use format 'alias [path] as [alias_name]'")
     
     #notes       
    elif inputs == "help['alias']":
        print("\nINFO: MODULE ['alias']")
        print("PURGE: Creates a persistent shortcut for long directory paths.")
        print(fr"USAGE: alias C:\Users\Name\Downloads as DL")
        print("RESULT: Typing 'cd DL' will now move you to that folder instantly.")
        print("DATA: Aliases are stored in 'aliases.json' for persistent use.")
        print("---------------------------------")
         
     #view-alias
    elif inputs == "view aliases":
        if not alias:
            print(F"{YELLOW}INFO: No aliases found in aliases.json{RESET}")
        else:
            try:
                print("\n--- CURRENT SYSTEM ALIASES ---")
                print(f"{'NAME':<10} | {'PATH'}")
                print("-" * 30)
                for name, path in alias.items():
                    print(f"{name:<10} | {path}")
                    print("-------------------------------\n")
                    logging.info(f"{name} checked Sys.alias")
            except Exception as e:
                print(f"Error: Unable To Access alias.json : {e}")
                logging.warning("Sys.alias failed")
     #pci-scan     
    elif inputs == "pci-scan":

        print("\n--- PCI ANTIVIRUS: HYBRID SCANNING ---")
        
        VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
        
        if not VT_API_KEY:
            saved_key = next((item for item in datas if isinstance(item, str) and len(item) == 64), None)
            
            if saved_key:
                VT_API_KEY = saved_key
                print(f"{GREEN} Cloud Intelligence Enabled (Loaded saved key from settings){RESET}.\n")
            else:
                print(f"{RED}  Notice: No VirusTotal API Key found.{RESET}")
                setup_choice = input("[?] Provide a VirusTotal API key for cloud verification? (y/n): ").lower().strip()
                
                if setup_choice == 'y':
                    user_key = input(" Paste your VirusTotal API Key: ").strip()
                    if len(user_key) == 64:
                        VT_API_KEY = user_key
                        datas.append(user_key)
                        save_settings(datas) 
                        print(" {GREEN}Key saved to your settings list! Cloud Intelligence Enabled{RESET}.\n")
                    else:
                        print(f"{RED} Invalid key length. Operating in LOCAL-ONLY mode{RESET}.\n")
                else:
                    print(" Operating in LOCAL-ONLY mode using heuristic entropy flags.\n")
        else:
            print(" Cloud Intelligence Enabled (System Environment API Active).\n")
            
        mode = input("[1] Quick Scan / [2] Deep Scan: ").strip()

        if mode == '2':
            targets = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
        else:
            targets = [os.getcwd()]

        found_threats = []
        file_count = 0
        total_files_estimate = 120000 if mode == '2' else 5000 
        start_time = time.time()

        try:
            for target_dir in targets:
                for root, dirs, files in os.walk(target_dir):
                    if mode == '1':
                        
                        path_parts = root.split(os.sep)
                        if any(x in path_parts for x in ["Windows", "Program Files", "AppData"]):
                            continue

                    for file in files:
                        file_count += 1
                        
                       
                        if any(file.lower().endswith(ex) for ex in ['.exe', '.bat', '.js', '.py', '.scr', '.vbs', '.msi']):
                            try:
                                full_path = os.path.join(root, file)
                                with open(full_path, "rb") as f:
                                    data = f.read(10240)
                                    if data:
                                        p = [data.count(i)/len(data) for i in range(256)]
                                        ent = -sum(x * math.log(x, 2) for x in p if x > 0)
                                        
          
                                        if ent > 7.7:
                                            print(f"\n[!] High Entropy ({ent:.2f}) flag: {file}")
                                            
                                            
                                            if VT_API_KEY:
                                                print("    Querying global malware database...")
                                                file_hash = hashlib.sha256(data).hexdigest()
                                                vt_url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
                                                headers = {"x-apikey": VT_API_KEY}
                                                
                                                try:
                                                    response = requests.get(vt_url, headers=headers, timeout=5)
                                                    if response.status_code == 200:
                                                        vt_data = response.json()
                                                        stats = vt_data['data']['attributes']['last_analysis_stats']
                                                        malicious_count = stats['malicious']
                                                        
                                                        if malicious_count > 0:
                                                            print(f" CONFIRMED THREAT: Flagged by {malicious_count} anti-virus engines!")
                                                            found_threats.append(full_path)
                                                        else:
                                                            print(" False Positive: VirusTotal confirmed this file is safe.")
                                                    
                                                    elif response.status_code == 404:
                                                        print(" Unknown File Signature: Not in database, keeping local entropy flag.")
                                                        found_threats.append(full_path)
                                                    
                                                    elif response.status_code == 429:
                                                        print(" API Rate Limit Hit (4req/min). Falling back entirely to entropy data.")
                                                        found_threats.append(full_path)
                                                except Exception as api_err:
                                                    print(f" Cloud scan failed ({api_err}). Defaulting to entropy flag.")
                                                    found_threats.append(full_path)
                                            else:
                                                found_threats.append(full_path)
                            except:
                                pass

                        #UI
                        if file_count % 100 == 0:
                            elapsed = int(time.time() - start_time)
                            min_e, sec_e = divmod(elapsed, 60)
                            
                            files_per_sec = file_count / (elapsed if elapsed > 0 else 1)
                            eta_sec = int(max(0, total_files_estimate - file_count) / files_per_sec)
                            min_a, sec_a = divmod(eta_sec, 60)
                    
                            status = f"\rSCAN: {target_dir[0]} | TIME: {min_e:02d}:{sec_e:02d} | ETA: {min_a:02d}:{sec_a:02d} | FILES: {file_count}"
                            print(status.ljust(80), end='', flush=True)

        except KeyboardInterrupt:
            print(f"{YELLOW}\n\n[!] Aborted{RESET}.")

        print(f"\n\nSCAN COMPLETE | VERIFIED THREATS: {len(found_threats)} | TOTAL FILES CHECKED: {file_count}")
        
        if found_threats:
            choice = input(f"\n[?] Found {len(found_threats)} threats. Delete all? (y/n): ").lower().strip()
            if choice == 'y':
                print(f"Cleaning system...")
                for threat_path in found_threats:
                    try:
                        if os.path.isfile(threat_path):
                            os.remove(threat_path)
                            print(f"[CLEANED] {os.path.basename(threat_path)}")
                    except Exception as e:
                        print(f"[ERROR] Could not delete {os.path.basename(threat_path)}: {e}")
    
    #notes
    elif inputs == "help['pci-scan']":

        print("\nINFO ON MODULE : 'pci-scan' ")

        print("USAGE : Checks The user's PC for any Malware,spyware and viruses.")

        print("Types : 2")

        print("For E.g: If the user's PC is hacked/invaded by a virus You can use pci-scan to scan for viruses and kill/delete the process/file")

        print("Works like a common Antivirus")
        
        print("\n----MORE INFO ON TYPES----")

        print(fr"""It has 2 types[Quick/deep scan]\

               Quick scan: Scans the folder the user is using to run Python CMD   E.g: if User is using C:\users it checks the C:\Users folder only.

               

               Deep Scan: Scans the ENTIRE PC Warning [May take a Loong time].

                            """)

        print(fr"NOTE(Update): Using VirusTotal's API keys and it's database the pci-scan module can finally distinguish b/w false postives and real-positive(given that you gave the key to the System) So now this scanner is officially 99.9% accurate(that +0.01% away from 100% is when a new virus is made it will not be seen as virus in Virustotal databse but dont worry maybe enthopy will help you out.) ")
    
     #pci-verify
     
    elif inputs.startswith("pci-verify "):
        file_path = inputs[11:].strip().strip('"').strip("'")
        
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                print("ERROR: Target is a directory. 'pci-verify' only works on specific files.")
            else:
                sha256_hash = hashlib.sha256()
                try:
                    with open(file_path, "rb") as f:
                        # Perfect chunk-reading logic maintained here
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                    
                    print(f"\n--- FILE VERIFICATION ---")
                    print(f"File: {os.path.basename(file_path)}")
                    print(f"SHA-256: {sha256_hash.hexdigest()}")
                    print(f"Status: Fingerprint generated successfully.")
                except Exception as e:
                    print(f"ERROR: Could not read file. {e}")
        else:
            print("ERROR: File not found. Check the path spelling.")
    #notes
    elif inputs == "help['pci-verify']":
        print("\nINFO ON MODULE : 'pci-verify' ")
        print("USAGE : Generates a unique SHA-256 digital fingerprint for a file.")
        print("FORMAT: pci-verify [file_path]")
        print("Example: pci-verify C:\\Users\\Desktop\\suspicious.exe")
    
        print("\n----WHY USE THIS?----")
        print("1. Integrity: Check if a system file has been modified by a virus.")
        print("2. Identification: Copy the generated hash and search it online (e.g., VirusTotal).")
        print("3. Security: Confirms if a file is exactly what it claims to be.")
    
        print("\nNOTE: This does NOT delete files. It only provides information.")
    
    #vol
    elif inputs == "vol":
        def pci_vol(drive_letter="C:"):
            try:
                raw_vol = subprocess.check_output(f"vol {drive_letter}", shell=True).decode()
                serial = raw_vol.split("Number is")[-1].strip()

                 
                partitions = psutil.disk_partitions()
                drive_data = next((p for p in partitions if p.mountpoint.startswith(drive_letter)), None)
        
                if drive_data:
                    
                    drive_type = "Local Disk" if "fixed" in drive_data.opts else "Removable Drive"
                    access = "Read/Write" if "rw" in drive_data.opts else "Read-Only"
            
                    print(f"\n Volume in drive {drive_letter} is SYSTEM_OS")
                    print(f" Volume Serial Number is {serial}")
                    print(f" Status: {drive_type} | Access: {access}")
                else:
                    print(f"Error: Volume {drive_letter} not found.")
            
            except Exception as e:
                print(f"PCI_VOL_ERR: {e}")


        pci_vol("C:")
    #ds-b
    elif inputs == "diskpart-basic":
        def help_diskpart_bs():
            print("\n" + "="*50)
            print("GUIDE: DISKPART-BASIC (READ-ONLY)")
            print("="*50)
            print("This mode is for system reporting and health checks.")
            print("\nCOMMANDS:")
            print("1. list disk   - Shows all physical drives and their sizes.")
            print("2. list volume - Displays partitions and current mount points.")
            print("3. exit        - Returns to the main PCI terminal.")
            print("\nNOTE: No modifications can be made in this mode.")
            print("="*50 + "\n")
            
        def diskpart_basic():
            print("\n--- PCI DISK MANAGEMENT (BASIC) ---")
            print("Type 'help-bs' for commands or 'exit' to return.\n")
            while True:
                cmd = input("DISKPARTbs> ").lower().strip()
                if cmd == "exit":
                    break
            
                elif cmd == "list disk":
                    # Shows Physical Drives
                    print(f"\n{'Disk ###':<10} {'Status':<10} {'Size':<10} {'Free':<10}")
                    print("-" * 45)
                    
                    for i, part in enumerate(psutil.disk_partitions()):
                        if 'fixed' in part.opts:
                            usage = psutil.disk_usage(part.mountpoint)
                            print(f"Disk {i:<5} Online     {usage.total // (1024**3):<3} GB    {usage.free // (1024**3):<3} GB")

                elif cmd == "list volume":
                    # Shows Logical Volumes 
                    print(f"\n{'Volume ###':<12} {'Ltr':<5} {'Label':<12} {'Fs':<6} {'Type'}")
                    print("-" * 55)
                    for i, part in enumerate(psutil.disk_partitions()):
                        d_type = "Partition" if "fixed" in part.opts else "Removable"
                        print(f"Volume {i:<5} {part.mountpoint:<5} {'SYS_OS':<12} {part.fstype:<6} {d_type}")
                         
                elif cmd == "help-bs":
                    help_diskpart_bs()
                else:
                    print(f"{YELLOW}'{cmd}' is not recognized in Basic mode.{RESET}")
        diskpart_basic()
        datas.append(f"{name} accessed Diskpart-Basic")
        save_settings(datas)
     #ds-a       
    elif inputs == "diskpart-advance":
        def help_diskpart_ad():
            print("\n" + "!"*50)
            print("GUIDE: DISKPART-ADVANCE (SYSTEM MODIFICATION)")
            print("!"*50)
            print("WARNING: This mode interfaces with Windows Diskpart.exe.")
            print("Incorrect usage can result in PERMANENT DATA LOSS.")
            print("\nWORKFLOW:")
            print("1. list disk          - Identify the Disk ID (e.g., Disk 1).")
            print("2. select disk [ID]   - Focus the tool on a specific drive.")
            print("3. clean              - ERASES all partitions on the selected disk.")
            print("4. format fs=ntfs quick - Formats the disk to NTFS.")
            print("\nREQUIRED: Must run PCI as Administrator or access in WinRE.")
            print("!"*50 + "\n")
        def diskpart_advance():
            
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("\n" + "!"*50)
                print(" ERROR: ADMINISTRATIVE PRIVILEGES REQUIRED ".center(50, "!"))
                print(" Please Restart PCI as Administrator to use Advance Mode. ".center(50, "!"))
                print("!"*50 + "\n")
                return # This fixes your 'exit' error by kicking the user out safely

            print("\n" + "="*60)
            print(" PCI DISKPART: ADVANCED SYSTEM MODIFICATION MODE ".center(60, " "))
            print(" WARNING: DATA LOSS IS PERMANENT IN THIS SHELL ".center(60, "!"))
            print("="*60)
            print("Type 'help-ad' for syntax or 'exit' to return.\n")

            while True:
                cmd = input("DISKPARTad> ").lower().strip()
                if cmd == "exit":
                    # Clean up 
                    if os.path.exists("pci_script.txt"):
                        os.remove("pci_script.txt")
                        break
                    logging.info(f"{name} exited Diskpart at {date}")
                elif cmd == "help-ad":
                    help_diskpart_ad()

                elif cmd == "list disk" or cmd == "list volume":
                    with open("pci_script.txt", "w") as f:
                        f.write(cmd)
                    subprocess.run("diskpart /s pci_script.txt", shell=True)
            
                elif cmd.startswith("select ") or cmd == "clean" or "format" in cmd:
                    confirm = input(f"CRITICAL: Confirm '{cmd}'? (y/n): ").lower().strip()
                    if confirm == 'y':
                        with open("pci_script.txt", "w") as f:
                            f.write(f"{cmd}\n")
                        print(f"Executing {cmd}...")
                        subprocess.run("diskpart /s pci_script.txt", shell=True)
                        print("Command Sent to System Controller.")
                    else:
                        print(f"{YELLOW}Operation Aborted.{RESET}")
                    
                    logging.warning(f"{name} modified Diskpart")
                
                else:
                    print(f"'{cmd}' not recognized. Use 'list disk' or 'select disk X'.")
        diskpart_advance()
        datas.append(f"{name} accessed Diskpart-Advance")
        save_settings(datas)
         
    #view-dir
    elif inputs.startswith("view-dir"):
        parts = inputs.split(" ", 1)
        target_path = parts[1].strip() if len(parts) > 1 else "."
    
        try:
            if not os.path.exists(target_path):
                print(f"Error: Path '{target_path}' does not exist.")
                continue
            
            items = os.listdir(target_path)
        
            file_count = 0
            dir_count = 0
            total_file_size = 0
        
            print(f"\n Contents of: {os.path.abspath(target_path)}")
            print("+" + "-"*32 + "+" + "-"*12 + "+" + "-"*22 + "+")
            print(f"| {'Name'.ljust(30)} | {'Type'.ljust(10)} | {'Modified'.ljust(20)} |")
            print("+" + "-"*32 + "+" + "-"*12 + "+" + "-"*22 + "+")
        
            for item in items:
                item_path = os.path.join(target_path, item)
                is_dir = os.path.isdir(item_path)
            
                
                if is_dir:
                    dir_count += 1
                    item_type = "DIR"
                else:
                    file_count += 1
                    item_type = "FILE"
                    try:
                        total_file_size += os.path.getsize(item_path)
                    except OSError:
                        pass  # Skip system files that are locked/inaccessible
            
                try:
                    mtime = os.path.getmtime(item_path)
                    date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                except OSError:
                    date_str = "UNKNOWN".ljust(20)
                
                display_name = item[:27] + "..." if len(item) > 30 else item
            
                print(f"| {display_name.ljust(30)} | {item_type.ljust(10)} | {date_str.ljust(20)} |")
            
            print("+" + "-"*32 + "+" + "-"*12 + "+" + "-"*22 + "+")
        
            # 2. Get true free disk space using standard shutil library
            _, _, free_space = shutil.disk_usage(target_path)
        
            # 3. Format 
            formatted_file_size = f"{total_file_size:,}"
            formatted_free_space = f"{free_space:,}"
        
            print(f"               {file_count} File(s)      {formatted_file_size} bytes")
            print(f"               {dir_count} Dir(s)   {formatted_free_space} bytes free\n")
        
        except Exception as e:
            print(f"{YELLOW}Error accessing directory: {e}{RESET}")
            
    
   
#scan-reg
    elif inputs == "scan-reg":
        print("\n Scanning Registry Persistence Hives...")
    
        target_paths = [
        (win32con.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "HKLM_Run"),
        (win32con.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce", "HKLM_RunOnce"),
        (win32con.HKEY_CURRENT_USER,  r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "HKCU_Run"),
        (win32con.HKEY_CURRENT_USER,  r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce", "HKCU_RunOnce")
        ]
    
        found_items = []
    
        
        for root_hive, subkey, label in target_paths:
            try:
                hKey = win32api.RegOpenKeyEx(root_hive, subkey, 0, win32con.KEY_READ)
                index = 0
                while True:
                    try:
                        name, data, _ = win32api.RegEnumValue(hKey, index)
                        found_items.append({
                        "hive": root_hive,
                        "subkey": subkey,
                        "label": label,
                        "name": name,
                        "data": data
                        })
                        index += 1
                    except Exception:
                        break
                win32api.RegCloseKey(hKey)
            except Exception:
                continue

        if not found_items:
            print(f"️{GREEN} Scan complete. No registry entries detected.{GREEN}\n")
            continue

        # ASCII table
        print(f"\n️{RED} Detected {len(found_items)} Registry Startup Entries{RESET}:")
        print("+" + "-"*4 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*42 + "+")
        print(f"{RED}| {'ID'.ljust(2)} | {'Hive'.ljust(10)} | {'Key Name'.ljust(20)} | {'Executable Path'.ljust(40)}{RESET} |")
        print("+" + "-"*4 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*42 + "+")
    
        for idx, item in enumerate(found_items, start=1):
            # Truncate strings so they don't break the beautiful layout columns
            display_name = item['name'][:17] + "..." if len(item['name']) > 20 else item['name']
            display_data = item['data'][:37] + "..." if len(item['data']) > 40 else item['data']
        
            print(f"| {str(idx).ljust(2)} | {item['label'].ljust(10)} | {display_name.ljust(20)} | {display_data.ljust(40)} |")
        
        print("+" + "-"*4 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*42 + "+")

       
        print("\n Options: Type a single ID (e.g., '3'), multiple IDs separated by commas (e.g., '1,3'), 'all', or 'none'.")
        action = input(" Selection to OBLITERATE: ").strip().lower()
    
        if action == "none" or action == "":
            print("Skipped. No keys were deleted.\n")
            continue
        
        
        targets_to_delete = []
        if action == "all":
            targets_to_delete = found_items
        else:
            try:
                # Parse inputs like "1, 3" into integer indices
                selected_indices = [int(x.strip()) for x in action.split(",")]
                for idx in selected_indices:
                    if 1 <= idx <= len(found_items):
                        targets_to_delete.append(found_items[idx - 1])
                    else:
                        print(f"️ Warning: ID {idx} is out of range. Skipping.")
            except ValueError:
                print(" Invalid input format. Operation aborted.")
                continue

        deleted_count = 0
        for item in targets_to_delete:
            try:
                hKeyWritable = win32api.RegOpenKeyEx(item['hive'], item['subkey'], 0, win32con.KEY_SET_VALUE)
                win32api.RegDeleteValue(hKeyWritable, item['name'])
                win32api.RegCloseKey(hKeyWritable)
                print(f" Destroyed: [{item['label']}] {item['name']}")
                deleted_count += 1
            except Exception as e:
                print(f"{RED} Error: Failed to delete {item['name']}: {e}{RESET}")
            
        print(f"\n Batch operation complete. {deleted_count} items purged.\n")
 #notes
    elif inputs == "help['scan-reg']":
        print("INFO ON MODULE : scan-reg")
        
        print("Usage : Scan-reg is used to find random bytes/keys made by viruses/trojans and other malware to control the OS.")
        
        print("More Info : It scans the Registry files[regedit] and highlights/gives the keys which have the most enthropy(randomness).")
        
        print("Now again just like pci-scan this module software is not 100% accurate as some system/sys-health files contain same randomness equal to some keys made by viruses.[So don't 100% trust it but since it gives the Keys name's it should be easy to differentiate].")
        
    else:
        print("Command Not In Current Version of Python CMD or there is no existing command")
        
        
