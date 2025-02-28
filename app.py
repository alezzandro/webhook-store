from flask import Flask, request, jsonify
import json
import os
import uuid
from datetime import datetime

app = Flask(__name__)

# Directory to store the JSON files
WEBHOOK_DIR = "/tmp/webhooks"

# Create the directory if it doesn't exist
if not os.path.exists(WEBHOOK_DIR):
    os.makedirs(WEBHOOK_DIR)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()  # Get the JSON data from the request
        now = datetime.now()
        date_str = now.strftime("%Y%m%d-%H%M%S")  # Format: YYYYMMDD-HHMMSS
        unique_id = uuid.uuid4()
        filename = f"{date_str}-{unique_id}.json"
        filepath = os.path.join(WEBHOOK_DIR, filename)

        # Write the JSON data to a file, formatted for readability
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)  # indent=4 for human-readable formatting

        return jsonify({"message": "Webhook received and saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def hello():
    return "You should call /webhook"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')