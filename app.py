# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

app = Dash(__name__)

import json
with open('trips.json', 'r') as f:
    data = json.loads(f.read())

# Normalize data
df = pd.json_normalize(data, record_path =['features'])

# Explore for Street names
gcod_street_df = df.explode('properties.streetnames')
# Remove column name 'geometry.coordinates'
gcod_street_df = gcod_street_df.drop(['geometry.coordinates'], axis=1)

street_name_list = df["properties.streetnames"].tolist()


fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
