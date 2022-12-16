from flask import Flask, request
import component.pandas_example001 as ps
import requests

app = Flask(__name__)


@app.route('/init_pandas', methods=['GET'])
def init_pandas():
    result = ps.read_url("example")
    ps.pandas_config(result)
    return result


if __name__ == '__main__':
    app.run()




