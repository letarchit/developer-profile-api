from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    age: int
    experience: int

