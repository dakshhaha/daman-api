from flask import Flask, jsonify, request
import requests, time

app = Flask(__name__)

BASE_URL = "https://draw.ar-lottery01.com/WinGo/WinGo_30S"

def now_ts():
    """Return current timestamp in milliseconds"""
    return int(time.time() * 1000)

@app.route("/latest")
def latest():
    """Fetch the latest issue info (previous/current/next)"""
    url = f"{BASE_URL}.json?ts={now_ts()}"
    r = requests.get(url, timeout=10)
    return jsonify(r.json())

@app.route("/history")
def history():
    """Fetch past draws with numbers + colors"""
    page = request.args.get("page", 1)
    page_size = request.args.get("pageSize", 10)
    url = f"{BASE_URL}/GetHistoryIssuePage.json?page={page}&pageSize={page_size}&ts={now_ts()}"
    r = requests.get(url, timeout=10)
    return jsonify(r.json())

@app.route("/predict")
def predict():
    """
    Naive example predictor:
    - Counts frequency of last N results
    - Returns most common number & color
    """
    n = int(request.args.get("limit", 20))
    url = f"{BASE_URL}/GetHistoryIssuePage.json?page=1&pageSize={n}&ts={now_ts()}"
    r = requests.get(url, timeout=10)
    data = r.json()["data"]["list"]

    numbers = [d["number"] for d in data]
    colors = [d["color"] for d in data]

    # simple frequency analysis
    from collections import Counter
    top_number = Counter(numbers).most_common(1)[0][0]
    top_color = Counter(colors).most_common(1)[0][0]

    return jsonify({
        "analyzed": n,
        "predicted_number": top_number,
        "predicted_color": top_color
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
