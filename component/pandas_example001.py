# as : 별명
import pandas as pd
def start_pandas():
    area = [3000, 2000, 5000, 2100, 4000]
    price = [50000, 51000, 52000, 53000, 54000]

    df = pd.DataFrame(area, columns=['area'])
    df['price'] = price

    df.to_csv("start_pandas_export1.csv", index=False)
    print(df)

start_pandas()