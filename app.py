from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_user_info", methods=["POST"])
def get_user_info():
    username = request.form["username"]
    # Replace YOUR_GITHUB_TOKEN with your own GitHub API token
    headers = {"Authorization": "token YOUR_GITHUB_TOKEN"}
    # Make a request for the user's profile data
    response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    if response.status_code == 200:
        # Parse and extract the relevant data
        user_info = response.json()
        return render_template("user_info.html", user_info=user_info)
    else:
        return "Failed to get user info"

if __name__ == "__main__":
    app.run(debug=True)
