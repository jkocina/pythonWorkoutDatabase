
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

        exerciseMuscleGroupArray = {}

        for row in xcrSheet.rows:
            if rowCount > 1:

                # Creating a dictionary, each key representes the workout record
                # number in the db and its value will be an array of body areas
                exerciseMuscleGroupArray[rowCount - 1] = []

                if row[6].value is not None and exerciseMuscleGroupArray[rowCount -1].count(row[6].value) is not 1:
                    exerciseMuscleGroupArray[rowCount - 1].append(row[6].value)

                if row[7].value is not None and exerciseMuscleGroupArray[rowCount -1].count(row[7].value) is not 1:
                    exerciseMuscleGroupArray[rowCount - 1].append(row[7].value)

                if row[8].value is not None and exerciseMuscleGroupArray[rowCount -1].count(row[8].value) is not 1:
                    exerciseMuscleGroupArray[rowCount - 1].append(row[8].value)

                if row[9].value is not None and exerciseMuscleGroupArray[rowCount -1].count(row[9].value) is not 1:
                    exerciseMuscleGroupArray[rowCount - 1].append(row[9].value)

                rowCount += 1
            else:
                rowCount += 1

        #making a dictionary of body areas and their corresponding record number
        #from the bodyArea tables
        muscleGroupDictionary = {}

        sql = "SELECT * FROM muscleGroup"
        cursor.execute(sql)
        muscleGroups = cursor.fetchall()

        #looping through the results and populating the dictionary
        for muscleGroup in muscleGroups:

            muscleGroupDictionary[muscleGroup["muscleGroupId"]] = muscleGroup["muscleGroupName"]

        #loop through the
        for exerciseId in exerciseMuscleGroupArray:

            for muscleGroup in exerciseMuscleGroupArray[exerciseId]:

                sql = """INSERT INTO exerciseMuscleGroup (exerciseId, muscleGroupId)
                         VALUES(%s,%s)"""
                cursor.execute(sql,(exerciseId,list(muscleGroupDictionary.keys())[list(muscleGroupDictionary.values()).index(muscleGroup)]))
    cnx.commit()
finally:
    cnx.close()
