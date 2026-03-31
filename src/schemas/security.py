from pydantic import BaseModel

class LoginSecurity(BaseModel):
    username: str
    password: str