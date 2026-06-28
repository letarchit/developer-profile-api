import json

PROFILE_FILE = "profiles.json"

def load_profiles():
    try:
        with open(PROFILE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return []
    except json.JSONDecodeError:
            return []

def save_profiles(profiles):
     with open(PROFILE_FILE, 'w') as file:
          json.dump(profiles, file, indent = 4)
