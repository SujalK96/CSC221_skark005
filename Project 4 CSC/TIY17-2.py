import requests
from operator import itemgetter
import plotly.graph_objs as go
from plotly.offline import plot

# Making an API call and checking the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Making a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Building a dictionary for each article.
    if 'descendants' in response_dict:
        comments = response_dict['descendants']
    else:
        comments = 0
    
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': comments,
    }
    submission_dicts.append(submission_dict)

# Sorting submissions by the number of comments.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extracting submission titles, comment counts, and links.
titles = [submission['title'] for submission in submission_dicts]
comment_counts = [submission['comments'] for submission in submission_dicts]
hn_links = [submission['hn_link'] for submission in submission_dicts]

hover_text = [f'<a href="{link}" target="_blank">{title}</a>' for title, link in zip(titles, hn_links)]

# Create the bar chart.
data = [
    go.Bar(
        x=hover_text,  
        y=comment_counts,
        hoverinfo='y+text', 
        text=titles,
        marker=dict(color='steelblue'),
    )
]

layout = go.Layout(
    title='Most Active Discussions on Hacker News',
    xaxis=dict(title='Submission Title', tickangle=-45),
    yaxis=dict(title='Number of Comments'),
)

fig = go.Figure(data=data, layout=layout)

plot(fig, filename='hacker_news_discussions.html')
