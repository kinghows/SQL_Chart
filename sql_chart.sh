#!/bin/sh
report_base=/root/report
cd $report_base
/usr/local/bin/python3 $report_base/sql_chart.py -p $report_base/dbset.ini
/usr/local/bin/python3 $report_base/SendEmail.py -p $report_base/emailset.ini -f $report_base/chart_demo.html