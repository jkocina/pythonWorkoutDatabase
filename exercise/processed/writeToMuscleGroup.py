
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
        muscleGroupArray = []

        for row in xcrSheet.rows:
            if rowCount > 0:

                if row[6].value is not None:
                    if muscleGroupArray.count(row[6].value) is not 1:
                        muscleGroupArray.append(row[6].value)
                if row[7].value is not None:
                    if muscleGroupArray.count(row[7].value) is not 1:
                        muscleGroupArray.append(row[7].value)
                if row[8].value is not None:
                    if muscleGroupArray.count(row[8].value) is not 1:
                        muscleGroupArray.append(row[8].value)
                if row[9].value is not None:
                    if muscleGroupArray.count(row[9].value) is not 1:
                        muscleGroupArray.append(row[9].value)
            else:
                rowCount += 1

        for muscleGroupName in muscleGroupArray:

            sql = """INSERT INTO muscleGroup (muscleGroupName, createdOn, updatedOn)
                     VALUES(%s,%s,%s) """
            cursor.execute(sql,(muscleGroupName, dateTimeNow, dateTimeNow))
    cnx.commit()
finally: cnx.close()
