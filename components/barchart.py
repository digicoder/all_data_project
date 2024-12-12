from dash import html, dcc
import plotly.express as px

def render(app, data):
  fig = px.bar(data, x="COUNTRIES", y="Healthcare_2016 ($ per capita)")
  return html.Div(dcc.Graph(figure=fig), id="bar_chart")