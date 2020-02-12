
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
        equipmentArray = []

        for row in xcrSheet.rows:
            if rowCount > 0:

                if row[20].value is not None:
                    if equipmentArray.count(row[20].value) is not 1:
                        equipmentArray.append(row[20].value)
                if row[21].value is not None:
                    if equipmentArray.count(row[21].value) is not 1:
                        equipmentArray.append(row[21].value)
                if row[22].value is not None:
                    if equipmentArray.count(row[22].value) is not 1:
                        equipmentArray.append(row[22].value)
            else:
                rowCount += 1

        for equipment in equipmentArray:
            sql = """INSERT INTO equipment ( equipmentName, createdOn, updatedOn) VALUES(%s,%s,%s) """
            cursor.execute(sql,(equipment, dateTimeNow, dateTimeNow))

    cnx.commit()
finally: cnx.close()
