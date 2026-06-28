import uuid
import json

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

class Profile(BaseModel):
    name: str
    age: int
    experience: int

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

# create POST /profile

@app.post('/profiles')
def create_profile(profile: Profile):
    profile_data = profile.model_dump()
    profiles = load_profiles()
    profile_data["id"] = str(uuid.uuid4())
    profiles.append(profile_data)
    save_profiles(profiles)
    return {
        "message": "Profile created",
        "profile": profile_data
    }

# GET /profiles

@app.get('/profiles')
def get_profiles():
     return load_profiles()

# GET /profile{:id}
@app.get('/profiles/{profile_id}')
def get_profile(profile_id: str):
    profiles = load_profiles()
    for profile in profiles:
        if profile["id"] == profile_id:
             return profile
    raise HTTPException(
         status_code=404,
         details='Profile not found'
    )

# PUT /profiles/{profile_id}

# client should be able to exist the existing fields

@app.put('/profiles/{profile_id}')
def update_profile(profile_id: str, profile: Profile):
     newProfileData = profile.model_dump()
     profiles = load_profiles()

     for index, profile in enumerate(profiles):
          if profile['id'] == profile_id:
            newProfileData["id"] = profile_id
            profiles[index] = newProfileData
            save_profiles(profiles)
            return {
                "message": "profile updated successfully",
                "profiles data": profiles
            }
     raise HTTPException(
            status_code=404,
            detail='Profile not found'
        ) 

@app.delete('/profiles/{profile_id}')
def delete_profile(profile_id: str):
    profiles = load_profiles()
    for index, profile in enumerate(profiles):
         if profile["id"] == profile_id:
            del profiles[index]
            save_profiles(profiles)
            return {
                 "message": "profile deleted successfully",
                 "profiles data": profiles
            }
    raise HTTPException(
         status_code=404,
         detail="profile not found"
    )
                