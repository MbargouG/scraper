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
    url = 'https://github.com/{}/'.format(username)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        repo_name = soup.find("strong", class_="mr-2 flex-self-stretch").text.strip()
        repo_desc = soup.find("p", class_="f4 mt-3").text.strip()
        stars = soup.find("a", class_="social-count js-social-count").text.strip()
        forks = soup.find_all("a", class_="social-count")[1].text.strip()
        return render_template('result.html', repo_name=repo_name, repo_desc=repo_desc, stars=stars, forks=forks)
    else:
        return "Failed to retrieve data from GitHub"

if __name__ == '__main__':
    app.run(debug=True)
