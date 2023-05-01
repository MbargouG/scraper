import requests
import json


@app.route("/get_user_info", methods=["POST"])
def get_user_info():
    # Get the username entered by the user
username = request.form['username']

# Replace YOUR_GITHUB_TOKEN with your own GitHub API token
headers = {'Authorization': 'token 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'}

# Make a request for the user information
response = requests.get(f'https://api.github.com/users/{username}', headers=headers)

if response.status_code == 200:
    # Parse the response JSON
    user_info = json.loads(response.text)
    return render_template("user_info.html", user_info=user_info)
else:
    return "Failed to retrieve user information"
