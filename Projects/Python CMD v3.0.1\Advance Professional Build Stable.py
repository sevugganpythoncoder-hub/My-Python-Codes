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
import string
import math
import hashlib
import ctypes

# Starting
print("""NOTE : ------------------------------------------------------------------
PYTHON COMMAND INTERFACE (PCI) | v3.0.0 FINAL STABLE BUILD
Status: Completed
------------------------------------------------------------------
NOTE: This tool is optimized for System Recovery and Management. 
All core features (Process Kill, Disk List, Sys-Health) are active.
This CMD will no longer recieve Updates(This is False).
------------------------------------------------------------------
     """)

print("\nFor best of use make sure to install some of the libraries.[Ignore If not using a raw .py file]")

py = platform.python_version()
date = datetime.datetime.now()
print(fr"""
Python CMD Copyright Access [V.3.0.0/v Advance Standalone Stable] [Future updates?]
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
            if path in alias:
                    path = alias[path]
                    print(f"Redirecting via alias to: {path}")
                    logging.info(f"{name} used alias : {path}")
            
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
        
        print("\n--- ADVANCED FEATURES ---")
        print("21)   -  system restore                   -  Creates a backup of the current folder")
        print("                                          -  Note: For more info type help['system restore']")
        print("22)   -  alias [path] as [name]           -  Creates a custom shortcut to a path")
        print("                                          -  Note: For more info type help['alias']")
        print("23)   -  view aliases                     -  Shows all shortcuts created by you")
        
        print("\n--- DISK MANAGEMENT (NEW) ---")
        print("24)   -  diskpart-basic                   -  Safe, Read-Only disk monitoring")
        print("25)   -  diskpart-advance                 -  Write-Access (Clean/Format) - ADMIN REQ.")
        
        print("\n--- SECURITY (PCI SUITE) ---")
        print("26)   -  pci-scan                         -  Scans files for malware/viruses")
        print("27)   -  pci-verify [file]                -  Verifies if malicious files are system-critical")
        print("--------------------------------------------------------------------------------------------------")
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
        print("Status         : V.3.0.0 Advance Professional Build Stable(Completed?)")
        print("---------------------------")
        print("""Special thanks to the PSF for the core engine
         Also to my friends and People for helping me with this endeavour and I Hope This project Helps Everybody
         Thank You.
        """)
        datas.append("Viewed Credits")
        save_settings(datas)
        
    elif inputs.startswith("pykill "):
        proc_name = inputs[7:].strip()  # Added .strip() to clean up spaces
        found = False
        
        # 1. Define the critical system blacklist
        blacklist = ["svchost.exe", "lsass.exe", "wininit.exe", "services.exe", "csrss.exe", "explorer.exe"]
        
        print(fr"Searching for processes Matching name {proc_name}...")
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                # Basic check to see if the process name exists safely
                if proc.info["name"] and proc_name.lower() in proc.info["name"].lower():
                    current_proc_name = proc.info["name"].lower()
                    
                    # 2. Check if the found process is in your blacklist
                    if current_proc_name in blacklist:
                        print("\n" + "!"*60)
                        print(f" WARNING: {proc.info['name']} (PID: {proc.info['pid']}) is a CRITICAL SYSTEM PROCESS! ".center(60, "="))
                        print(" Terminating this could cause a Blue/black Screen of Death (BSOD). ".center(60, "="))
                        print("!"*60)
                        
                        # Ask for confirmation (Soft Block)
                        confirm = input(f"Are you absolutely sure you want to kill {proc.info['name']}? (y/N): ").lower().strip()
                        if confirm != 'y':
                            print(f"Skipped: Termination of {proc.info['name']} aborted by user.\n")
                            continue  # Skips this process and moves to the next one in the loop
                    
                    # 3. Execution Phase (Runs if not blacklisted OR if user typed 'y')
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
            print(f"No Process named {proc_name} or process is unkillable/banned by user.")
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
        except Exception as e:
            print("ERROR: System Restore Call Not accepted/Failed")
            logging.warning(f"SYSTEM RESTORE FAILURE")
    elif inputs == "help['systemrestore']":
        print("INFO : Module ['Systemrestore']")
        
        print("USE : Creates a Carbon Copy of the folder the user is using to run pythoncmd. ")
        
        print(fr"For E.g: if the user runs the CMD in C:\users\[yourname]\[dirpath] it will create a copy of that folder")
        
        print(f"\n NOTE: This Command is for Educational/Emergency Purposes only. This command although Enforced with safety features Can drain your system Space Very quickly as well as Potentially Damage the system.")
        
        print("Use the command When needed and Wisely.You have been Warned.")
        
    elif inputs.startswith("alias"):
        try:
            parts = inputs.split(" as ")
            path = parts[1]
            name = parts[3]
            alias[name] = path
            save_alias(alias)
            print(f"Successfully mapped {name} -> {path}")
            logging.info(f"{name} made an alias : {name} AKA {path}")
        except IndexError:
            print("Error: Use format 'alias [path] as [name]'")
            
    elif inputs == "help['alias']":
        print("\nINFO: MODULE ['alias']")
        print("PURGE: Creates a persistent shortcut for long directory paths.")
        print(fr"USAGE: alias C:\Users\Name\Downloads as DL")
        print("RESULT: Typing 'cd DL' will now move you to that folder instantly.")
        print("DATA: Aliases are stored in 'aliases.json' for persistent use.")
        print("---------------------------------")
        
    elif inputs == "view aliases":
        if not alias:
            print("INFO: No aliases found in aliases.json")
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
                
    elif inputs == "pci-scan":
        print("\n--- PCI ANTIVIRUS: SCANNING ---")
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
                    if mode == '1' and target_dir not in root:
                        if any(x in root for x in ["Windows", "Program Files", "AppData"]):
                            continue

                    for file in files:
                        file_count += 1
                        
                        # 1. SCAN LOGIC
                        if any(file.lower().endswith(ex) for ex in ['.exe', '.bat', '.js', '.py']):
                            try:
                                full_path = os.path.join(root, file)
                                with open(full_path, "rb") as f:
                                    data = f.read(10240)
                                    if data:
                                        p = [data.count(i)/len(data) for i in range(256)]
                                        ent = -sum(x * math.log(x, 2) for x in p if x > 0)
                                        if ent > 7.7:
                                            found_threats.append(file)
                                            # Print threat on a new line so it stays in history
                                            print(f"\n[!] THREAT: {file}")
                            except: pass

                        # 2. THE SINGLE-LINE UI (STRICT FIX)
                        if file_count % 100 == 0:
                            elapsed = int(time.time() - start_time)
                            min_e, sec_e = divmod(elapsed, 60)
                            
                            files_per_sec = file_count / (elapsed if elapsed > 0 else 1)
                            eta_sec = int(max(0, total_files_estimate - file_count) / files_per_sec)
                            min_a, sec_a = divmod(eta_sec, 60)
                    
                            # We use end='' and \r at the START to force overwriting
                            status = f"\rSCAN: {target_dir[0]} | TIME: {min_e:02d}:{sec_e:02d} | ETA: {min_a:02d}:{sec_a:02d} | FILES: {file_count}"
                            
                            # ljust adds spaces to the end to "clear" any leftover long text
                            print(status.ljust(80), end='', flush=True)

        except KeyboardInterrupt:
            print("\n\n[!] Aborted.")

        print(f"\n\nSCAN COMPLETE | THREATS: {len(found_threats)} | TOTAL: {file_count}")
        
        if found_threats:
            choice = input(f"\n[?] Found {len(found_threats)} threats. Delete all? (y/n): ").lower().strip()
            if choice == 'y':
                print(f"Cleaning system...")
                for threat_path in found_threats:
                    try:
                        if os.path.isfile(threat_path):
                            os.remove(threat_path)
                            print(f"[CLEANED] {threat_path}")
                        elif os.path.isdir(threat_path):
                            shutil.rmtree(threat_path)
                            print(f"[REMOVED] {threat_path}")
                    except Exception as e:
                        print(f"[ERROR] Could not delete {threat_path}: {e}")
                
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

        print(fr"NOTE: This Anti-virus scanner is only 85-90% accurate due to technical difficulties[Idk how to make it 100%] Such as targetting Existant Anti\-virus software files as they are encrypted and have a high Entropy Number.So use this In case of emergencies and Use wisely[AGAIN DO NOT TRUST 100% This could [if you have admin privilges] destroy your PC beyond repair].")
    
    elif inputs.startswith("pci-verify "):
        # Use .strip() with arguments to clear any accidental drag-and-drop quotes
        file_path = inputs[11:].strip().strip('"').strip("'")
        
        if os.path.exists(file_path):
            # NEW CHECK: Prevent directory crashes using os.path.isdir
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
    
    
    elif inputs == "vol":
        def pci_vol(drive_letter="C:"):
            try:
                # 1. Get the Serial Number using a background system call
                # We filter the output of the Windows 'vol' command
                raw_vol = subprocess.check_output(f"vol {drive_letter}", shell=True).decode()
                serial = raw_vol.split("Number is")[-1].strip()

                # 2. Get the Drive Type and Status using psutil
                partitions = psutil.disk_partitions()
                drive_data = next((p for p in partitions if p.mountpoint.startswith(drive_letter)), None)
        
                if drive_data:
                    # Human-readable translation
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
                    # Shows Physical Drives (Using psutil.disk_usage logic)
                    print(f"\n{'Disk ###':<10} {'Status':<10} {'Size':<10} {'Free':<10}")
                    print("-" * 45)
                    # We treat the root of partitions as the 'disks' for basic mode
                    for i, part in enumerate(psutil.disk_partitions()):
                        if 'fixed' in part.opts:
                            usage = psutil.disk_usage(part.mountpoint)
                            print(f"Disk {i:<5} Online     {usage.total // (1024**3):<3} GB    {usage.free // (1024**3):<3} GB")

                elif cmd == "list volume":
                    # Shows Logical Volumes (Drive Letters and File Systems)
                    print(f"\n{'Volume ###':<12} {'Ltr':<5} {'Label':<12} {'Fs':<6} {'Type'}")
                    print("-" * 55)
                    for i, part in enumerate(psutil.disk_partitions()):
                        d_type = "Partition" if "fixed" in part.opts else "Removable"
                        print(f"Volume {i:<5} {part.mountpoint:<5} {'SYS_OS':<12} {part.fstype:<6} {d_type}")
                elif cmd == "help-bs":
                    help_diskpart_bs()
                else:
                    print(f"'{cmd}' is not recognized in Basic mode.")
        diskpart_basic()
        datas.append(f"{name} accessed Diskpart-Basic")
        save_settings(datas)
                    
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
            # 1. Check for Admin immediately
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
                    # Clean up any leftover temp scripts before leaving
                    if os.path.exists("pci_script.txt"):
                        os.remove("pci_script.txt")
                        break
                    logging.info(f"{name} exited Diskpart at {date}")
                elif cmd == "help-ad":
                    help_diskpart_ad()

                elif cmd == "list disk" or cmd == "list volume":
                    # We use /s to run a one-line script so the window stays open long enough to read
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
                        print("Operation Aborted.")
                    
                    logging.warning(f"{name} modified Diskpart")
                
                    # We use capture_output=False so you can see the real Diskpart success message
                else:
                    print(f"'{cmd}' not recognized. Use 'list disk' or 'select disk X'.")
        diskpart_advance()
        datas.append(f"{name} accessed Diskpart-Advance")
        save_settings(datas)
            
        
    else:
        print("Command Not In Current Version of Python CMD or there is no existing command")
        
        
