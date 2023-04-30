import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_users")
def search_users():
    query = request.args.get('query')
    # Replace YOUR_GITHUB_TOKEN with your own GitHub API token
    headers = {'Authorization': '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'}
    # Make a request for searching users based on the query
    response = requests.get(f'https://api.github.com/search/users?q={query}', headers=headers)
    if response.status_code == 200:
        # Parse and extract the relevant data
        search_results = response.json()['items']
        return render_template("search_results.html", search_results=search_results)
    else:
        return "Failed to search for users"

if __name__ == '__main__':
    app.run(debug=True)
