import pandas as pd
from datetime import datetime

def fuc_test():
    print('teset')

def fuc_import_csv(var1):
    return pd.read_csv(var1)

def fuc_export_csv():
    now = datetime.now()
    path = now.strftime('%Y%m%d')
    print(path)
    var1 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/11-02-2021.csv")
    print(var1)
    var1.to_csv(path+"_file.csv", index = False)
    # var1.to_csv("/csv/file.csv", index=False)