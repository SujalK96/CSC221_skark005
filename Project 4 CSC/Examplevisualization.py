import requests
import plotly.graph_objs as go
from plotly.offline import plot

# Making an API call and checking the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Converting the response object to a dictionary.
response_dict = r.json()

# Extracting repository information.
repo_dicts = response_dict['items']
repo_names = [repo_dict['name'] for repo_dict in repo_dicts]
stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

# Creating the bar chart.
data = [
    go.Bar(
        x=repo_names,
        y=stars,
    )
]

layout = go.Layout(
    title='Stars Count for Python Repositories on GitHub',
    xaxis=dict(title='Repository'),
    yaxis=dict(title='Stars Count'),
)

fig = go.Figure(data=data, layout=layout)
plot(fig, filename='python_repos_stars.html')
