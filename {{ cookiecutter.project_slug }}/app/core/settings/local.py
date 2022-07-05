from typing import List
from .base import BaseAppSettings

class Settings(BaseAppSettings):
    origings: List[str] = ["0.0.0.0", "localhost", "127.0.0.1"]