import plotly.graph_objs as go
from dash import Dash, html, dcc
import plotly.express as px
from flask import Flask, render_template, request

application = Flask(__name__)

dash_app4 = Dash(__name__, server=application, url_base_pathname='/')
def mappie_example() :
    # Define the latitude and longitude coordinates for the location
    lat = [40.7]
    lon = [-74.0]

    # Define the data for the pie chart
    data = {'labels': ['Apple', 'Banana', 'Orange'], 'values': [10, 20, 30], 'type': 'pie'}

    # Create the figure
    fig = go.Figure()

    # Add the pie chart to the figure
    fig.add_trace(go.Scattermapbox(lat=lat, lon=lon, mode='markers',
                                   marker=go.scattermapbox.Marker(size=20, colorscale='Reds', color=data['values'],
                                                                  cmin=0, cmax=100, showscale=True),
                                   text=data['labels'], hoverinfo='text', textfont=dict(size=14)))

    # Set the layout of the figure
    fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=41, mapbox_center_lon=-74, mapbox_zoom=4)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


    sample_layout = html.Div(children=[
        dcc.Graph(
            id='graph1',
            figure=fig
        ),
    ])

    return sample_layout

dash_app4.layout = mappie_example

if __name__ == "__main__":
    # application.debug = True
    application.run('0.0.0.0', port=80)