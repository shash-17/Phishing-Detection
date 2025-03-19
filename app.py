from flask import Flask, render_template, request, jsonify
import requests
import validators
import urllib.parse

app = Flask(__name__)

GOOGLE_API_KEY = "API KEY"
IPQS_API_KEY = "API KEY"

# Google Safe Browsing API
def check_google_safe_browsing(url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}"
    payload = {
        "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    response = requests.post(api_url, json=payload)
    try:
        data = response.json()
        if "matches" in data:
            return {"status": True, "details": data["matches"]}
        return {"status": False, "details": "No threats detected"}
    except requests.exceptions.JSONDecodeError:
        return {"status": False, "details": "Error fetching data"}

#IPQualityScore API
def check_ipqs(url):
    encoded_url = urllib.parse.quote_plus(url)  # Encode URL for safety
    endpoint = f"https://www.ipqualityscore.com/api/json/url/{IPQS_API_KEY}/{encoded_url}"
    
    response = requests.get(endpoint)
    try:
        data = response.json()
        return {"status": data.get("unsafe", False), "details": data}
    except requests.exceptions.JSONDecodeError:
        return {"status": False, "details": "Error fetching data"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_url():
    """Check if the given URL is phishing."""
    url = request.json.get("url")

    if not validators.url(url):  #Improved URL validation
        return jsonify({"error": "Invalid URL format"}), 400

    # Run phishing checks
    google_result = check_google_safe_browsing(url)
    ipqs_result = check_ipqs(url)

    # Confidence Score Calculation
    confidence_score = 0
    if google_result["status"]:
        confidence_score += 50

    if ipqs_result["status"]:
        confidence_score += 50

    result = {
        "status": "Phishing Detected" if confidence_score > 0 else "Safe",
        "confidence": confidence_score if confidence_score > 0 else 100,
        "google_safe_browsing": google_result,
        "ipqualityscore": ipqs_result,
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
