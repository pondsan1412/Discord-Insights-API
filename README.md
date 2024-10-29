
# Discord Bot with Flask API Integration

## Overview
This project integrates a **Discord Bot** with a **Flask API** to track messages in Discord channels. When a new message is posted in a Discord server that the bot has access to, the message content, along with metadata such as user profile picture, server information, and attachments, is sent to an endpoint exposed by the Flask server.

The integration aims to make it easy to log and interact with incoming messages through an external service, allowing for custom responses, data processing, or any further handling by the Flask backend.

[![Webhook Usage on Discord](https://img.youtube.com/vi/nVQ-baDmoTg/0.jpg)](https://www.youtube.com/watch?v=nVQ-baDmoTg)

## Features
- **Message Tracking and Replying**: The Discord bot listens for messages in the server and takes the following actions:
  - Replies to specific keywords (e.g., "helloworld", "ขอบคุณ", etc.).
  - Captures metadata of every message, including:
    - Author profile picture.
    - Message ID.
    - Whether the user is an admin.
    - Server details (name, ID, and server profile picture).
    - Attachments (files, images, etc.).
  - Sends the captured data to a Flask server via a POST request.

- **WebSocket Support**: Real-time data emission to WebSocket clients when a new message is posted.

## Prerequisites
- Python 3.x
- Discord bot token
- Flask and Flask-SocketIO
- A `.env` file to store the bot token securely
- Required Python packages listed in `requirements.txt`

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:
   - Create a `.env` file in the root directory and add the following:
     ```env
     TOKEN=your_discord_bot_token_here
     API_TOKEN=your_api_secret_token_here
     ```

## Usage
This project consists of two main components:
1. **Discord Bot (`client.py`)** - The bot that listens to messages and sends data to the Flask server.
2. **Flask Server (`modules/api.py`)** - Receives data from the Discord bot and provides endpoints to view the messages.

The project uses the script **`start.py`** to run both the bot and the Flask server simultaneously.

### Running the Project
Run the project by executing the following command:
```bash
python start.py
```
This command will:
- Start the Flask server to handle incoming POST requests at `http://localhost:5000/api/last_message`.
- Start the Discord bot and connect it to your server.

## Endpoint Details
- **`/api/last_message` [POST]**: Receives the latest message details from the Discord bot.
  - Data sent includes message content, message ID, profile picture of the author, server info, and any attachments.
  - Emits real-time data to WebSocket clients via `new_message` event.
- **`/api/last_message` [GET]**: Returns the latest captured message details.

## Example Data Sent
Here is an example of the data sent by the Discord bot to the Flask API:
```json
{
  "LastMessage": "ทดสอบส่งข้อความ สวัสดีครับ ภาษาไทย UTF-8 TEST TEST",
  "datetime": "2024-10-29 14:07:31.428000+00:00",
  "is_admin": true,
  "message_content": "ทดสอบส่งข้อความ สวัสดีครับ ภาษาไทย UTF-8 TEST TEST",
  "message_id": "1300823335986397184",
  "profilepicture": "https://cdn.discordapp.com/avatars/324207503816654859/30fbc21ee0046eca166cec456d871818.png?size=1024",
  "server_id": "1250837063394267156",
  "server_name": "สมาชิกชมรมคนชอบผี",
  "server_profile_picture": "https://cdn.discordapp.com/icons/1250837063394267156/95c15ddb8f9f8476d23a10671db45793.png?size=1024",
  "attachments": [
    {
      "filename": "example.png",
      "url": "https://cdn.discordapp.com/attachments/1250837063394267156/324207503816654859/example.png",
      "content_type": "image/png",
      "size": 123456
    }
  ]
}
```

## Configuration
- **config.json**: Stores bot-specific settings like the author owner's ID.
- **respond-text.json**: Stores responses for keywords, e.g., "ขอบคุณ".

## Notes
- **Authorization**: The bot includes an API Token for secure communication with the Flask server.
- **Development Server**: The Flask server runs in development mode. For production deployment, a production WSGI server like **gunicorn** is recommended.

## Troubleshooting
- **Bot not responding**: Ensure your Discord token is correctly set in the `.env` file and that your bot has the required permissions.
- **Flask server not receiving data**: Check the `API_TOKEN` in `.env` matches the one expected by the Flask server.
- **Port Conflicts**: The default port for Flask is `5000`. If another application is using this port, change the port number in `modules/api.py`.

## Contributing
Feel free to open an issue or submit a pull request if you have suggestions for improving the project.

## License
This project is licensed under the MIT License.

---


