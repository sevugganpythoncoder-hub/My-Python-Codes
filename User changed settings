import json
import os

# 1. Define the filename where the "Vault" lives
SETTINGS_FILE = "user_settings.json"

# 2. Default settings (The "Factory Reset" state)
default_settings = {
    "theme": "dark",
    "font_size": 14,
    "notifications": True,
    "user_level": "Senior-Slayer"(demon slayer reference ifykyk)
}

def load_settings():
    """Load settings from the JSON file or return defaults if file doesn't exist."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)
    return default_settings

def save_settings(settings):
    """Write the current settings dictionary to the JSON file."""
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)
    print("\n[SYSTEM] Settings saved to the Vault successfully!")

def update_settings(current_settings):
    """Interactive menu to change user preferences."""
    print("\n--- ARCHITECT SETTINGS MENU ---")
    print(f"1. Theme (Current: {current_settings['theme']})")
    print(f"2. Font Size (Current: {current_settings['font_size']})")
    print(f"3. Notifications (Current: {'ON' if current_settings['notifications'] else 'OFF'})")
    print("4. Save and Exit")
    
    choice = input("\nSelect an option to modify: ")
    
    if choice == "1":
        new_theme = input("Enter theme (light/dark): ").lower()
        current_settings["theme"] = new_theme
    elif choice == "2":
        try:
            new_size = int(input("Enter font size (10-30): "))
            current_settings["font_size"] = new_size
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "3":
        current_settings["notifications"] = not current_settings["notifications"]
        print(f"Notifications toggled to: {current_settings['notifications']}")
    elif choice == "4":
        save_settings(current_settings)
        return False # This breaks the loop
    
    return True # Keep the menu running

# --- MAIN EXECUTION ---
user_prefs = load_settings()
print(f"Welcome back, Architect. Current Theme: {user_prefs['theme']}")

running = True
while running:
    running = update_settings(user_prefs)

print("System Offline. Ready for Day 19.")
