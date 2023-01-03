import pandas as pd
import plotly.express as px
import component.pandas_example001 as pandas_example001


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

