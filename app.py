import flask

# dash : plotly 라이브러리에서 python 버전으로 출시된 웹기반 그래프 출력 라이브러리 (javascript plotly와 유사)
# https://plotly.com/python/
# https://dash.plotly.com/
# dash.dcc : dash core component : dash에서 제공하는 기본 tag (그래프, 다운로드.. 등 기능)
# dash.html : html에서 제공하는 기본 tag (체크박스, input, button, 라디오버튼, div, p, a... html에서 늘 사용하는 tag)
# 기타 dashTable(테이블), dashCanvas(이미지출력) 등등 다양한 기능은 차순위

# callback : 매개변수, 전역변수를 담당하는 함수

import plotly.express as px
from dash import Dash, html, dcc
import dataframe.dash_app_dataframe as dash_app_dataframe
import layout.bar_chart as bar_chart

# server start
application = flask.Flask(__name__)

# dash app with flask server : fask에 dash 라이브러리 추가 route
# server=application : flask 서버(application 변수명)를 사용하여 
# url_base_pathname='/dashapp1/' 경로명에 dash 라이브러리 페이지를 출력한다 >> 변수 dash_app1에 저장한다
dash_app1 = Dash(__name__, server=application, url_base_pathname='/dashapp1/')
dash_app2 = Dash(__name__, server=application, url_base_pathname='/dashapp2/')

# --------------------------------------------------------------------------------------------------------
# dash app1
# dash 페이지의 html을 구성하는 dataframe 변수
dash_app1.layout = bar_chart.bar_chart_sample()

# --------------------------------------------------------------------------------------------------------
# dash app2
dash_app2.layout = html.Div(children=[
    dcc.Graph(
        id='graph1',
        figure=dash_app_dataframe.fig_data()
    )
])

# # flask app start
# @application.route('/')
# def index():
#     print('flask app index()')
#     return 'index'

# run app : flask서버 기동
# __main__ : web python 코드의 시작점을 알려주는 변수
if __name__ == "__main__":
    application.debug = True
    application.run()