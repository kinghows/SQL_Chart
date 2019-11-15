#!/usr/local/bin/python
# coding: utf-8

# SQL Chart V0.1.0
# Export SQL to HTML chart.
# Copyright (C) 2019-2019 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/SQL_Chart

import getopt
import sys
import configparser
from pyecharts import options as opts
from pyecharts.charts import Page,Pie,Bar,Line
from pyecharts.charts import Calendar
from pyecharts.charts import Funnel
from pyecharts.charts import Gauge
from pyecharts.charts import Graph

def f_get_conn(dbinfo,database_type):
    if database_type == "MySQL":
        try:
            conn = MySQLdb.connect(host=dbinfo[0], user=dbinfo[1], passwd=dbinfo[2], port=int(dbinfo[3]))
            return conn
        except MySQLdb.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
    elif database_type == "Oracle":
        try:
            conn = cx_Oracle.connect(dbinfo[1], dbinfo[2], dbinfo[0]+':'+dbinfo[3]+'/'+dbinfo[4])
            return conn
        except cx_Oracle.DatabaseError as msg:
            print(msg)
            sys.exit(1)

def f_get_query_record(conn, query,database_type):
    cursor = conn.cursor()
    if database_type == "MySQL":
        cursor.execute('SET NAMES utf8') 
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
    cursor.execute(query.encode('utf-8'))
    records = cursor.fetchall()
    cursor.close()
    return records

def f_get_query_list(conn, query,database_type):
    cursor = conn.cursor()
    if database_type == "MySQL":
        cursor.execute('SET NAMES utf8') 
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
    cursor.execute(query.encode('utf-8'))
    rows = cursor.fetchall()
    cursor.close()
    strlist=[]
    for row in rows:
        for col in row:
            #strlist.append(str(col).encode('raw_unicode_escape').decode('utf-8')) #linux
            strlist.append(str(col)) #windows
    return strlist

def chart(conn,database_type,chart_type,title,x,y,data,style):
    xlist = f_get_query_list(conn, x, database_type)
    ylist = f_get_query_list(conn, y, database_type)
    datas = f_get_query_record(conn, data,database_type)
    
    if ylist[0] != '0':
        zdict={}
        for i in range(len(ylist)):
            zdict[ylist[i]]=[]

        for row in datas:
            #zdict[row[1].encode('raw_unicode_escape').decode('utf-8')].append(str(row[2])) #linux
            zdict[row[1]].append(str(row[2])) #windows

    if chart_type == 'line':    # 折线图
        line = Line()
        line.set_global_opts(title_opts={"text": title})#{"text": "主标题", "subtext": "副标题"}
        line.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            line.add_yaxis(name, zdict[name],  is_smooth=True) 
        return line
    elif chart_type == 'pie':# 饼图
        pie = Pie()
        pie.set_global_opts(title_opts={"text": title})
        for i in range(len(ylist)):
            name = ylist[i]
            data_pair = list(zip(xlist,zdict[name]))
            pie.add(series_name=name,data_pair=data_pair)
        return pie
    elif chart_type == 'bar': # 柱形图
        bar = Bar()
        bar.set_global_opts(title_opts={"text": title})
        bar.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            bar.add_yaxis(name, zdict[name]) 
        return bar
    elif chart_type == 'calendar': # 日历图
        calendar = Calendar()
        calendar.add("", datas, calendar_opts=opts.CalendarOpts(range_=xlist[0]))
        calendar.set_global_opts(
            title_opts={"text": title},
            visualmap_opts=opts.VisualMapOpts(
            max_=style.setdefault('max_',20000),
            min_=style.setdefault('min_',500),
            orient=style.setdefault('orient',"horizontal"),
            is_piecewise=style.setdefault('is_piecewise',True),
            pos_top=style.setdefault('pos_top',"230px"),
            pos_left=style.setdefault('pos_left',"100px"))
        )
        return calendar
    elif chart_type == 'funnel': # 漏斗图
        funnel = Funnel()
        funnel.set_global_opts(title_opts={"text": title})
        funnel.add("", datas, sort_=style.setdefault('sort_',"descending"),label_opts=opts.LabelOpts(position="inside"))
        return funnel
    elif chart_type == 'gauge': # 仪表盘
        gauge = Gauge()
        gauge.set_global_opts(title_opts={"text": title})
        gauge.add("", datas, title_label_opts=opts.LabelOpts(
            font_size=style.setdefault('font_size', 40), 
            color=style.setdefault('color', "blue"), 
            font_family=style.setdefault('font_family', "Microsoft YaHei")
            ))
        return gauge
    elif chart_type == 'graph': # 关系图
        graph = Graph()
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            nodes.append({"name": row[0], "symbolSize": row[1]})
        links = []
        for row in datas:
            links.append({"source": row[0], "target": row[1]})
        graph.set_global_opts(title_opts={"text": title})
        graph.add("", nodes, links, repulsion=4000)
        return graph

if __name__=="__main__":
    
    dbinfo=["127.0.0.1","root","",3306,"orcl"] #host,user,passwd,port,sid
    config_file="dbset.ini"
    chart_title=""
    chart_count = 0
    save_as = "html"
    database_type = "MySQL"

    opt, args = getopt.getopt(sys.argv[1:], "p:s:")
    for o,v in opt:
        if o == "-p":
            config_file = v
        elif o == "-s":
            save_as = v

    config = configparser.ConfigParser()
    config.read(config_file,encoding="utf-8-sig")
    dbinfo[0] = config.get("database","host")
    dbinfo[1] = config.get("database","user")
    dbinfo[2] = config.get("database","passwd")
    dbinfo[3] = config.get("database", "port")
    chart_title = config.get("chart", "chart_title")
    all_in_one_page = config.get("chart", "all_in_one_page")
    chart_count = int(config.get("chart", "chart_count"))
    database_type = config.get("database", "type")

    if database_type == "MySQL":
        import MySQLdb
        from warnings import filterwarnings
        filterwarnings('ignore', category=MySQLdb.Warning)
    elif database_type == "Oracle":
        import cx_Oracle
        dbinfo[4] = config.get("database", "sid")

    conn = f_get_conn(dbinfo,database_type)
    
    if all_in_one_page =='1':
        page = Page()

    n = 1
    while n <= chart_count:
        title = config.get ( "chart", "title"+str(n))
        chart_type = config.get ( "chart", "chart_type"+str(n))
        x = config.get ( "chart", "x"+str(n))
        y = config.get ( "chart", "y"+str(n))
        data = config.get ( "chart", "data"+str(n))
        strstyle = config.get ( "chart", "style"+str(n))
        style = eval(strstyle)
        if all_in_one_page =='1':
            page.add(chart(conn,database_type,chart_type,title,x,y,data,style))
        else:
            chart(conn,database_type,chart_type,title,x,y,data,style).render(path=title + '.' + save_as)
        n += 1

    if all_in_one_page =='1':
        page.render(path=chart_title + '.' + save_as)

    conn.close()