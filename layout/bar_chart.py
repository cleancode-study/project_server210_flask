import dataframe.dash_app_dataframe as dash_app_dataframe
from dash import html, dcc


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