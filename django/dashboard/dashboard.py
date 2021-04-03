import datetime
from collections import deque

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from django.utils import timezone

from api.models import Request

num_minutes = 20
max_len = num_minutes * 60
X = deque(maxlen=max_len)
tz = timezone.get_current_timezone()
methods = ['GET', 'POST', 'PUT', 'DELETE']
Ys = {method: deque(maxlen=max_len) for method in methods}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1('Live Graph'),
    dcc.Graph(id='live-graph', animate=True,
              style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Interval(
        id='graph-update',
        ),

    ])


def get_recent_requests(only_new_requests=False, **kwargs):
    now = timezone.datetime.now(tz=tz)
    some_time_ago = now - datetime.timedelta(**kwargs)
    requests = Request.objects.filter(datetime__range=[some_time_ago, now])
    if only_new_requests:
        requests = requests.filter(shown_in_graph=False)
    return requests.order_by('datetime')


def update_ys(requests):
    counter = {method: 0 for method in methods}
    for request in requests:
        counter[request.type] += request.response_time / 1000
        request.shown_in_graph = True
        request.save()
    for method, val in counter.items():
        Ys[method].append(val)
    return counter


# Plot initial graph
now = timezone.datetime.now(tz=tz)
previous_requests = deque(get_recent_requests(minutes=num_minutes))
if previous_requests:
    first_req_dt = timezone.template_localtime(previous_requests[0].datetime)
    all_seconds = [first_req_dt + datetime.timedelta(seconds=x) for x in
                   range(0, (now - first_req_dt).seconds)]
    for t in all_seconds:
        X.append(t)
        current_requests = deque()
        while previous_requests and previous_requests[0].datetime < t:
            current_requests.appendleft(previous_requests.popleft())
        update_ys(current_requests)
else:
    X.append(now)
    for Y in Ys.values():
        Y.append(0)


def make_scatter_plot(name):
    return go.Scatter(
        x=list(X),
        y=list(Ys[name]),
        name=name,
        fill='tozeroy'
        )


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')])
def update_graph(value):
    now = timezone.datetime.now(tz=tz)
    X.append(now)
    requests = get_recent_requests(seconds=4, only_new_requests=True)
    counter = update_ys(requests)
    plots = [make_scatter_plot(method) for method in counter]

    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(X), max(X)]),
        yaxis=dict(range=[0, max([max(i) for i in Ys.values()])]),
        xaxis_title="Time",
        yaxis_title="Request Response Time (s)",
        font=dict(family="Helvetica",
                  size=12,
                  color='white'),
        height=700,

        )
    return {'data': plots, 'layout': layout}
