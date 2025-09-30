from flask import Flask, request
import requests

app = Flask(__name__)

# Your Telegram details
TELEGRAM_TOKEN = "8395367042:AAG--avUlp1VHYzz3EQauM5GGCXzCPP7fy4"
CHAT_ID = "6299292695"

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
