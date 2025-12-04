from dotenv import load_dotenv
import os

load_dotenv()  # 讀取 .env 檔案

api_key = os.getenv("OPENAI_API_KEY")
app_name = os.getenv("APP_NAME")

print(api_key)
print(app_name)
