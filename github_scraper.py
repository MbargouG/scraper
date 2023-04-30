import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_user_info", methods=["POST"])
def get_user_info():
    username = request.form["username"]
    # Replace YOUR_GITHUB_TOKEN with your own GitHub API token
    headers = {'Authorization': 'token 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'}
    # Make a request for user information based on the username
    response = requests.get(f'https://api.github.com/users/{username}', headers=headers)
    if response.status_code == 200:
        # Parse and extract the relevant data
        user_info = response.json()
        name = user_info['name']
        avatar_url = user_info['avatar_url']
        bio = user_info['bio']
        public_repos = user_info['public_repos']
        followers = user_info['followers']
        following = user_info['following']
        return render_template("user_info.html", name=name, avatar_url=avatar_url, bio=bio, public_repos=public_repos, followers=followers, following=following)
    else:
        return "Failed to get user information"

if __name__ == '__main__':
    app.run(debug=True)
