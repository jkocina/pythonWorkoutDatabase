
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

        typeExerciseArray = []

        for row in xcrSheet.rows:
            if rowCount > 0:
                if row[12].value is not None:
                    if '/' in row[12].value:
                        delimitedString = row[12].value.split("/")

                        for word in delimitedString:
                            if measurementArray.count(word) is not 1:
                                measurementArray.append(word)
                    elif typeExerciseArray.count(row[12].value) is not 1 and row[12].value.upper() != 'BOTH':
                        typeExerciseArray.append(row[12].value)
            else:
                rowCount += 1

        #loop through array and run insert statements
        for typeExercise in typeExerciseArray:
            sql = """INSERT INTO typeExercise (exerciseTypeName, createdOn, updatedOn) VALUES(%s,%s,%s) """
            cursor.execute(sql,(typeExercise, dateTimeNow, dateTimeNow))

    cnx.commit()
finally: cnx.close()
