from dash import html, dcc


def render (app,df):
    all_data=  df["COUNTRIES"].unique()
    options =[{"label": x, "value":x} for x in all_data]
    return html.Div([
        dcc.Dropdown(
            options=options,
            value="FRA",
            multi=True,
            id="dropdown"
        )
    ])


