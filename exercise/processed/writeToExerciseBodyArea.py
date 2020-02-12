
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

        #creating a dictionary from the exercise excel sheet of exercise record
        #numbers and body areas
        rowCount = 1

        exBodAreaArray = {}

        for row in xcrSheet.rows:
            if rowCount > 1:

                # Creating a dictionary, each key representes the workout record
                # number in the db and its value will be an array of body areas
                exBodAreaArray[rowCount - 1] = []

                if row[2].value is not None:
                    exBodAreaArray[rowCount - 1].append(row[2].value)

                if row[3].value is not None:
                    exBodAreaArray[rowCount - 1].append(row[3].value)

                if row[4].value is not None:
                    exBodAreaArray[rowCount - 1].append(row[4].value)

                if row[5].value is not None:
                    exBodAreaArray[rowCount - 1].append(row[5].value)


                rowCount += 1
            else:
                rowCount += 1

        #making a dictionary of body areas and their corresponding record number
        #from the bodyArea tables
        bodyAreaDictionary = {}

        sql = "SELECT * FROM bodyArea"
        cursor.execute(sql)
        bodyAreas = cursor.fetchall()

        #looping through the results and populating the dictionary
        for bodyArea in bodyAreas:

            bodyAreaDictionary[bodyArea["bodyAreaId"]] = bodyArea["bodyAreaName"]

        #loop through the
        for exerciseId in exBodAreaArray:
            for bodyArea in exBodAreaArray[exerciseId]:
                sql = """INSERT INTO exerciseBodyArea (exerciseId, bodyAreaId, createdOn, updatedOn)
                         VALUES(%s,%s,%s,%s)"""
                cursor.execute(sql,(exerciseId,list(bodyAreaDictionary.keys())[list(bodyAreaDictionary.values()).index(bodyArea)], dateTimeNow, dateTimeNow))
    cnx.commit()
finally:
    cnx.close()
