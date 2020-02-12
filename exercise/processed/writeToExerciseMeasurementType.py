
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

        #creating a dictionary from the exercise excel sheet of exercise record
        #numbers and body areas
        rowCount = 1

        exMeasurementTypeArray = {}

        for row in xcrSheet.rows:
            if rowCount > 1:

                # Creating a dictionary, each key representes the workout record
                # number in the db and its value will be an array of body areas
                exMeasurementTypeArray[rowCount - 1] = []

                if row[15].value is not None:
                    if row[15].value.upper() == "BOTH":
                        exMeasurementTypeArray[rowCount - 1].append("Duration")
                        exMeasurementTypeArray[rowCount - 1].append("Distance")
                    elif '/' in row[15].value:
                        delimitedStringsArray = row[15].value.split("/")

                        for word in delimitedStringsArray:
                            if exMeasurementTypeArray[rowCount - 1].count(word) is not 1:
                                exMeasurementTypeArray[rowCount - 1].append(word)
                    else:
                        exMeasurementTypeArray[rowCount -1].append(row[15].value)
                rowCount += 1
            else:
                rowCount += 1

        #making a dictionary of body areas and their corresponding record number
        #from the bodyArea tables
        measurementTypeDictionary = {}

        sql = "SELECT * FROM measurementType"
        cursor.execute(sql)
        types = cursor.fetchall()

        #looping through the results and populating the dictionary
        for aType in types:

            measurementTypeDictionary[aType["measureId"]] = aType["measureType"]

        #loop through the
        for typeId in exMeasurementTypeArray:
        #    print(typeId)
            for eaType in exMeasurementTypeArray[typeId]:
                #print(eaType)
                sql = """INSERT INTO exerciseMeasurementType (exerciseId, measureId)
                         VALUES(%s,%s)"""
                cursor.execute(sql,(typeId,list(measurementTypeDictionary.keys())[list(measurementTypeDictionary.values()).index(eaType)]))
    cnx.commit()
finally:
    cnx.close()
