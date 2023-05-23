import plotly_express
import numpy as np
from dash import Dash, dcc
from dash.html import H1, Div, P, H2

app = Dash(__name__)

app.layout = Div([
    H1("Dice simulator"),
    P("Choose number of dice and number of rolls and enjoy the results"),
    H2("Number of rolls ")
])


if __name__ == "__main__":
    print('Hello from the docker side')

    app.run_server(debug=True)