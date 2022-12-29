from flask import Flask, request
import component.pandas_example001 as ps
from dash import Dash, html, dcc
import plotly.express as px
import requests

# ------------------ graph and dataframe example
df = px.data.iris() # iris data 불러오기
# plotly를 이용한 산점도
fig = px.scatter(df, x="sepal_length", y="sepal_width",
                 color="species")

fig_another = px.scatter(df, x="sepal_length", y="sepal_width",
                         color="species")

app = Flask(__name__)


# server110 연동 route
@app.route('/init_pandas', methods=['GET'])
def init_pandas():
    result = ps.read_url("covid19")
    ps.pandas_config(result)
    return result

app.layout = html.Div(children=[
    # dash.core.component(dcc)의 그래프컴포넌트로 plotly 그래프 렌더링
    dcc.Graph(
        id='graph1',
        figure=fig
    ),
    dcc.Graph(
        id='graph2',
        figure=fig_another
    ),
])
#
# if __name__ == '__main__':
#     app.run()




