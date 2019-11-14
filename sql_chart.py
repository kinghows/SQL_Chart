#!/usr/local/bin/python
# coding: utf-8

# SQL Chart V0.1.0
# Export SQL to HTML chart.
# Copyright (C) 2019-2019 Kinghow - Kinghow@hotmail.com
# Git repository available at https://github.com/kinghows/SQL_Chart

import getopt
import sys
import configparser
import time
from pyecharts.charts  import Page,Pie, EffectScatter, Bar, Line,Scatter,Funnel, Gauge, Graph,Liquid, Polar, Radar,WordCloud
from pyecharts import options as opts
from snapshot_selenium import snapshot as driver
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType

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
            strlist.append(str(col).encode('raw_unicode_escape').decode('utf-8'))
    return strlist

def chart(conn,database_type,chart_type,title,x,y,data):
    xlist = f_get_query_list(conn, x, database_type)
    ylist = f_get_query_list(conn, y, database_type)
    datas = f_get_query_record(conn, data,database_type)
    
    zdict={}
    for i in range(len(ylist)):
        zdict[ylist[i]]=[]

    for row in datas:
        zdict[row[1].encode('raw_unicode_escape').decode('utf-8')].append(str(row[2]))
    
    if chart_type == 'line':    # 普通折线图
        line = Line()
        line.set_global_opts(title_opts={"text": title})#{"text": "主标题", "subtext": "副标题"}
        line.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            line.add_yaxis(name, zdict[name],  is_smooth=True) 
        return line
    elif chart_type == 'line_stair': # 阶梯折线图
        line = Line()
        line.set_global_opts(title_opts={"text": title})
        line.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            line.add_yaxis(name, zdict[name],is_step=True, is_label_show=True) 
        return line
    elif chart_type == 'line_area': # 面积折线图
        line = Line()
        line.set_global_opts(title_opts={"text": title})
        line.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            line.add_yaxis(name, zdict[name],is_fill=True, area_color='#a3aed5', area_opacity=0.3, is_smooth=True) 
        return line
    elif chart_type == 'bar': # 柱形图
        bar = Bar()
        bar.set_global_opts(title_opts={"text": title})
        bar.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            bar.add_yaxis(name, zdict[name]) 
        return bar
    elif chart_type == 'bar_label': # 显示标记线和标记点
        bar = Bar()
        bar.set_global_opts(title_opts={"text": title})
        bar.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            bar.add_yaxis(name, zdict[name], mark_point=['min', 'max']) # mark_point=['avgrage']
        return bar
    elif chart_type == 'bar_muti_label':  # 多标记柱形图
        attr =["{}月".format(i) for i in range(1, 13)]
        v1 =[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
        v2 =[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
        bar =Bar(title)
        bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
        bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
        bar.render(path=filename)
    elif chart_type == 'bar_h': # 水平显示
        bar = Bar()
        bar.set_global_opts(title_opts={"text": title})
        bar.add_xaxis(xlist)
        for i in range(len(ylist)):
            name = ylist[i]
            bar.add_yaxis(name, zdict[name], is_convert=True) # mark_point=['avgrage']
        return bar
    elif chart_type == 'bar_line':# 柱形图-折线图
        att = ['A', 'B', 'C', 'D', 'E', 'F']
        v3 = [10, 20, 30, 40, 50, 60]
        v4 = [38, 28, 58, 48, 78, 68]
        bar = Bar(title)
        bar.add('bar', att, v3)
        line = Line()
        line.add('line', att, v4)
        overlap = Overlap()
        overlap.add(bar)
        overlap.add(line)
        overlap.render(path=filename)
    elif chart_type == 'pie':# 饼图
        pie = Pie()
        pie.set_global_opts(title_opts={"text": title})
        for i in range(len(ylist)):
            name = ylist[i]
            data_pair = list(zip(xlist,zdict[name]))
            pie.add(series_name=name,data_pair=data_pair)
        return pie
    elif chart_type == 'pie_rose':  # 玫瑰饼图
        pie = Pie(title, title_pos='center', width=900)
        pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
        pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
        pie.render(path=filename)
    elif chart_type == 'pie_muti':  # 多个饼图
        pie =Pie(title, "数据来着豆瓣", title_pos='center')
        pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, )
        pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
        pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
        pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
        pie.show_config()
        pie.render(path=filename)
    elif chart_type == 'scatter':  # 散点图
        scatter =Scatter(title)
        scatter.add("A", v1, v2)
        scatter.add("B", v1[::-1], v2)
        #scatter.show_config()
        scatter.render(path=filename)
    elif chart_type == 'scatter_print':  # 散点打印Pyecharts字体 白底图片
        scatter =Scatter(title)
        v1, v2 = scatter.draw("./data/two.jpg")
        scatter.add("pyecharts", v1, v2, is_random=True)
        scatter.render(path=filename)
    elif chart_type == 'effect_scatter':  # 动态散点图
        es =EffectScatter(title)
        # v1 x坐标 v2 y坐标
        es.add("商家", v1, v2)
        es.render(path=filename)
    elif chart_type == 'effect_scatter_muti':  # 动态散点图各种图形
        es = EffectScatter(title)
        es.add("", [10], [10], symbol_size=20, effect_scale=3.5,  effect_period=3, symbol="pin")
        es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
        es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
        es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
        es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
        es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
        es.render(path = filename)
    elif chart_type == 'gauge':  # 仪表盘
        gauge = Gauge(title)
        gauge.add('业务指标', '完成率', 66.66)
        gauge.render(path=filename)
    elif chart_type == 'funnel':  # 漏斗图
        funnel = Funnel(title)
        funnel.add('商品', attr, v1, is_label_show=True, label_pos='inside', label_text_color="#fff")
        funnel.render(path=filename)
    elif chart_type == 'graph':  # 关系图-环形布局示例        
        nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30}, {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 50}, {"name": "结点6", "symbolSize": 40}, {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
        links =[]
        for i in nodes:
            for j in nodes:
                links.append({"source": i.get('name'), "target": j.get('name')})
        print(links)
        print(nodes)
        graph =Graph(title)
        graph.add("", nodes, links, is_label_show=True, repulsion=8000,     layout='circular', label_text_color=None)
        graph.render(path=filename)
    elif chart_type == 'liquid':  # 水球图
        liquid =Liquid(title)
        liquid.add("Liquid", [0.6])
        liquid.render(path=filename)
    elif chart_type == 'liquid_circular':  # 圆形水球
        liquid =Liquid(title)
        liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
        liquid.render(path=filename)
    elif chart_type == 'liquid_diamond':  # 菱形水球
        liquid3 =Liquid(title)
        liquid3.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
        liquid3.render(path=filename)
    elif chart_type == 'polar':  # 极坐标-堆叠柱状图
        radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        polar =Polar(title, width=1200, height=600)
        polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
        polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
        polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
        polar.render(path=filename)
    elif chart_type == 'radar':  # 雷达图
        schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
        v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
        v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
        radar =Radar(title)
        radar.config(schema)
        radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
        radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
        radar.render(path=filename)
    elif chart_type == 'wordcloud_Weight':  # 权重词云
        name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
        value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
        wordcloud =WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, word_size_range=[20, 100])
        wordcloud.render(path=filename)
    elif chart_type == 'wordcloud_deformation':  # 变形词云
        wordcloud =WordCloud(width=1300, height=620)
        wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
        wordcloud.render(path=filename)
    elif chart_type == 'wordcloud_chinese':  # 中文词云
        words = ['好看', '不错', '人性', '可以', '值得', '真的', '一部', '感觉', '喜欢', '一般', '演技', '还是',
           '剧情', '一出', '有点', '出好', '好戏', '不是', '没有', '非常', '哈哈', '喜剧', '就是', '一个',
           '现实', '什么', '支持', '还行', '但是', '很多', '觉得', '搞笑', '值得一看', '故事', '看好',
           '这部', '哈哈哈', '失望', '最后', '导演', '自己', '演员', '看完', '社会', '特别', '看到', '不好',
           '比较', '表达', '那么', '作品', '个人', '东西', '思考', '这个', '第一', '不过', '情节',
           '哈哈哈哈', '意思', '一直', '推荐', '一般般', '时候', '开始', '般般', '片子', '知道', '处女',
           '期待', '很棒', '影院', '深度', '反应', '无聊', '可能', '一些', '精彩', '爱情', '这么', '希望',
           '一点', '不知', '有些', '还好', '恐怖', '看着', '没看', '还有', '观看', '后面', '真实', '因为',
           '如果', '出来', '部分', '确实', '我们', '意义', '深刻']
        new_worlds = " ".join(words)
        coloring = np.array(Image.open("huangbo.jpg"))
        # simkai.ttf 必填项 识别中文的字体，例：simkai.ttf，
        my_wordcloud = WordCloud(background_color="white", max_words=800,
                     mask=coloring, max_font_size=120, random_state=30, scale=2,font_path="simkai.ttf").generate(new_worlds)
        image_colors = ImageColorGenerator(coloring)
        plt.imshow(my_wordcloud.recolor(color_func=image_colors))
        plt.imshow(my_wordcloud)
        plt.axis("off")
        plt.show()
        my_wordcloud.to_file(filename)
        
if __name__=="__main__":
    dbinfo=["127.0.0.1","root","",3306,"orcl"] #host,user,passwd,port,sid
    config_file="chart.ini"
    chart_title=""
    chart_count = 0
    save_as = "html"
    database_type = "MySQL"

    opts, args = getopt.getopt(sys.argv[1:], "p:s:")
    for o,v in opts:
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
        if all_in_one_page =='1':
            page.add(chart(conn,database_type,chart_type,title,x,y,data))
        else:
            chart(conn,database_type,chart_type,title,x,y,data).render(path=title + '.' + save_as)
        n += 1

    if all_in_one_page =='1':
        page.render(path=chart_title + '.' + save_as)

    conn.close()
