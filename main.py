from flask import *
import requests
from dash import Dash
import pandas_example.Pandas001
import pandas_example.Pandas002

print("hello world")

app = Flask(__name__)


@app.route('/')
def hello_world():
    data1 = pandas_example.Pandas001.Pandas001(20, 30)
    print(data1.get_data001())
    return "testString"


@app.route('/read_spring_data_example', methods=['GET', 'POST'])
def read_spring_data_example():
    if request.method == 'POST':
        return "testPost"
    if request.method == 'GET':
        url = "http://localhost:8090/csvlink?csvRequest=covid19"
        response = requests.get(url=url)
        print(response)
        return "testGET"


if __name__ == '__main__':
    app.run()
