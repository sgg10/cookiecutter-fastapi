
from uuid import UUID
from typing import Optional
from datetime import date

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import validator

class User(BaseModel):
    username: str = Field(...)