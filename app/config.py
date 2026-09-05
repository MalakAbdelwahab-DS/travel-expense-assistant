import os
from dotenv import load_dotenv

load_dotenv()

# Model configuration
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")  
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "anthropic")
MODEL_NAME = os.getenv("MODEL_NAME", "anthropic:claude-sonnet-4-6")
MODEL_TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", "0"))

# Data path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #project root
TRAVEL_EXPENSE_POLICY_DATA_PATH = os.path.join(BASE_DIR, "data", "travel_expense_policy.csv")

