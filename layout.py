from dash import html
import dash_bootstrap_components as dbc
from components import dropdown
from components import barchart
def create_layout(app,df):
        return dbc.Container([
        dropdown.render(app,df),
        barchart.render(app,df),
        ])
