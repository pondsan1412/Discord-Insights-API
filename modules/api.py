from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

API_TOKEN = os.getenv("API_TOKEN", "your_secret_token")
last_message_data = {
    "LastMessage": "",
    "datetime": "",
    "profilepicture": "",
    "message_id": "",
    "message_content": "",
    "is_admin": False,
    "server_id": "",
    "server_name": "",
    "server_profile_picture": "",
    "attachments": [],
    "author_name": ""
}  # Variable to store the latest message data

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

    # Store the latest message data
    last_message_data = data
    # Emit data to WebSocket clients
    socketio.emit('new_message', data)
    print("Sent data to WebSocket clients:", data)

    return jsonify({"status": "success", "message": "Data received"}), 200

@app.route('/api/last_message', methods=['GET'])
def get_last_message():
    if not last_message_data or last_message_data.get("LastMessage") == "":
        return jsonify({"status": "failed", "message": "No message data available"}), 404

    # Send the latest data that was POSTed
    return jsonify(last_message_data), 200

if __name__ == "__main__":
    socketio.run(app, port=5000)
