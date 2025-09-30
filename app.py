from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8395367042:AAG--avUlp1VHYzz3EQauM5GGCXzCPP7fy4"
CHAT_ID = "6299292695"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = None
    try:
        data = request.get_json(force=True)  # try parse JSON
        message = data.get("text", "⚠️ No text in payload")
    except:
        # fallback if TradingView sent plain text
        message = request.data.decode("utf-8")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})

    return "ok", 200
