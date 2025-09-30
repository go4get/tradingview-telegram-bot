from flask import Flask, request
import requests, os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID", "YOUR_CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("text", "🚨 New TradingView Alert")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
