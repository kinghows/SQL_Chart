import getopt
import sys
import configparser
import json
import os

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

if __name__=="__main__":
    
    dbinfo=["127.0.0.1","root","",3306,"orcl"] #host,user,passwd,port,sid
    config_file="dbset.ini"
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
    database_type = config.get("database", "type")

    if database_type == "MySQL":
        import MySQLdb
        from warnings import filterwarnings
        filterwarnings('ignore', category=MySQLdb.Warning)
    elif database_type == "Oracle":
        import cx_Oracle
        dbinfo[4] = config.get("database", "sid")

    conn = f_get_conn(dbinfo,database_type)
    cursor = conn.cursor()
    if database_type == "MySQL":
        cursor.execute('SET NAMES utf8') 
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
    with open("les-miserables.json", "r", encoding="utf-8") as f:
        j = json.load(f)
        nodes = j["nodes"]
        links = j["links"]
        categories = j["categories"]
    for row in nodes:
        id = row['id']
        name = row['name']
        symbolsize = str(row['symbolSize'])
        category = str(row['category'])
        x = str(row['x'])
        y = str(row['y'])
        label = str(row.setdefault('label', ''))
        value = str(row['value'])
        query ='insert into chart_demo.t_les_miserables_nodes(id,name,symbolsize,category,label,value,x,y) values ("'+id+'","'+name+'","'+symbolsize+'","'+category+'","'+label+'","'+value+'","'+x+'","'+y+'")'
        cursor.execute(query.encode('utf-8'))
    query ='commit;'
    cursor.execute(query.encode('utf-8'))
    for row in links:
        if row['id']==None:
            id='Null'
        else:
            id = row['id']
        source = row['source']
        target = row['target']
        query ='insert into chart_demo.t_les_miserables_links(id,source,target) values ("'+id+'","'+source+'","'+target+'")'
        cursor.execute(query.encode('utf-8'))
    query ='commit;'
    cursor.execute(query.encode('utf-8'))
    for row in categories:
        name = row['name']
        query ='insert into chart_demo.t_les_miserables_categories(name) values ("'+name+'")'
        cursor.execute(query.encode('utf-8'))
    query ='commit;'
    cursor.execute(query.encode('utf-8'))
    cursor.close()
    conn.close()