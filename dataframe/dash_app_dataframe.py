import pandas as pd
import plotly.express as px
import component.pp_data_sample as pp


# ---------------------------------------------------------------------
# fig setup
def fig_data():
    # df = px.data.iris()
    # df = pd.read_csv('./assets/job_card_example.csv')
    # print(df.head())
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    df_dir = 'https://raw.githubusercontent.com/regenesis90/datasets/master/sample07_worldbank.csv'
    df = pd.read_csv(df_dir)
    df_1990 = df[df['year'] == 1990]
    fig = px.scatter(df_1990, x='gdp_capita', y='lifeexpectancy',
                     color='region',
                     range_x=[0, 70000])

    # fig = px.line(df, x="연월", y="관광 민예품 및 선물용품 소매업", color="country", text="year")
    # fig.update_traces(textposition="bottom right")
    # print(df['연월'])
    # fig = px.scatter(df['관광 민예품 및 선물용품 소매업', '연월'], x="sepal_length", y="sepal_width",
    #                  color="species")
    return fig


# ---------------------------------------------------------------------
# pp - fig setup
def pp_data_sample():
    data_a = pp.preprocessing()
    # 남자의 연령대별 평균 콜레스테롤 수치 구하기
    y_male = data_a[data_a["성별코드"] == 1].groupby(["연령대코드(5세단위)"])["총콜레스테롤"].mean()
    y_male = pd.DataFrame(y_male)
    y_male["성별코드"] = "1"
    y_male

    # 여자의 연령대별 평균 콜레스테롤 수치 구하기
    y_female = data_a[data_a["성별코드"] == 2].groupby(["연령대코드(5세단위)"])["총콜레스테롤"].mean()
    y_female = pd.DataFrame(y_female)
    y_female["성별코드"] = "2"
    y_female

    df2 = pd.concat([y_male, y_female], keys=["성별코드", "총콜레스테롤"])
    df2.reset_index(inplace=True)
    print(df2)
    fig = px.bar(df2, barmode="group", x="연령대코드(5세단위)", y="총콜레스테롤", color="성별코드")
    return fig
