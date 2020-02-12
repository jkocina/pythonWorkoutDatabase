
import openpyxl, pprint, datetime
import pymysql.cursors

dateTimeNow    = datetime.datetime.today().strftime('%Y-%m-%d')
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

        for row in xcrSheet.rows:
            if rowCount > 0:
                tinyIntValues = {}

                if row[14].value is not None:
                    flexibility = 1
                else:
                    flexibility = 0

                if row[16].value is not None and row[16].value.upper() == "Y":
                    weightPattern = 1
                else:
                    weightPattern = 0

                if row[17].value is not None and row[17].value.upper() == "Y":
                    spotter = 1
                else:
                    spotter = 0

                if row[19].value is not None and row[19].value.upper() == "Y" or row[19].value.upper() == "YES":
                    equipmentRequired = 1
                else:
                    equipmentRequired = 0

                name          = row[0].value
                alternation   = row[10].value
                spectrum      = row[11].value
                #muscularFocus = row[12].value
                metabolicEquivalent = row[13].value
                difficulty          = row[18].value
                #link                = row[23].value

                sql = """INSERT INTO exercise (exerciseName, alternation, spectrum,
                       metabolicEquivalent, flexibility, weightPattern,
                       spotter, difficulty, equipmentRequired, createdOn,
                       updatedOn) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
                cursor.execute(sql,(name, alternation, spectrum, metabolicEquivalent, flexibility, weightPattern, spotter, difficulty, equipmentRequired, dateTimeNow, dateTimeNow))
            else:
                rowCount += 1
    cnx.commit()
finally:
    cnx.close()
