import pymysql

conn = pymysql.connect(host='localhost',
                        user='debian-sys-maint',
                        passwd='EIl0mMQqevL99ojk')
try:
    with conn.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
            id int NOT NULL AUTO_INCREMENT,
            latitude FLOAT(10, 6),
            longitude FLOAT(10, 6),
            date DATETIME,
            category VARCHAR(1000),
            updated_at TIMESTAMP,
            PRIMARY KEY(id)
        )""" 
        cursor.execute(sql);
        conn.commit()
finally:
    conn.close