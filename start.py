import os
from dotenv import load_dotenv
import subprocess
import time
import requests

load_dotenv()

def run_flask():
    subprocess.Popen(["python", "modules/api.py"])

def run_bot():
    subprocess.Popen(["python", "client.py"])

def test_flask_server():
    time.sleep(5)  # รอให้ Flask server เริ่มต้นทำงานก่อน
    try:
        response = requests.get("http://localhost:5000/api/last_message")
        if response.status_code == 200:
            print("Flask server is running and accessible")
        else:
            print(f"Failed to connect to Flask server. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to Flask server: {e}")

if __name__ == "__main__":
    # เปิด Flask Server และ Discord Bot แยกกันในสอง process
    run_flask()
    test_flask_server()  # ทดสอบว่า Flask Server พร้อมแล้ว
    run_bot()
