# SQL_Chart
Export SQL to HTML chart.  

Python 3.6+

pip install mysqlclient

Oracle need install cx_Oracle

pip install cx_Oracle

chart used pyecharts 1.6+

pip install pyecharts

##chart_demo.html: more than 40 chart effects demonstration.

##dbset.ini: database connect info & SQL info.

##chart_demo.sql: demo database backup file.

##execute:

python sql_chart.py -p dbset.ini -s html

##send email:

python SendEmail.py -p emailset.ini -f my_chart1.html,my_chart2.html

use crontab regularly perform sql_chart.sh,auto generate html chart,and send email.

Enjoy it!

## 好用的DBA系列，喜欢的打颗星：

- [MySQL_Watcher：数据库性能指标的HTML监控报告](https://github.com/kinghows/MySQL_Watcher)

- [SQL_Report：自定义SQL生成HTML报告](https://github.com/kinghows/SQL_Report)

- [SQL_Chart：自定义SQL生成HTML图表](https://github.com/kinghows/SQL_Chart)
