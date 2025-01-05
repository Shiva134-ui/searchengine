from flask import Flask, render_template, request
from serpapi import GoogleSearch

app = Flask(__name__)

# Function to perform a Google search using SerpApi
def search_internet(query):
    params = {
        "q": query,
        "api_key": "e89e7e03b8a6e0fef3fb927f9e967d681be71da1b9db9a3645ae73acab0f05d5"  # Replace with your SerpApi key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # Check if 'organic_results' is in the response
    if 'organic_results' in results:
        return results['organic_results']
    else:
        return []  # Return an empty list if no organic results are found

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = search_internet(query)
        return render_template('search_results.html', results=results, query=query)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
