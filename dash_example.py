from dash import Dash, html, dcc
import plotly.express as px


df = px.data.iris() # 데이터(csv 또는 pandas.dataframe 블러오기)
# plotly를 이용한 산점도
fig = px.scatter(df, x="sepal_length", y="sepal_width",
                 color="species")

fig_another = px.scatter(df, x="sepal_length", y="sepal_width",
                         color="species")

app = Dash(__name__)

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

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)