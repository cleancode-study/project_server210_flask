# conda install pymysql

import pymysql

db = pymysql.connect(host='svc.gksl2.cloudtype.app', user='root', db='studydb', password='1234', charset='utf8', port=32419)
curs = db.cursor()

# sql = "select * from project3db";
#
# curs.execute(sql)
#
# rows = curs.fetchall()
# print(rows)
#
# db.commit()
# db.close()

# ----------

sql = '''insert into covid19noti (id, continent_eng_nm, sfty_notice_id) values (30,'bb','cc')
'''

curs.execute(sql)

sql = "select * from covid19noti";
curs.execute(sql)

rows = curs.fetchall()
print(rows)

db.commit()
db.close()