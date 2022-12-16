# as : 별명
import pandas as pd
from datetime import datetime
import requests


def save_pandas():
    """
    create dataframe
    :return: none
    """
    area = [3000, 2000, 5000, 2100, 4000]
    price = [50000, 51000, 52000, 53000, 54000]
    cost = [200, 100, 300, 120, 500]

    df = pd.DataFrame(area, columns=['area'])
    df['price'] = price
    df['cost'] = cost

    df.to_csv(export_title_name("file_name"), index=False)

def pandas_config(url_var1):
    """
    지난 프로젝트 혹은 통계데이터 csv를 github에 저장하고,
    springboot서버의 @Controller의 @GetMapping("/csvlink")의 메서드에 할당된 DB내용을 github link주소를 추가하고 조회할 수 있도록 추가하시오.
    flask에서 springboot를 사용하여 csv파일을 읽어올 수 있도록 함수를 완성하시오
    :param url_var1:
    :return:
    """
    var1 = pd.read_csv(url_var1)
    print(var1)


def export_title_name(var1):
    """
    save csv file name
    :param var1: filename
    :return: date_filename.csv : string
    """
    now = datetime.now()
    str_date = now.strftime('%Y%m%d%H%M%S_')
    return str_date + var1 + ".csv"


def read_url(var1):
    url = "http://localhost:8090/csvlink?csvRequest="+var1
    response = requests.get(url=url)
    return response.text
