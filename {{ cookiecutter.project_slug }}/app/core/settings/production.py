from typing import List
from .base import BaseAppSettings

class Settings(BaseAppSettings):
    origins: List[str] = []