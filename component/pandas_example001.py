# as : 별명
import pandas as pd
from datetime import datetime

def save_pandas():
    area = [3000, 2000, 5000, 2100, 4000]
    price = [50000, 51000, 52000, 53000, 54000]

    df = pd.DataFrame(area, columns=['area'])
    df['price'] = price

    df.to_csv(export_title_name("file_name"), index=False)
    print(df)

def export_title_name(var1):
    now = datetime.now()
    str_date = now.strftime('%Y%m%d%H%M%S_')
    return str_date+var1+".csv"

save_pandas()