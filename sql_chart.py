#!/usr/local/bin/python
# coding: utf-8

# SQL Chart V1.0.0
# Export SQL to HTML chart.
# Copyright (C) 2019-2019 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/SQL_Chart

import getopt
import sys
import configparser
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pyecharts.globals import ChartType
from pyecharts.charts import Page
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Calendar
from pyecharts.charts import Funnel
from pyecharts.charts import Gauge
from pyecharts.charts import Graph
from pyecharts.charts import Liquid
from pyecharts.charts import Parallel
from pyecharts.charts import Polar
from pyecharts.charts import Radar
from pyecharts.charts import Sankey
from pyecharts.charts import Sunburst
from pyecharts.charts import ThemeRiver
from pyecharts.charts import WordCloud
from pyecharts.charts import Boxplot
from pyecharts.charts import EffectScatter
from pyecharts.charts import HeatMap
from pyecharts.charts import Kline
from pyecharts.charts import PictorialBar
from pyecharts.charts import Scatter
from pyecharts.charts import Tree
from pyecharts.charts import TreeMap
from pyecharts.charts import Geo
from pyecharts.charts import Map
from pyecharts.charts import Bar3D
from pyecharts.charts import Line3D
from pyecharts.charts import Scatter3D
from pyecharts.charts import Surface3D
from pyecharts.charts import MapGlobe
from pyecharts.charts import Grid
from pyecharts.charts import Tab
from pyecharts.charts import Timeline
from pyecharts.components import Table

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
    
    if ylist[0] != '0' and chart_type != 'graph2' and chart_type != 'graph3'  and chart_type != 'pictorialbar' and chart_type != 'geo_lines' and chart_type != 'bar3d' and chart_type != 'bar3d_stack' and chart_type != 'line3d' and chart_type != 'timeline_map':
        zdict={}
        for i in range(len(ylist)):
            zdict[ylist[i]]=[]

        for row in datas:
            #zdict[row[1].encode('raw_unicode_escape').decode('utf-8')].append(str(row[2])) #linux
            zdict[row[1]].append(str(row[2])) #windows

    if chart_type == 'line':    # 折线图
        c = Line()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
                ),
            )
        c.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            c.add_yaxis(name, zdict[name],
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_=style.setdefault('type_',"max"))]),
                is_smooth=style.setdefault('is_smooth',True),
                label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)),
                areastyle_opts=opts.AreaStyleOpts(opacity=style.setdefault('opacity',0))
                ) 
        return c
    elif chart_type == 'pie':# 饼图
        c = Pie()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        for i in range(len(ylist)):
            name = ylist[i]
            data_pair = list(zip(xlist,zdict[name]))
            c.add(series_name=name,data_pair=data_pair)
        c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        return c
    elif chart_type == 'bar': # 柱形图
        c = Bar()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            c.add_yaxis(name, zdict[name]) 
        return c
    elif chart_type == 'calendar': # 日历图
        c = Calendar()
        c.add("", datas, calendar_opts=opts.CalendarOpts(range_=xlist[0]))
        c.set_global_opts(
            title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                  pos_right=style.setdefault('title_pos_right',None)),
            legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                        pos_left=style.setdefault('legend_pos_left',None),
                                        pos_right=style.setdefault('legend_pos_right',None)),
            visualmap_opts=opts.VisualMapOpts(
            max_=style.setdefault('max_',20000),
            min_=style.setdefault('min_',500),
            orient=style.setdefault('orient',"horizontal"),
            is_piecewise=style.setdefault('is_piecewise',True),
            pos_top=style.setdefault('pos_top',"230px"),
            pos_left=style.setdefault('pos_left',"100px"))
        )
        return c
    elif chart_type == 'funnel': # 漏斗图
        c = Funnel()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add("", datas, sort_=style.setdefault('sort_',"descending"),label_opts=opts.LabelOpts(position=style.setdefault('position',"inside")))
        return c
    elif chart_type == 'gauge': # 仪表盘
        c = Gauge()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add("", datas, title_label_opts=opts.LabelOpts(
            font_size=style.setdefault('font_size', 40), 
            color=style.setdefault('color', "blue"), 
            font_family=style.setdefault('font_family', "Microsoft YaHei")
            ))
        return c
    elif chart_type == 'graph': # 关系图
        c = Graph()
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            nodes.append({"name": row[0], "symbolSize": row[1]})
        links = []
        for row in datas:
            links.append({"source": row[0], "target": row[1]})
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add("", nodes, links, repulsion=style.setdefault('repulsion',4000))
        return c
    elif chart_type == 'graph2': # 关系图2
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            if row[4].decode('utf-8') !='':
                label =eval(row[4].decode('utf-8'))
            nodes.append({"name": row[0].decode('utf-8'), "symbolSize": row[1],"category": row[2].decode('utf-8'),"draggable": row[3].decode('utf-8'),"label": label,"value": row[5]})
        ys = f_get_query_record(conn, y,database_type)
        categories = []
        for row in ys:
            categories.append({"name": row[0]})       
        links = []
        for row in datas:
            links.append({"source": row[0], "target": row[1]})
        c = Graph()
        c.add(
                "",
                nodes,
                links,
                categories,
                repulsion=style.setdefault('repulsion',50),
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
                label_opts=opts.LabelOpts(is_show=style.setdefault('label_opts_is_show',False)),
            )
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None),
                                            is_show=style.setdefault('legend_opts_is_show',False)),
            )
        return c
    elif chart_type == 'graph3': # 关系图3
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            if row[4] !='':
                label =eval(row[4])
            nodes.append({"id": row[0],"name": row[1], "symbolSize": float(row[2]),"category": int(row[3]),"label": label,"value": float(row[5]),"x": float(row[6]),"y": float(row[7])})
        ys = f_get_query_record(conn, y,database_type)
        categories = []
        for row in ys:
            categories.append({"name": row[0]})       
        links = []
        for row in datas:
            links.append({"id": row[0], "source": row[1], "target": row[2]})
        c = Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        c.add(
                "",
                nodes=nodes,
                links=links,
                categories=categories,
                layout=style.setdefault('layout',"circular"),
                is_rotate_label=style.setdefault('is_rotate_label',True),
                linestyle_opts=opts.LineStyleOpts(color=style.setdefault('color',"source"), curve=style.setdefault('curve',0.3)),
                label_opts=opts.LabelOpts(position=style.setdefault('position',"right")),
            )
        c.set_global_opts(
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(orient=style.setdefault('orient',"vertical"),
                                            pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None),
                                            ),
            )
        return c
    elif chart_type == 'graph4': # 关系图4
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            nodes.append({
                "x": float(row[0]),
                "y": float(row[1]),
                "id": row[2],
                "name": row[3], 
                "symbolSize": float(row[4]),
                "itemStyle": eval(row[5])
                })
        links = []
        for row in datas:
            links.append({"source": row[0], "target": row[1]})
        #file=open('a.txt','w')  
        #file.writelines([str(line)+"\n" for line in nodes]);  
        #file.close() 
        c = Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        c.add(
                "",
                nodes=nodes,
                links=links,
                layout=style.setdefault('layout',"none"),
                label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)),
                linestyle_opts=opts.LineStyleOpts(width=style.setdefault('width',0.5), curve=style.setdefault('curve',0.3), opacity=style.setdefault('opacity',0.7)),
            )
        c.set_global_opts(
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None),
                                            ),
            )
        return c
    elif chart_type == 'liquid': # 水球图
        c = Liquid()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add("lq", datas, is_outline_show=style.setdefault('is_outline_show',True))
        return c
    elif chart_type == 'parallel': # 平行坐标系
        xs = f_get_query_record(conn, x,database_type)
        schemas = []
        for row in xs:
            strdata = row[3]
            datalist = strdata.split(",")
            schemas.append({"dim": row[0], "name": row[1], "type_": row[2], "data": datalist})
        c = Parallel()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.add_schema(schemas)
        c.add("parallel", datas)
        return c
    elif chart_type == 'polar': # 极坐标系
        c = Polar()
        c.add("", datas, type_=style.setdefault('type_',"scatter"), label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)))
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'radar': # 雷达图
        xs = f_get_query_record(conn, x,database_type)
        schemas = []
        for row in xs:
            schemas.append({"name": row[0], "max_": row[1], "min_": row[2]})
        c = Radar()
        c.add_schema(schemas)
        v =[]
        name =''
        color=''
        for row in datas:
            if row[0]!=name:
                if len(v)>0:
                    c.add(name, v, color=color)
                    v =[]
                name = row[0]
                color = row[1]
            v.append(row[2:])
        c.add(name, v, color=color)
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)))
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'sankey': # 桑基图
        xs = f_get_query_record(conn, x,database_type)
        nodes = []
        for row in xs:
            nodes.append({"name": row[0]})
        links = []
        for row in datas:
            links.append({"source": row[0], "target": row[1], "value": row[2]})
        c = Sankey()
        c.add(
                "sankey",
                nodes=nodes,
                links=links,
                linestyle_opt=opts.LineStyleOpts(opacity=style.setdefault('opacity',0.2), curve=style.setdefault('curve',0.5), color=style.setdefault('color',"source")),
                label_opts=opts.LabelOpts(position=style.setdefault('position',"right")),
            )
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'sunburst': # 旭日图
        j = []
        for row in datas:
            j.append(eval(row[0]))
        c = Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
        c.add(
            "",
            data_pair=j,
            highlight_policy=style.setdefault('highlight_policy',"ancestor"),
            radius=style.setdefault('radius',[0, "95%"]),
            sort_=style.setdefault('sort_',"null"),
            levels=style.setdefault('levels',[
                {},
                {
                    "r0": "15%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"rotate": "tangential"},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right"}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": {"position": "outside", "padding": 3, "silent": False},
                    "itemStyle": {"borderWidth": 3},
                },
            ],)
            )
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
        return c
    elif chart_type == 'themeriver': # 主题河流图
        c = ThemeRiver()
        c.add(
                xlist,
                datas,
                singleaxis_opts=opts.SingleAxisOpts(type_=style.setdefault('type_',"time"), pos_bottom=style.setdefault('pos_bottom',"10%")),
            )
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'wordcloud': # 词云图
        c = WordCloud()
        c.add("", datas, word_size_range=style.setdefault('word_size_range',[20, 100]))
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'boxpolt': # 箱形图
        c = Boxplot()
        c.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            vn=[]
            for v in zdict[name]:
                vn.append(list(map(int, v.split(","))))
            c.add_yaxis(name, c.prepare_data(vn))
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'effectscatter': # 涟漪特效散点图
        c = EffectScatter()
        c.add_xaxis(xlist)
        c.add_yaxis("", datas)
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'heatmap': # 热力图
        c = HeatMap()
        c.add_xaxis(xlist)
        c.add_yaxis("series0",ylist , datas)
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                visualmap_opts=opts.VisualMapOpts(),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'kline': # K线图
        c = Kline()
        c.add_xaxis(xlist)
        c.add_yaxis("kline", datas,itemstyle_opts=opts.ItemStyleOpts(
                color=style.setdefault('color',"#ec0000"),
                color0=style.setdefault('color0',"#00da3c"),
                border_color=style.setdefault('border_color',"#8A0000"),
                border_color0=style.setdefault('border_color0',"#008F28"),
                ),
                markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="max", value_dim="close")]
                ),
            )
        c.set_global_opts(yaxis_opts=opts.AxisOpts(is_scale=True),
                xaxis_opts=opts.AxisOpts(is_scale=True),
                datazoom_opts=[opts.DataZoomOpts(type_="inside")],
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'pictorialbar': # 象形柱状图
        ys = f_get_query_record(conn, y,database_type)
        symbols = {}
        for row in ys:
            symbols[row[0]]=row[1]

        c = PictorialBar()
        c.add_xaxis(xlist)
        v =[]
        name =''
        i=5
        for row in datas:
            if row[0]!=name:
                if len(v)>0:
                    c.add_yaxis(name, 
                          v,
                          label_opts=opts.LabelOpts(is_show=False),
                          symbol_size=22,
                          symbol_repeat="fixed",
                          symbol_offset=[0, i],
                          is_symbol_clip=True)
                    v =[]
                    i=i-20
                name = row[0]
            v.append({"value": row[2], "symbol": symbols[row[1]]})
        c.add_yaxis(name, 
                          v,
                          label_opts=opts.LabelOpts(is_show=False),
                          symbol_size=22,
                          symbol_repeat="fixed",
                          symbol_offset=[0, i],
                          is_symbol_clip=True)
        c.reversal_axis()
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                xaxis_opts=opts.AxisOpts(is_show=True),
                yaxis_opts=opts.AxisOpts(
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(opacity=0))
                    )    
                )
        return c
    elif chart_type == 'scatter': # 散点图
        c = Scatter()
        c.add_xaxis(xlist)
        v =[]
        name =''
        for row in datas:
            if row[0]!=name:
                if len(v)>0:
                    c.add_yaxis(name, v)
                    v =[]
                name = row[0]
            v.append(row[2])
        c.add_yaxis(name, v)
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'overlap': # 层叠多图
        v1 = []
        v2 = []
        v3 = []
        for row in datas:
            v1.append(row[0])
            v2.append(row[1])
            v3.append(row[2])
        c = Bar()
        c.add_xaxis(xlist)
        c.add_yaxis("蒸发量", v1)
        c.add_yaxis("降水量", v2)
        c.extend_axis(
                yaxis=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
                )
            )
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml")
                ),
            )
        line = Line().add_xaxis(xlist).add_yaxis("平均温度", v3, yaxis_index=1)
        c.overlap(line)
        return c
    elif chart_type == 'tree': # 树图
        j = []
        for row in datas:
            j.append(eval(row[0]))
        c = Tree()
        c.add("", j, collapse_interval=2, orient=style.setdefault('orient',"LR"),label_opts=opts.LabelOpts(
                position=style.setdefault('position',None),
                horizontal_align=style.setdefault('horizontal_align',None),
                vertical_align=style.setdefault('vertical_align',None),
                rotate=style.setdefault('rotate',None)
                )
            )
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'treemap': # 矩形树图
        j = []
        for row in datas:
            j.append(eval(row[0]))
        c = TreeMap()
        c.add(xlist[0], j[0])
        c.set_global_opts(title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'geo': # 地理坐标系
        c = Geo()
        c.add_schema(maptype=xlist[0])
        if style.setdefault('ChartType','None')=='None':
            c.add(xlist[0],datas)
        elif style.setdefault('ChartType','None')=='HEATMAP': 
            c.add(xlist[0],datas,type_=ChartType.HEATMAP)  
        elif style.setdefault('ChartType','None')=='EFFECT_SCATTER': 
            c.add(xlist[0],datas,type_=ChartType.EFFECT_SCATTER)
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        c.set_global_opts(visualmap_opts=opts.VisualMapOpts(is_piecewise=style.setdefault('is_piecewise',None)),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'geo_lines': # 地理坐标系3
        ys = f_get_query_record(conn, y,database_type)
        c = Geo()
        c.add_schema(maptype=xlist[0],
            itemstyle_opts=opts.ItemStyleOpts(color=style.setdefault('back_color',"#323c48"), border_color=style.setdefault('border_color',"#111")))
        c.add(xlist[0],datas,type_=ChartType.EFFECT_SCATTER,color=style.setdefault('dot_color',"red"))
        c.add(
            xlist[0],
            ys,
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=style.setdefault('symbol_size',6), color=style.setdefault('line_color',"blue")
            ),
            linestyle_opts=opts.LineStyleOpts(curve=style.setdefault('curve',0.2)),
        )
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        c.set_global_opts(
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'map': # 地图
        c = Map()
        c.add(xlist[1],datas, xlist[0])
        c.set_series_opts(label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)))
        if style.setdefault('max_',0) ==0 :
            c.set_global_opts(
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        else:
            c.set_global_opts(
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                visualmap_opts=opts.VisualMapOpts(max_=style.setdefault('max_',200),is_piecewise=style.setdefault('is_piecewise',True))
                )
        return c
    elif chart_type == 'bar3d': # 3D柱状图
        c =  Bar3D()
        c.add(
            "",
            [[d[1], d[0], d[2]] for d in datas],
            xaxis3d_opts=opts.Axis3DOpts(xlist, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(ylist, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=style.setdefault('max_',80)),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'bar3d_stack': # 堆叠柱状图
        c = Bar3D()
        for _ in range(7):
            c.add(
                "",
                datas,
                shading="lambert",
                xaxis3d_opts=opts.Axis3DOpts(data=xlist, type_="value"),
                yaxis3d_opts=opts.Axis3DOpts(data=ylist, type_="value"),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=style.setdefault('max_',80)),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        c.set_series_opts(**{"stack": "stack"})
        return c
    elif chart_type == 'line3d': # 3D折线图
        c = Line3D()
        c.add(
                "",
                datas,
                xaxis3d_opts=opts.Axis3DOpts(xlist, type_="value"),
                yaxis3d_opts=opts.Axis3DOpts(ylist, type_="value"),
                grid3d_opts=opts.Grid3DOpts(width=style.setdefault('width',100), 
                                            height=style.setdefault('height',100), 
                                            depth=style.setdefault('depth',100),
                                            is_rotate=style.setdefault('is_rotate',False)),
            )
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                    max_=style.setdefault('max_',30), min_=style.setdefault('min_',0), range_color=style.setdefault('range_color',[]).split(',')
                ),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'scatter3d': # 3D散点图
        c = Scatter3D()
        c.add(xlist[0], datas)
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(range_color=style.setdefault('range_color',[]).split(',')),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'surface3d': # 3D曲面图
        c = Surface3D()
        c.add(
                xlist[0],
                datas,
                xaxis3d_opts=opts.Axis3DOpts(type_="value"),
                yaxis3d_opts=opts.Axis3DOpts(type_="value"),
                grid3d_opts=opts.Grid3DOpts(width=style.setdefault('width',100), 
                                            height=style.setdefault('height',100), 
                                            depth=style.setdefault('depth',100)
                ),
            )
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                   max_=style.setdefault('max_',3), min_=style.setdefault('min_',-3), range_color=style.setdefault('range_color',[]).split(',')
                ),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'mapglobe': # 地球地图
        high = max([x for _, x in datas])
        low = min([x for _, x in datas])
        c = MapGlobe()
        c.add_schema()
        c.add(
                maptype=style.setdefault('maptype',"world"),
                series_name=xlist[0],
                data_pair=datas,
                is_map_symbol_show=style.setdefault('is_map_symbol_show',False),
                label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)),
            )
        c.set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                min_=low,
                max_=high,
                range_text=["max", "min"],
                is_calculable=style.setdefault('is_calculable',True),
                range_color=style.setdefault('range_color',["lightskyblue", "yellow", "orangered"]).split(',')),
                title_opts=opts.TitleOpts(title=title,pos_top=style.setdefault('title_pos_top',None),
                                                      pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
        return c
    elif chart_type == 'kline_profession': # 多图联动
        def calculate_ma(day_count: int, d):
            result: List[Union[float, str]] = []
            for i in range(len(d)):
                if i < day_count:
                    result.append("-")
                    continue
                sum_total = 0.0
                for j in range(day_count):
                    sum_total += float(d[i - j][1])
                result.append(abs(float("%.3f" % (sum_total / day_count))))
            return result

        kline = Kline()
        kline.add_xaxis(xaxis_data=xlist)
        kline.add_yaxis(series_name="Dow-Jones index",y_axis=datas,itemstyle_opts=opts.ItemStyleOpts(color=style.setdefault('color',"#ec0000"), color0=style.setdefault('color0',"#00da3c")))
        kline.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle="MA(5,10,30,60)",),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(is_scale=True,splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1))),
            legend_opts=opts.LegendOpts(is_show=False, pos_bottom=10, pos_left="center"),
            datazoom_opts=[opts.DataZoomOpts(is_show=False,type_="inside",xaxis_index=[0, 1],range_start=0,range_end=100,),
                opts.DataZoomOpts(is_show=True,xaxis_index=[0, 1],type_="slider",pos_top="90%",range_start=0,range_end=100,)],
            tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type="cross",background_color="rgba(245, 245, 245, 0.8)",
                border_width=1,border_color="#ccc",textstyle_opts=opts.TextStyleOpts(color="#000")),
            visualmap_opts=opts.VisualMapOpts(is_show=False,dimension=2,series_index=5,is_piecewise=True,
                pieces=[{"value": 1, "color": "#ec0000"},{"value": -1, "color": "#00da3c"}]),
            axispointer_opts=opts.AxisPointerOpts(is_show=True,link=[{"xAxisIndex": "all"}],label=opts.LabelOpts(background_color="#777")),
            brush_opts=opts.BrushOpts(x_axis_index="all",brush_link="all",out_of_brush={"colorAlpha": 0.1},brush_type="lineX")
        )

        line = Line()
        line.add_xaxis(xaxis_data=xlist)
        line.add_yaxis(series_name="MA5",y_axis=calculate_ma(day_count=5, d=datas),is_smooth=True,is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
        line.add_yaxis(series_name="MA10",y_axis=calculate_ma(day_count=10, d=datas),is_smooth=True,is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
        line.add_yaxis(series_name="MA30",y_axis=calculate_ma(day_count=30, d=datas),is_smooth=True,is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
        line.add_yaxis(series_name="MA60",y_axis=calculate_ma(day_count=60, d=datas),is_smooth=True,is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),label_opts=opts.LabelOpts(is_show=False))
        line.set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"))

        bar = Bar()
        bar.add_xaxis(xaxis_data=xlist)
        bar.add_yaxis(series_name="Volume",yaxis_data=[[i, datas[i][3], 1 if datas[i][0] > datas[i][1] else -1] for i in range(len(datas))],
            xaxis_index=1,yaxis_index=1,label_opts=opts.LabelOpts(is_show=False))
        bar.set_global_opts(xaxis_opts=opts.AxisOpts(type_="category",is_scale=True,grid_index=1,boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),axislabel_opts=opts.LabelOpts(is_show=False),
                split_number=20,min_="dataMin",max_="dataMax",),
            yaxis_opts=opts.AxisOpts(grid_index=1,is_scale=True,split_number=2,
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False)),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        # Kline And Line
        overlap_kline_line = kline.overlap(line)

        # Grid Overlap + Bar
        c = Grid()
        c.add(overlap_kline_line,grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height="50%"))
        c.add(bar,grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top="70%", height="16%"))
        return c
    elif chart_type == 'table': # 表格
        c = Table()
        c.add(xlist, datas)
        c.set_global_opts(title_opts=opts.ComponentTitleOpts(title=title))
        return c
    elif chart_type == 'timeline_bar': # 时间线轮播柱状图
        c = Timeline()
        for i in ylist:
            b = Bar()
            b.add_xaxis(xlist)
            b.add_yaxis(i, zdict[i]) 
            b.set_global_opts(title_opts=opts.TitleOpts("{}".format(i),pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
            c.add(b, "{}".format(i))
        return c
    elif chart_type == 'timeline_pie': # 时间线轮播饼图
        c = Timeline()
        for i in ylist:
            b = Pie()
            data_pair = list(zip(xlist,zdict[i]))
            b.add(series_name=i,data_pair=data_pair)
            b.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            b.set_global_opts(title_opts=opts.TitleOpts("{}".format(i),pos_top=style.setdefault('title_pos_top',None),
                                                                pos_right=style.setdefault('title_pos_right',None)),
                legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                            pos_left=style.setdefault('legend_pos_left',None),
                                            pos_right=style.setdefault('legend_pos_right',None)),
                )
            c.add(b, "{}".format(i))
        return c
    elif chart_type == 'timeline_map': # 时间线轮播地图
        zdict={}
        for i in range(len(ylist)):
            zdict[ylist[i]]=[]

        for row in datas:
            row=list(row)
            i=row[0]
            del row[0]
            zdict[i].append(row)
        c = Timeline()
        for i in ylist:
            b = Map()
            b.add(xlist[1],zdict[i], xlist[0])
            b.set_series_opts(label_opts=opts.LabelOpts(is_show=style.setdefault('is_show',False)))
            if style.setdefault('max_',0) ==0 :
                b.set_global_opts(
                    title_opts=opts.TitleOpts("{}".format(i),pos_top=style.setdefault('title_pos_top',None),
                                                             pos_right=style.setdefault('title_pos_right',None)),
                    legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                                pos_left=style.setdefault('legend_pos_left',None),
                                                pos_right=style.setdefault('legend_pos_right',None)),
                    )
            else: 
                b.set_global_opts(
                    title_opts=opts.TitleOpts("{}".format(i),pos_top=style.setdefault('title_pos_top',None),
                                                             pos_right=style.setdefault('title_pos_right',None)),
                    legend_opts=opts.LegendOpts(pos_top=style.setdefault('legend_pos_top',None),
                                                pos_left=style.setdefault('legend_pos_left',None),
                                                pos_right=style.setdefault('legend_pos_right',None)),
                    visualmap_opts=opts.VisualMapOpts(max_=style.setdefault('max_',200),is_piecewise=style.setdefault('is_piecewise',True))
                    )
            c.add(b, "{}".format(i))
        return c

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
    mutli_chart_type = config.get("chart", "mutli_chart_type")
    all_in_one_page = config.get("chart", "all_in_one_page")
    draggable = config.get("chart", "draggable")
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
    
    if mutli_chart_type=='page':
        if all_in_one_page =='ON':
            if draggable=='ON':
                page = Page(layout=Page.DraggablePageLayout)
            else:
                page = Page()
    else:
        page = Tab()

    n = 0
    while n < chart_count:
        n += 1
        switch = config.get ( "chart", "switch"+str(n))
        if switch=='ON':
            title = config.get ( "chart", "title"+str(n))
            chart_type = config.get ( "chart", "chart_type"+str(n))
            if chart_type[0:4] != 'grid':
                x = config.get ( "chart", "x"+str(n))
                y = config.get ( "chart", "y"+str(n))
                data = config.get ( "chart", "data"+str(n))
                strstyle = config.get ( "chart", "style"+str(n))
                style = eval(strstyle)
                if all_in_one_page =='ON':
                    if mutli_chart_type=='page':
                        page.add(chart(conn,database_type,chart_type,title,x,y,data,style))
                    else:
                        page.add(chart(conn,database_type,chart_type,title,x,y,data,style),title)
                else:
                    chart(conn,database_type,chart_type,title,x,y,data,style).render(path=title + '.' + save_as)
            else:
                grid = Grid()
                chart_count_grid = int(config.get("chart", "chart_count"+str(n)))
                grid_chart_type = chart_type
                m = 0
                while m < chart_count_grid:
                    m += 1
                    title = config.get ( "chart", "title"+str(n)+'_'+str(m))
                    chart_type = config.get ( "chart", "chart_type"+str(n)+'_'+str(m))
                    x = config.get ( "chart", "x"+str(n)+'_'+str(m))
                    y = config.get ( "chart", "y"+str(n)+'_'+str(m))
                    data = config.get ( "chart", "data"+str(n)+'_'+str(m))
                    strstyle = config.get ( "chart", "style"+str(n)+'_'+str(m))
                    style = eval(strstyle)
                    c = chart(conn,database_type,chart_type,title,x,y,data,style)
                    if grid_chart_type == 'grid_vertical':
                        if m==1:
                            grid.add(c, grid_opts=opts.GridOpts(pos_bottom=style.setdefault('grid_pos_bottom',"60%")))
                        else:
                            grid.add(c, grid_opts=opts.GridOpts(pos_top=style.setdefault('grid_pos_top',"60%")))
                    else:
                        if m==1:
                            grid.add(c, grid_opts=opts.GridOpts(pos_left=style.setdefault('grid_pos_left',"55%")))
                        else:
                            grid.add(c, grid_opts=opts.GridOpts(pos_right=style.setdefault('grid_pos_right',"55%")))

                if all_in_one_page =='ON':
                    page.add(grid)
                else:
                    grid.render(path=title + '.' + save_as)

    if all_in_one_page =='ON':
        page.render(path=chart_title + '.' + save_as)

    conn.close()
