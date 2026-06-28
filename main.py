from fastapi import FastAPI
from models import Profile
from services import (
    create_profile,
    get_profiles,
    get_profile,
    update_profile,
    delete_profile
)

app = FastAPI()

@app.post('/profiles')
def create(profile: Profile):
    return create_profile(profile)

@app.get('/profiles')
def get_all():
    return get_profiles()

@app.get('/profiles/{profile_id}')
def get_one(profile_id: str):
    return get_profile(profile_id)

@app.put('/profiles/{profile_id}')
def update(profile_id: str, profile: Profile):
    return update_profile(profile_id, profile)

@app.delete('/profiles/{profile_id}')
def delete(profile_id: str):
    return delete_profile(profile_id)