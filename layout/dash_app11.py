import plotly.express as px
import pandas as pd


def fig_data():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_length", y="sepal_width",
                     color="species")
    return fig


def preprocessing():
    df1 = pd.read_csv('2017.csv', encoding="CP949")
    df1.drop(["구강검진수검여부", "치아우식증유무", "결손치유무", "치아마모증유무", "제3대구치(사랑니)이상",
              "치석", "데이터공개일자", "기준년도", "가입자일련번호", "시도코드",
              "시력(좌)", "시력(우)", "청력(좌)", "청력(우)"], axis=1, inplace=True)

    df1["BMI"] = df1["체중(5Kg단위)"] / ((df1["신장(5Cm단위)"] / 100) * (df1["신장(5Cm단위)"] / 100))
    df_bmi = df1["BMI"]

    for i, b in enumerate(df_bmi):
        if b < 18.5:
            df_bmi[i] = '저체중'
        elif b <= 22.9:
            df_bmi[i] = '정상'
        elif b <= 24.9:
            df_bmi[i] = '비만전단계'
        elif b <= 29.9:
            df_bmi[i] = '1단계비만'
        elif b <= 34.9:
            df_bmi[i] = '2단계비만'
        else:
            df_bmi[i] = '3단계비만'

    df1["BMI단계"] = df_bmi
    df1["BMI"] = df1["체중(5Kg단위)"] / ((df1["신장(5Cm단위)"] / 100) * (df1["신장(5Cm단위)"] / 100))
    df1 = df1.dropna()
    return df1


def grap1():
    data_a = preprocessing()
    age = data_a["연령대코드(5세단위)"].sort_values().unique()
    y_male = data_a[data_a["성별코드"] == 1].groupby(["연령대코드(5세단위)"])["총콜레스테롤"].mean()
    y_female = data_a[data_a["성별코드"] == 2].groupby(["연령대코드(5세단위)"])["총콜레스테롤"].mean()
    df2 = pd.concat([y_male, y_female], axis=1, keys=["남자-총콜레스테롤", "여자-총콜레스테롤"])
    fig = px.bar(df2, x=["남자-총콜레스테롤", "여자-총콜레스테롤"], y="연령대코드(5세단위)", color="City", barmode="group")
    return fig
