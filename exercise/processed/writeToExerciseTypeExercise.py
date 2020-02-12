
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

        exerciseTypeExerciseArray = {}

        for row in xcrSheet.rows:
            if rowCount > 1:

                # Creating a dictionary, each key representes the workout record
                # number in the db and its value will be an array of body areas
                exerciseTypeExerciseArray[rowCount - 1] = []

                if row[12].value is not None:
                    if '/' in row[12].value:
                        delimitedString = row[12].value.split("/")

                        for word in delimitedString:
                                if exerciseTypeExerciseArray[rowCount - 1].count(word) is not 1:
                                    exerciseTypeExerciseArray[rowCount - 1].append(word)
                    elif exerciseTypeExerciseArray[rowCount - 1].count(row[12].value) is not 1 :
                        exerciseTypeExerciseArray[rowCount - 1].append(row[12].value)
                rowCount += 1
            else:
                rowCount += 1

        #making a dictionary of body areas and their corresponding record number
        #from the bodyArea tables
        exerciseTypeDictionary = {}

        sql = "SELECT * FROM typeExercise"
        cursor.execute(sql)
        exerciseTypes = cursor.fetchall()
        #looping through the results and populating the dictionary

        for exerciseType in exerciseTypes:

            exerciseTypeDictionary[exerciseType["typeId"]] = exerciseType["exerciseTypeName"]

        #loop through the
        for exerciseTypeId in exerciseTypeExerciseArray:
            #print(exerciseTypeId)
            for typeExercise in exerciseTypeExerciseArray[exerciseTypeId]:
                #print(typeExercise)
                sql = """INSERT INTO exerciseTypeExercise (exerciseId, typeId)
                         VALUES(%s,%s)"""
                         cnx.commit()
                cursor.execute(sql,(exerciseTypeId,list(exerciseTypeDictionary.keys())[list(exerciseTypeDictionary.values()).index(typeExercise)]))
finally:
    cnx.close()
