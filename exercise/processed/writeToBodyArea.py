
import openpyxl, pprint, datetime
import pymysql.cursors

dateTimeNow = datetime.datetime.today().strftime('%Y-%m-%d')
exerciseXlsx   = openpyxl.load_workbook('../files/ExerciseDB.xlsx')
first_sheet    = exerciseXlsx.get_sheet_names()[0]
xcrSheet       = exerciseXlsx.get_sheet_by_name(first_sheet)

cnx = pymysql.connect(host='localhost',
                      user='root',
                      password='Pa$$w0rd',
                      db='FAM',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
cursor = cnx.cursor()

try:
    with cnx.cursor() as cursor:

        rowCount = 0

        bodyArray = []

        for row in xcrSheet.rows:
            if rowCount > 0:
                if row[2].value is not None:
                    if bodyArray.count(row[2].value) is not 1:
                        bodyArray.append(row[2].value)
                if row[3].value is not None:
                    if bodyArray.count(row[3].value) is not 1:
                        bodyArray.append(row[3].value)
                if row[4].value is not None:
                    if bodyArray.count(row[4].value) is not 1:
                        bodyArray.append(row[4].value)
                if row[5].value is not None:
                    if bodyArray.count(row[5].value) is not 1:
                        bodyArray.append(row[5].value)
            else:
                rowCount += 1

        #loop through array and run insert statements
        for bodyAreaName in bodyArray:
            sql = """INSERT INTO bodyArea (bodyAreaName, createdOn, updatedOn) VALUES(%s,%s,%s) """
            cursor.execute(sql,(bodyAreaName, dateTimeNow, dateTimeNow))

    cnx.commit()
finally: cnx.close()
