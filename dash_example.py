from dash import Dash

from layout import bar_chart

app = Dash(__name__, title='sample1')

app.layout = bar_chart.pp_graph_sample(app.title)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)