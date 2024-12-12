from dash import html, dcc


def render (app,df):
    all_data=  df["COUNTRIES"].unique()
    y="Healthcare_2016 ($ per capita)"
    options =[{"label": x, "value":y} for x in all_data]
    return html.Div([
        dcc.Dropdown(
            options=options,
            value=y,
            multi=False,
            id="dropdown"
        )
    ])


