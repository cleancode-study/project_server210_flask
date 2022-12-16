# flask라는 라이브러리 안에 있는 모든 패키지와 메서드를 가져온다
from flask import Flask, request
# 처음부터 import가 있을 경우는 내장 라이브러리 혹은 내장 패키지이다
# 내장 패키지인 requests를 사용하겠다
import requests
from dash import Dash
# 개발자가 만든 패키지와 class
import pandas_example.Pandas001
import pandas_example.Pandas002
import component_pandas_example.Pandas_compoenet001 as component_pd
import machinelearning_example.Sklean001

import pandas as pd

import csv

print("hello world")
pandas_example.Pandas001.Pandas001.get_dataframe_set()
component_pd.fuc_test()

# 주피터 노트북은 위에 코드가 실행되어야 아래 코드를 활성화 가능하나,
# 일반 파이썬의 함수는 프로그램이 시작되는 시점에 가장 먼저 load = static method (def : 함수)
# form flask import * 안에 Flask라는 패키지를 가져와서 (__name__)이라는 인자값을 넣은 변수 app을 선언
app = Flask(__name__)

#@app. : app이라는 변수 안에 특정값을 받는 route함수를 확인하라는 데코레이션 = spring 어노테이션
#spring의 디스페처서블릿과 동일하게 client의 요청을 계속 대기함
#요청이 들어왔다는 확인만 되면 하단에 있는 함수 실행 (EX: def hello_world())
@app.route('/')
def hello_world():
    # pandas_example이라는 패키지 안에 Pandas001 파일 안에 있는 Pandas001 클래스 파일의 생성자 호출
    data1 = pandas_example.Pandas001.Pandas001(20, 30, 20)
    print(data1.get_data001())
    data2 = machinelearning_example.Sklean001.Sklean001
    # data2.read_csv()
    data_csv = pd.read_csv(
        "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/11-02-2021.csv")
    print(component_pd.fuc_import_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/11-02-2021.csv"))
    data_csv.to_csv("file_test4.csv", index=False)
    component_pd.fuc_export_csv()
    return "testString"


#methods=['GET','POST'] : spring의 @GetMapping과 @PostMapping과 동일 (HTTP 통신이 get방식인지, post방식인지 확인하는 value)
#Get, Post 두가지 모두 받는다는 속성
@app.route('/read_spring_data_example', methods=['GET', 'POST'])
def read_spring_data_example():
    #request.method 변수값은 Flask라는 라이브러리의 request 패키지 안에 있는 method변수값
    if request.method == 'POST':
        return "testPost"
    if request.method == 'GET':
        #url 변수값을 "http://localhost:8090/csvlink?csvRequest=covid19"으로 할당 : 동적타입으로 자동으로 문자열 선언
        url = "http://localhost:8090/csvlink?csvRequest=covid19"
        #respnse 변수에 requests 패키지 안에 있는 get함수 실행 (url 변수값은 위에 문자열url값으로 전달)
        response = requests.get(url=url)
        print(response.content)
        print(response.text)
        print(response.json)
        print(response)
        return "testGET"

# __name__변수가 문자열 '__main__'일 경우 app변수(Flask)의 run()함수가 실행된다
if __name__ == '__main__':
    app.run()
