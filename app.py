import flask
from flask import Flask, render_template, request

# dash : plotly 라이브러리에서 python 버전으로 출시된 웹기반 그래프 출력 라이브러리 (javascript plotly와 유사)
# https://plotly.com/python/
# https://dash.plotly.com/
# dash.dcc : dash core component : dash에서 제공하는 기본 tag (그래프, 다운로드.. 등 기능)
# dash.html : html에서 제공하는 기본 tag (체크박스, input, button, 라디오버튼, div, p, a... html에서 늘 사용하는 tag)
# 기타 dashTable(테이블), dashCanvas(이미지출력) 등등 다양한 기능은 차순위

# callback : 매개변수, 전역변수를 담당하는 함수

import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import dataframe.dash_app_dataframe as dash_app_dataframe
import layout.bar_chart as bar_chart

external_stylesheets = ["style.css"]

# server start
application = Flask(__name__)


# dash app with flask server : fask에 dash 라이브러리 추가 route
# server=application : flask 서버(application 변수명)를 사용하여 
# url_base_pathname='/dashapp1/' 경로명에 dash 라이브러리 페이지를 출력한다 >> 변수 dash_app1에 저장한다
# Dash라는 패키지 생성자를 사용하여 하나의 page를 생성
# Dash(__name__(시작 메서드), server=application(연동하는 서버 변수), url_base_pathname='/dashapp1/'(URL주소))
# title 속성으로 매개변수 전달
dash_app1 = Dash(__name__, server=application, url_base_pathname='/dashapp1/', external_stylesheets=external_stylesheets, title='/dashapp1/')
dash_app2 = Dash(__name__, server=application, url_base_pathname='/dashapp2/')
dash_app3 = Dash(__name__, server=application, url_base_pathname='/pp1/', external_stylesheets=external_stylesheets, title='sample1')
dash_app4 = Dash(__name__, server=application, url_base_pathname='/mappie/')

# flask app start
# GET : URL 주소로 데이터 전달하는 방식 : String
@application.route('/', methods=['GET'])
def index():
    print('flask app index()')
    return render_template('index.html')


# POST : URL 주소가 아닌 BODY에 데이터 전달하는 방식 : 객체
@application.route('/', methods=['POST'])
def index_POST():
    print('flask app index()')
    test = int(request.form['test'])
    print(test)
    return render_template('index_output.html', data=test)

# dynamic route
@application.route('/dynamic/<pagename>',  methods=['GET'])
def hello(pagename):
    return render_template('index_output.html', data=pagename)

# --------------------------------------------------------------------------------------------------------
# dash app1
# dash 페이지의 html을 구성하는 dataframe 변수
# 만들어진 dash page 안에 html구조 생성 : layout
dash_app1.layout = bar_chart.bar_chart_sample(dash_app1.title)

# --------------------------------------------------------------------------------------------------------
# dash app2
dash_app2.layout = html.Div(children=[
    dcc.Dropdown([1990, 1991, 1992], 1990, id='year-slider'),
    dcc.Graph(id='graph-with-slider'),
])


@dash_app2.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_output(value):
    print(value)
    fig = dash_app_dataframe.fig_data(value)
    print(fig)
    fig.update_layout(transition_duration=500)
    return fig

# --------------------------------------------------------------------------------------------------------
# dash app3 - pp example
dash_app3.layout = bar_chart.bar_chart_sample(dash_app1.title)
# dash_app3.layout = bar_chart.pp_graph_sample(dash_app3.title)

# --------------------------------------------------------------------------------------------------------
# dash app4
dash_app4.layout = bar_chart.mappie_example()

# run app : flask서버 기동
# __main__ : web python 코드의 시작점을 알려주는 변수
if __name__ == "__main__":
    # application.debug = True
    application.run('0.0.0.0', port=80)