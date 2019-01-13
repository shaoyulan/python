import sqlite3, hashlib, ast, os, requests
from bs4 import BeautifulSoup
import datetime
url = ("http://datacenter.taichung.gov.tw/swagger/OpenData/"
	   "5f89a604-73bd-4470-9c68-4ecf2e2ca708")
#路徑變數
txt_old_md5 = '2019_01_12_old_md5.txt'             
txt_update_status = '2019_01_12_update_status.txt'
html = requests.get(url).text.encode('utf-8-sig')

md5 = hashlib.md5(html).hexdigest()
old_md5 = ""

if os.path.exists(txt_old_md5):
	with open(txt_old_md5,'r') as f:
		old_md5 = f.read()

with open(txt_old_md5,'w') as f:
	f.write(md5)

#使用datetime 裡面的datetime物件中的now方法
localtime = (datetime.datetime.now()).isoformat()
if old_md5 != md5:
	with open(txt_update_status,'a') as f:
		f.write('網站已更新'+localtime+'\n')
else:
	with open(txt_update_status,'a') as f:
		f.write('無任何更新'+localtime+'\n')
