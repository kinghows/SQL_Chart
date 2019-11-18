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


Page().add(*[fn() for fn, _ in C.charts]).render('test.html')