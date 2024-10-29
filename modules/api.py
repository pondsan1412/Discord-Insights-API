from flask import Flask, request, jsonify
import os

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN", "your_secret_token")
last_message_data = None  # ตัวแปรสำหรับเก็บข้อมูลข้อความล่าสุด

@app.route('/api/last_message', methods=['POST'])
def last_message():
    global last_message_data
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"status": "failed", "message": "Missing or invalid Authorization header"}), 401

    token = auth_header.split(" ")[1]
    if token != API_TOKEN:
        return jsonify({"status": "failed", "message": "Invalid token"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"status": "failed", "message": "No data received"}), 400

    # เก็บข้อมูลข้อความล่าสุดในตัวแปร last_message_data
    last_message_data = data
    print("Received data:", data)

    return jsonify({"status": "success", "message": "Data received"}), 200

# เพิ่ม GET Method สำหรับการดึงข้อมูลล่าสุด
@app.route('/api/last_message', methods=['GET'])
def get_last_message():
    if last_message_data is None:
        return jsonify({"status": "failed", "message": "No message data available"}), 404

    # ส่งข้อมูลล่าสุดที่ถูก POST มาให้ผู้ใช้
    return jsonify(last_message_data), 200

if __name__ == "__main__":
    app.run(port=5000, debug=False)
