import os
from dotenv import load_dotenv

load_dotenv()

# Monday.com
MONDAY_API_TOKEN = os.getenv("MONDAY_API_TOKEN")
DEALS_BOARD_ID = int(os.getenv("DEALS_BOARD_ID"))
WORK_ORDERS_BOARD_ID = int(os.getenv("WORK_ORDERS_BOARD_ID"))

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Monday GraphQL Endpoint
MONDAY_API_URL = "https://api.monday.com/v2"

# Application
APP_NAME = "Skylark Monday BI Agent"