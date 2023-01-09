import dataframe.dash_app_dataframe as dash_app_dataframe
from dash import html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


def bar_chart_sample(test):
    sample_layout = html.Div(children=[
        html.Div(
            html.Button(
                dcc.Link(href=test, refresh=True),
            )
        ),
        html.Div(
            dcc.Link(href='/dashapp2/', refresh=True),
        ),
        dcc.Graph(
            id='graph1',
            figure=dash_app_dataframe.fig_data(1990)
        ),
    ])
    return sample_layout

def pp_graph_sample(text_route):
    sample_layout = html.Div(children=[
        html.Div(
            html.Button(
                dcc.Link(href=text_route, refresh=True),
            )
        ),
        html.Div(
            dcc.Link(href='/dashapp2/', refresh=True),
        ),
        dcc.Graph(
            id='graph1',
            figure=dash_app_dataframe.pp_data_sample()
        ),
    ])
    return sample_layout

# def mappie_example() :
#     df = px.data.gapminder().query("year==2007")
#     fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
#                          hover_name="country", size="pop",
#                          projection="natural earth")
#     fig_ex = px.scatter_mapbox()
#     sample_layout = html.Div(children=[
#         dcc.Graph(
#             id='graph1',
#             figure=fig
#         ),
#     ])
#     return sample_layout

def mappie_example() :
    # df = px.data.iris()
    #
    # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
    #                  title="Using The add_trace() method With A Plotly Express Figure")

    # df = px.data.gapminder().query("year==2007")
    # fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
    #                          hover_name="country", size="pop",
    #                          projection="natural earth")
    #
    # fig.add_trace(
    #     go.Scatter(
    #         x=[2, 4],
    #         y=[4, 8],
    #         mode="lines",
    #         line=go.scatter.Line(color="gray"),
    #         showlegend=False)
    # )

    # lat = [40.7, 41.3, 37.5]
    # lon = [-74.0, -72.0, -122.4]
    #
    # # Define the data for the pie charts
    # data = [{'labels': ['Apple', 'Banana', 'Orange'], 'values': [10, 20, 30], 'type': 'pie'},
    #         {'labels': ['Dog', 'Cat', 'Bird'], 'values': [25, 10, 15], 'type': 'pie'},
    #         {'labels': ['Men', 'Women'], 'values': [50, 50], 'type': 'pie'}]
    #
    # # Create the figure
    # fig = go.Figure()
    #
    # # Add the pie charts to the figure
    # for i in range(len(data)):
    #     fig.add_trace(go.Scattergeo(lat=[lat[i]], lon=[lon[i]], mode='markers',
    #                                 marker=go.scattergeo.Marker(size=20, colorscale='Reds', color=data[i]['values'],
    #                                                             cmin=0, cmax=100, showscale=True),
    #                                 text=data[i]['labels'], textfont=dict(size=14)))
    #
    # # Set the layout of the figure
    # fig.update_layout(geo=go.layout.Geo(projection_type='natural earth'))
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})



    # lat = [40.7, 41.3, 37.5]
    # lon = [-74.0, -72.0, -122.4]
    #
    # # Define the data for the pie charts
    # data = [{'labels': ['Apple', 'Banana', 'Orange'], 'values': [10, 20, 30], 'type': 'pie'},
    #         {'labels': ['Dog', 'Cat', 'Bird'], 'values': [25, 10, 15], 'type': 'pie'},
    #         {'labels': ['Men', 'Women'], 'values': [50, 50], 'type': 'pie'}]
    #
    # # Create the figure
    # fig = go.Figure()
    #
    # # Add the pie charts to the figure
    # for i in range(len(data)):
    #     fig.add_trace(go.Scattergeo(lat=[lat[i]], lon=[lon[i]], mode='markers',
    #                                 marker=go.scattergeo.Marker(size=20, colorscale='Reds', color=data[i]['values'],
    #                                                             cmin=0, cmax=100, showscale=True),
    #                                 text=data[i]['labels'], textfont=dict(size=14)))
    #
    # # Set the layout of the figure
    # fig.update_layout(
    #     geo=go.layout.Geo(projection_type='natural earth', landcolor='white', showocean=True,
    #                       oceancolor='lightblue', showcountries=True, countrycolor='gray', showcoastlines=True,
    #                       coastlinecolor='lightgray', showrivers=True, rivercolor='blue', showlakes=True,
    #                       lakecolor='lightblue', showframe=False, framecolor='white',
    #                       bgcolor='rgba(0,0,0,0)'))
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # use mapbox
    # px.set_mapbox_access_token("your-mapbox-access-token")

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

    # Add the pie charts to the figure
    for i in range(len(data)):
        fig.add_trace(go.Scattermapbox(lat=[lat[i]], lon=[lon[i]], mode='markers',
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