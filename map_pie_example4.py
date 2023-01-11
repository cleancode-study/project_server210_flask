import plotly.graph_objs as go
from dash import Dash, html, dcc
import plotly.express as px
from flask import Flask, render_template, request
import geopandas as gpd

application = Flask(__name__)

dash_app4 = Dash(__name__, server=application, url_base_pathname='/')
def mappie_example() :
    # Define the latitude and longitude coordinates for the location
    lat = 33.431441
    lon = 126.874237

    df = px.data.election()
    geo_df = gpd.GeoDataFrame.from_features(
        px.data.election_geojson()["features"]
    ).merge(df, on="district").set_index("district")

    fig = px.choropleth_mapbox(geo_df,
                               geojson=geo_df.geometry,
                               locations=geo_df.index,
                               color="Joly",
                               center={"lat": lat, "lon": lon},
                               mapbox_style="open-street-map",
                               zoom=8.5)


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