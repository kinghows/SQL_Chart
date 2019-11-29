# SQL_Chart
Export SQL to HTML chart.  

Python 3.6+

pip install mysqlclient

Oracle need install cx_Oracle

pip install cx_Oracle

chart used pyecharts 1.6+

pip install pyecharts

Edit connect info in dbset.ini [database] part.

Edit you SQL info in dbset.ini [[chart]] part.

demo:

you can import chart_demo.sql to mysql,then python sql_chart.py -p dbset.ini -s html

or just look at the results: chart_demo.html

dbset example:

chart_title = chart_demo

all_in_one_page = 1

chart_count = n

#---m---------------------------------

titlem = ***

chart_typem = ***

xm =select x from table

ym =select y from table

datam =select x,y,data from table

n must <=m

execute:

python sql_chart.py -p dbset.ini -s html

send email:

python SendEmail.py -p emailset.ini -f my_chart1.html,my_chart2.html

use crontab regularly perform sql_chart.sh,auto generate html chart,and send email.

Enjoy it!

## 好用的DBA系列，喜欢的打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)
