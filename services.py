from models import Profile
from storage import load_profiles, save_profiles
from fastapi import HTTPException

import uuid

# create POST /profile

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

def get_profiles():
     return load_profiles()

# GET /profile{:id}

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

def update_profile(profile_id: str, profile: Profile):
     new_profile_data = profile.model_dump()
     profiles = load_profiles()

     for index, profile in enumerate(profiles):
          if profile['id'] == profile_id:
            new_profile_data["id"] = profile_id
            profiles[index] = new_profile_data
            save_profiles(profiles)
            return {
                "message": "profile updated successfully",
            }
     raise HTTPException(
            status_code=404,
            detail='Profiles not found'
        ) 

def delete_profile(profile_id: str):
    profiles = load_profiles()
    for index, profile in enumerate(profiles):
         if profile["id"] == profile_id:
            del profiles[index]
            save_profiles(profiles)
            return {
                 "message": "profile deleted successfully",
            }
    raise HTTPException(
         status_code=404,
         detail="profile not found"
    )
                