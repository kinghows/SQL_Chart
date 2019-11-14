# SQL_Chart
Export SQL to HTML chart.  

Python 3.6+

pip install mysqlclient

Oracle need install cx_Oracle

pip install cx_Oracle

pip install pyecharts

pyecharts 1.6+

Edit connect info in dbset.ini [database] part.

Edit you SQL info in dbset.ini [[chart]] part.

example:

chart_title = my_chart1

all_in_one_page = 1

chart_count = n

#---m---------------------------------

titlem = ***

chart_typem = ***

xm =***

ym =***

datam =***

n must <=m

execute:

python sql_chart.py -p dbset.ini -s html

send email:

python SendEmail.py -p emailset.ini -f my_chart1.html,my_chart2.html

use crontab regularly perform sql_chart.sh,auto generate html chart,and send email.

Enjoy it!
