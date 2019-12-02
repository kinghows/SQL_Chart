import datetime
import random
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Calendar
from pyecharts.charts import Page
from pyecharts.faker import Collector
from pyecharts.charts import Funnel
from pyecharts.charts import Gauge
import json
import os
from pyecharts.charts import Graph
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
from pyecharts.charts import Parallel





C = Collector()

@C.funcs
def calendar_base() -> Calendar:
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    c = (
        Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017"),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c

@C.funcs
def funnel_label_inside() -> Funnel:

    a=[list(z) for z in zip(Faker.choose(), Faker.values())]
    c = (
        Funnel()
        .add(
            "商品",
            a,
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Label（inside)"))
    )
    return c

@C.funcs
def gauge_label_title_setting() -> Gauge:
    c = (
        Gauge()
        .add(
            "",
            [("完成率", 66.6)],
            title_label_opts=opts.LabelOpts(
                font_size=40, color="blue", font_family="Microsoft YaHei"
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-改变轮盘内的字体"))
    )
    return c

@C.funcs
def graph_base() -> Graph:
    nodes = [
        {"name": "结点1", "symbolSize": 10},
        {"name": "结点2", "symbolSize": 20},
        {"name": "结点3", "symbolSize": 30},
        {"name": "结点4", "symbolSize": 40},
        {"name": "结点5", "symbolSize": 50},
        {"name": "结点6", "symbolSize": 40},
        {"name": "结点7", "symbolSize": 30},
        {"name": "结点8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
    )
    return c

@C.funcs
def graph_weibo() -> Graph:
    with open("weibo.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes, links, categories, cont, mid, userl = j
    c = (
        Graph()
        .add(
            "",
            nodes,
            links,
            categories,
            repulsion=50,
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
        )
    )
    return c
    
@C.funcs
def graph_les_miserables():
    with open("les-miserables.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes = j["nodes"]
        links = j["links"]
        categories = j["categories"]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=links,
            categories=categories,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            label_opts=opts.LabelOpts(position="right"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_left="2%", pos_top="20%"
            ),
        )
    )
    return c

@C.funcs
def graph_npm_dependencies() -> Graph:
    with open("npmdepgraph.json", "r", encoding="utf-8") as f:
        j = json.load(f)
    nodes = [
        {
            "x": node["x"],
            "y": node["y"],
            "id": node["id"],
            "name": node["label"],
            "symbolSize": node["size"],
            "itemStyle": {"normal": {"color": node["color"]}},
        }
        for node in j["nodes"]
    ]

    edges = [
        {"source": edge["sourceID"], "target": edge["targetID"]} for edge in j["edges"]
    ]

    c = (
        Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            nodes=nodes,
            links=edges,
            layout="none",
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-NPM Dependencies"))
    )
    return c

@C.funcs
def liquid_base() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.6, 0.7])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    )
    return c

@C.funcs
def liquid_data_precision() -> Liquid:
    c = (
        Liquid()
        .add(
            "lq",
            [0.3254],
            label_opts=opts.LabelOpts(
                font_size=50,
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-数据精度"))
    )
    return c

@C.funcs
def parallel_category() -> Parallel:
    data = [
        [1, 91, 45, 125, 0.82, 34, 23, "良"],
        [2, 65, 27, 78, 0.86, 45, 29, "良"],
        [3, 83, 60, 84, 1.09, 73, 27, "良"],
        [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
        [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
        [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [8, 89, 65, 78, 0.86, 51, 26, "良"],
        [9, 53, 33, 47, 0.64, 50, 17, "良"],
        [10, 80, 55, 80, 1.01, 75, 24, "良"],
        [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
        [12, 99, 71, 142, 1.1, 62, 42, "良"],
        [13, 95, 69, 130, 1.28, 74, 50, "良"],
        [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"],
    ]
    schemas = [ {"dim": 0, "name": "data","type_":"","data":[]},
                {"dim": 1, "name": "AQI","type_":"","data":[]},
                {"dim": 2, "name": "PM2.5","type_":"","data":[]},
                {"dim": 3, "name": "PM10","type_":"","data":[]},
                {"dim": 4, "name": "CO","type_":"","data":[]},
                {"dim": 5, "name": "NO2","type_":"","data":[]},
                {"dim": 6, "name": "CO2","type_":"","data":[]},
                {"dim": 7, "name": "等级","type_":"category","data":["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"]}
            ]
    c = (
        Parallel()
        .add_schema(
                 [
                opts.ParallelAxisOpts(dim=0, name="data",type_="",data=[]),
                opts.ParallelAxisOpts(dim=1, name="AQI",type_="",data=[]),
                opts.ParallelAxisOpts(dim=2, name="PM2.5",type_="",data=[]),
                opts.ParallelAxisOpts(dim=3, name="PM10",type_="",data=[]),
                opts.ParallelAxisOpts(dim=4, name="CO",type_="",data=[]),
                opts.ParallelAxisOpts(dim=5, name="NO2",type_="",data=[]),
                opts.ParallelAxisOpts(dim=6, name="CO2",type_="",data=[]),
                opts.ParallelAxisOpts(dim=7, name="等级",type_="category",data=["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"])
                 ]
        )
        .add("parallel", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Parallel-Category"))
    )
    
    return c











Page().add(*[fn() for fn, _ in C.charts]).render('test.html')