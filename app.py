from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    username = request.args.get('username')
    url = 'https://api.github.com/users/{}/repos'.format(username)
    headers = {'Authorization': 'token YOUR_GITHUB_TOKEN'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        repo_name = repos[0]['name']
        repo_desc = repos[0]['description']
        stars = repos[0]['stargazers_count']
        forks = repos[0]['forks_count']
        return render_template('result.html', repo_name=repo_name, repo_desc=repo_desc, stars=stars, forks=forks)
    else:
        return "Failed to retrieve data from GitHub"

if __name__ == '__main__':
    app.run(debug=True)
