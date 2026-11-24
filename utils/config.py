import os
from pathlib import Path
from dotenv import load_dotenv

#locate project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#Load environment veriables
load_dotenv(PROJECT_ROOT / ".env")

#Application configuration
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL is mission in .env")