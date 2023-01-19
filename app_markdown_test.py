# import flask
from flask import Flask, render_template, request, jsonify

from dash import Dash, html, dcc

# server start
application = Flask(__name__)


dash_app2 = Dash(__name__, server=application, url_base_pathname='/down/')


# flask app start
# GET : URL 주소로 데이터 전달하는 방식 : String
@application.route('/', methods=['GET'])
def index():
    print('flask app index()')
    return render_template('index.html')


# --------------------------------------------------------------------------------------------------------
# dash app2
dash_app2.layout = html.Div(children=[
    dcc.Dropdown([1990, 1991, 1992], 1990, id='year-slider'),
    dcc.Markdown('''

        # This is an <h1> tag

        ## This is an <h2> tag

        ###### This is an <h6> tag
    ''')
])

if __name__ == "__main__":
    # application.debug = True
    application.run('0.0.0.0', port=80)