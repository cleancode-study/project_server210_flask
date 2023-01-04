import pandas as pd

def data_load() :
    df1 = pd.read_csv(
        '20221216150405_file_name.csv')
    return df1

# 데이터 전처리 함수
def preprocessing():
    df1 = data_load()
    print(df1)
    df1.drop(["구강검진수검여부", "치아우식증유무", "결손치유무", "치아마모증유무", "제3대구치(사랑니)이상",
              "치석", "데이터공개일자", "기준년도", "가입자일련번호", "시도코드",
              "시력(좌)", "시력(우)", "청력(좌)", "청력(우)"], axis=1, inplace=True)

    df1["BMI"] = df1["체중(5Kg단위)"] / ((df1["신장(5Cm단위)"] / 100) * (df1["신장(5Cm단위)"] / 100))
    df_bmi = df1["BMI"]

    # 저체중 < 18.5
    # 정상 18.5~22.9
    # 비만 전단계 23~24.9
    # 1단계비만 25~29.9
    # 2단계비만 30~34.9
    # 3단계비만 >35

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
