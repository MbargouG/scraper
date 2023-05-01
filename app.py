from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    # Get the GitHub username from the query string parameter
    username = request.args.get('username')

    # Make a request to the GitHub API to retrieve information about the user's public repositories
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)

    # If the request was successful, parse the JSON response and extract information about the repositories
    if response.status_code == 200:
        repos = json.loads(response.content)

        # Extract information about each repository
        repo_info = []
        for repo in repos:
            repo_name = repo['name']
            repo_desc = repo['description'] or 'No description provided.'
            stars = repo['stargazers_count']
            forks = repo['forks_count']
            repo_info.append({
                'name': repo_name,
                'description': repo_desc,
                'stars': stars,
                'forks': forks
            })

        # Render the result template with the repository information
        return render_template('result.html', username=username, repo_info=repo_info)

    # If the request was not successful, display an error message
    else:
        error_msg = f'Failed to retrieve data from GitHub API ({response.status_code})'
        return render_template('error.html', error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
