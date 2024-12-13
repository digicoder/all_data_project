from dash import html, dcc, Input, Output
import plotly.express as px

def render(app, df):
    @app.callback(
        Output("bar_chart", "children"),
        Input("dropdown", "value")
      )
    def update_barchart(dropdown):
        filter_df = df.query("COUNTRIES in @dropdown")
        if filter_df.shape[0]==0:
            return html.Div("No data selected.", id="bar_chart")
        fig = px.bar(filter_df, x="COUNTRIES", y="Healthcare_2016 ($ per capita)")
        return html.Div(dcc.Graph(figure=fig), id="bar_chart")
    return html.Div(id="bar_chart")