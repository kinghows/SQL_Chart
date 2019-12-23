# SQL_Chart
Export SQL to HTML chart.  

Python 3.6+

pip install mysqlclient

Oracle need install cx_Oracle

pip install cx_Oracle

chart used pyecharts 1.6+

pip install pyecharts

### save as png:

### windows:
pip install snapshot-pyppeteer

pyppeteer-install

### windows,linux:

pip install snapshot-phantomjs

windows:

https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip

linux:

wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

tar -xjvf phantomjs-2.1.1-linux-x86_64.tar.bz2

ln -s /root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs

yum install fontconfig freetype2


### chart_demo.html: 

chart effects demonstration.

### dbset.ini: 

database connect info & SQL info.

### chart_demo.sql: 

demo database backup file.

### execute:

python sql_chart.py -p dbset.ini -s html

python sql_chart.py -p dbset.ini -s png

### send email:

python SendEmail.py -p emailset.ini -f my_chart1.html,my_chart2.html

use crontab regularly perform sql_chart.sh,auto generate html chart,and send email.

Enjoy it!

中文处理Linux需要encode，decode：

88行：

cols.append(str(col).encode('raw_unicode_escape').decode('utf-8')) #linux

#cols.append(str(col)) #windows

105行：

strlist.append(str(col).encode('raw_unicode_escape').decode('utf-8')) #linux

#strlist.append(str(col)) #windows

地理坐标系pyecharts在Linux上有BUG，请设置switch = OFF

## 好用的DBA系列，喜欢的请打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)
