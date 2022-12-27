import flask

import plotly.express as px
from dash import Dash, html, dcc

# server start
application = flask.Flask(__name__)

# dash app with flask server
dash_app1 = Dash(__name__, server=application, url_base_pathname='/dashapp1/')
dash_app2 = Dash(__name__, server=application, url_base_pathname='/dashapp2/')

# flask app start
@application.route('/')
def index():
    print('flask app index()')
    return 'index'


# --------------------------------------------------------------------------------------------------------
# dash app1

df = px.data.iris()

fig_1 = px.scatter(df, x="sepal_length", y="sepal_width",
                 color="species")

dash_app1.layout = html.Div(children=[
    html.Div(
        html.Button(
            dcc.Link(href='/dashapp1/', refresh=True),
        )
    ),
    html.Div(
        dcc.Link(href='/dashapp2/', refresh=True),
    ),
    dcc.Graph(
        id='graph1',
        figure=fig_1
    ),
])

# --------------------------------------------------------------------------------------------------------
# dash app2

fig_2 = px.scatter(df, x="sepal_length", y="sepal_width",
                 color="species")

dash_app2.layout = html.Div(children=[
    dcc.Graph(
        id='graph1',
        figure=fig_2
    )
])

# run app
if __name__ == "__main__":
    application.debug = True
    application.run()