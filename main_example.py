from flask import Flask, request
import component.pandas_example001 as ps
import requests

app = Flask(__name__)


@app.route('/init_pandas', methods=['GET'])
def init_pandas():
    ps.save_pandas()
    return "hello world"


if __name__ == '__main__':
    app.run()
