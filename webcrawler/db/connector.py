import pymysql
import json


# data를 `date`,`time`,`name`,`city`,`district`,`detailed`,`longitude`,`latitude` 순서대로 List로 넣어 주시면 됩니다~
def insert(data) :
    with open('config.json','r',encoding='utf-8') as f :
        config = json.load(f)
        conn = config['db']
        db = pymysql.connect(user=conn['user'],passwd=conn['passwd'],host=conn['host'],db=conn['db'],charset=conn['charset'])
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "select * from location where city = %s and district = %s and name = %s"
        cursor.execute(sql, (data[3], data[4], data[2]))
        result = cursor.fetchall()
        if len(result) != 0 :
            return False
        else :
            sql = "INSERT INTO `corona`.`location`(`date`,`time`,`name`,`city`,`district`,`detailed`,`longitude`,`latitude`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            db.commit()
