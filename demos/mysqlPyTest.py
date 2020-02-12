import pymysql.cursors

cnx = pymysql.connect(host='localhost',
                      user='root',
                      password='Pa$$w0rd',
                      db='pyTest',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
try:
    with cnx.cursor() as cursor:
        sql = "CREATE TABLE `Users` (name varchar(32))"
        cursor.execute(sql)


    cnx.commit()
finally: cnx.close()
