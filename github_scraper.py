import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for rendering the HTML template
@app.route("/")
def index():
    return render_template("index.html")

# Define a route for handling the search form submission
@app.route("/search_users")
def search_users():
    query = request.args.get('query')
    # Replace YOUR_GITHUB_TOKEN with your own GitHub API token
    headers = {'Authorization': ''}
    # Make a request for searching users based on the query
    response = requests.get(f'https://api.github.com/search/users?q={query}', headers=headers)
    if response.status_code == 200:
        # Parse and extract the relevant data
        search_results = response.json()['items']
        return render_template("search_results.html", search_results=search_results)
    else:
        return "Failed to search for users"

# Define a route for scraping data from GitHub and displaying it
@app.route("/scrape_github")
def scrape_github():
    # Replace with your own GitHub repository URL
    url = "https://github.com/octocat/hello-world"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the repository name
        repo_name = soup.find("strong", class_="mr-2 flex-self-stretch").text.strip()
        # Find the repository description
        repo_desc = soup.find("p", class_="f4 mt-3").text.strip()
        # Find the number of stars
        stars = soup.find("a", class_="social-count js-social-count").text.strip()
        # Find the number of forks
        forks = soup.find_all("a", class_="social-count")[1].text.strip()
        return render_template("github_data.html", repo_name=repo_name, repo_desc=repo_desc, stars=stars, forks=forks)
    else:
        return "Failed to retrieve data from GitHub"

if __name__ == '__main__':
    app.run(debug=True)
