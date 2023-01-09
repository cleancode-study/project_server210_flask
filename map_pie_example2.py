import plotly.graph_objs as go
from dash import Dash, html, dcc
import plotly.express as px
from flask import Flask, render_template, request

application = Flask(__name__)

dash_app4 = Dash(__name__, server=application, url_base_pathname='/')
def mappie_example() :
    # Define the latitude and longitude coordinates for the locations
    lat = [40.7, 41.3, 37.5]
    lon = [-74.0, -72.0, -122.4]

    # Define the data for the pie charts
    data = [{'labels': ['Apple', 'Banana', 'Orange'], 'values': [10, 20, 30], 'type': 'pie'},
            {'labels': ['Dog', 'Cat', 'Bird'], 'values': [25, 10, 15], 'type': 'pie'},
            {'labels': ['Men', 'Women'], 'values': [50, 50], 'type': 'pie'}]

    # Create the figure
    fig = go.Figure()

    df_in = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df_in.loc[df_in['pop'] < 2.e6, 'country'] = 'Other countries'  # Represent only large countries
    fig_in = px.pie(df_in, values='pop', names='country', title='Population of European continent')

    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]

    fig_ex = go.Figure(data=[go.Pie(labels=labels, values=values)])

    # Add the pie charts to the figure
    for i in range(len(data)):
        fig.add_trace(go.Scattermapbox(lat=[lat[i]], lon=[lon[i]], mode='markers',
                                       # marker=dict(symbol='marker', size=15, color='blue'),
                                       marker=go.scattermapbox.Marker(size=20, colorscale='Reds',
                                                                      color=data[i]['values'], cmin=0, cmax=100,
                                                                      showscale=True), text=data[i]['labels'],
                                       hoverinfo='text', textfont=dict(size=14)))

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