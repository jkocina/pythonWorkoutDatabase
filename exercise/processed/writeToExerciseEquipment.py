
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

        exEquipmentArray = {}

        for row in xcrSheet.rows:
            if rowCount > 1:

                # Creating a dictionary, each key representes the workout record
                # number in the db and its value will be an array of body areas
                exEquipmentArray[rowCount - 1] = []

                if row[20].value is not None and exEquipmentArray[rowCount - 1].count(row[20].value) is not 1:
                    exEquipmentArray[rowCount - 1].append(row[20].value)

                if row[21].value is not None and exEquipmentArray[rowCount - 1].count(row[21].value) is not 1:
                    exEquipmentArray[rowCount - 1].append(row[21].value)

                if row[22].value is not None and exEquipmentArray[rowCount - 1].count(row[22].value) is not 1:
                    exEquipmentArray[rowCount - 1].append(row[22].value)

                rowCount += 1
            else:
                rowCount += 1

        #making a dictionary of body areas and their corresponding record number
        #from the equipment tables
        equipmentDictionary = {}

        sql = "SELECT * FROM equipment"
        cursor.execute(sql)
        equipments = cursor.fetchall()

        #looping through the results and populating the dictionary
        for equipment in equipments:

            equipmentDictionary[equipment["equipmentId"]] = equipment["equipmentName"]

        for equipmentId in exEquipmentArray:
            for equipment in exEquipmentArray[equipmentId]:
                sql = """INSERT INTO exerciseEquipment (exerciseId, equipmentId)
                         VALUES(%s,%s)"""
                cursor.execute(sql,(equipmentId,list(equipmentDictionary.keys())[list(equipmentDictionary.values()).index(equipment)],dateTimeNow, dateTimeNow))
    cnx.commit()
finally:
    cnx.close()
