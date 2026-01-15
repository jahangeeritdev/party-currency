import os
from dotenv import load_dotenv

load_dotenv()  # loads .env

print("API KEY:", os.getenv("MONIFY_API_KEY"))
print("SECRET KEY:", os.getenv("MONIFY_SECRET_KEY"))
print("CONTRACT CODE:", os.getenv("MONIFY_CONTRACT_CODE"))
print("BASE URL:", os.getenv("MONIFY_BASE_URL"))
