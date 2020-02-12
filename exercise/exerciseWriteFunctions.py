def writeToBodyArea(cursor, xcrSheet, dateTimeNow):

    rowCount = 0
    fileCount = 0

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
        fileCount += 1
        print ("Stacked " + str(fileCount) + " queries for commit in writeToBodyArea")

def writeToEquipment(cursor, xcrSheet, dateTimeNow):

    rowCount = 0
    fileCount = 0
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
        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToEquipment")

def writeToExercise(cursor, xcrSheet, dateTimeNow):

    rowCount = 0

    for row in xcrSheet.rows:
        if rowCount > 0:

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

            print("Stacked " + str(rowCount) + " queries for commit in writeToExercise")

            rowCount += 1
        else:
            rowCount += 1

def writeToMeasurementType(cursor, xcrSheet, dateTimeNow):

    rowCount = 0
    fileCount = 0

    measurementArray = []

    for row in xcrSheet.rows:
        if rowCount > 0:
            if row[15].value is not None:
                if '/' in row[15].value:
                    delimitedString = row[15].value.split("/")

                    for word in delimitedString:
                        if measurementArray.count(word) is not 1:
                            measurementArray.append(word)

                elif measurementArray.count(row[15].value) is not 1 and row[15].value.upper() != 'BOTH':
                    measurementArray.append(row[15].value)
        else:
            rowCount += 1

    #loop through array and run insert statements
    for measurement in measurementArray:
        sql = """INSERT INTO measurementType (measureType, createdOn, updatedOn) VALUES(%s,%s,%s) """
        cursor.execute(sql,(measurement, dateTimeNow, dateTimeNow))
        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToMeasurementType")

def writeToMuscleGroup(cursor, xcrSheet, dateTimeNow):

    rowCount = 0
    muscleGroupArray = []
    fileCount = 0

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
        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToMuscleGroup")

def writeTypeExercise(cursor, xcrSheet, dateTimeNow):

    rowCount = 0
    fileCount = 0

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
        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeTypeExercise")

def writeToExerciseBodyArea(cursor, xcrSheet, dateTimeNow):

    #creating a dictionary from the exercise excel sheet of exercise record
    #numbers and body areas
    rowCount = 1
    fileCount = 0

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
            fileCount += 1
            print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseBodyArea")

def writeToExerciseEquipment(cursor, xcrSheet, dateTimeNow):

    #This will create an associative array. Each index will represent the index
    #of the exercise in the exercise table and each value will be an array of
    #equipment needed for that exercise
    rowCount = 1
    fileCount = 0

    # This associative array will have indexes representing the id of exercises in
    # the exercise table, since the exercise table was read in order when populated
    # this array can read the files in order, automatically increment the key and it will
    # represent the id of the exercise in the exercise table. Allowing us to
    # use this to populate the exerciseEquipment table with both the exerciseId
    # and the equipmentId
    exEquipmentArray = {}

    for row in xcrSheet.rows:
        if rowCount > 1:

            # populating the dictionary with the value of
            exEquipmentArray[rowCount - 1] = []

            if row[20].value is not None and exEquipmentArray[rowCount -1].count(row[20].value) is not 1:
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
            sql = """INSERT INTO exerciseEquipment (exerciseId, equipmentId, createdOn, updatedOn)
                     VALUES(%s,%s, %s, %s)"""

            equipId = list(equipmentDictionary.keys())[list(equipmentDictionary.values()).index(equipment)]

            cursor.execute(sql,(equipmentId, equipId, dateTimeNow, dateTimeNow))
            fileCount += 1
            print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseEquipment")


def writeToExerciseMeasurementType(cursor, xcrSheet, dateTimeNow):

    #creating a dictionary from the exercise excel sheet of exercise record
    #numbers and body areas
    rowCount = 1
    fileCount = 0

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
            sql = """INSERT INTO exerciseMeasurementType (exerciseId, measureId, createdOn, updatedOn)
                     VALUES(%s,%s, %s, %s)"""
            cursor.execute(sql,(typeId,list(measurementTypeDictionary.keys())[list(measurementTypeDictionary.values()).index(eaType)], dateTimeNow, dateTimeNow))
            fileCount += 1
            print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseMeasurementType")

def writeToExerciseMuscleGroup(cursor, xcrSheet, dateTimeNow):

    #creating a dictionary from the exercise excel sheet of exercise record
    #numbers and body areas
    rowCount = 1
    fileCount = 0

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

            sql = """INSERT INTO exerciseMuscleGroup (exerciseId, muscleGroupId, createdOn, updatedOn)
                     VALUES(%s,%s, %s, %s)"""
            cursor.execute(sql,(exerciseId,list(muscleGroupDictionary.keys())[list(muscleGroupDictionary.values()).index(muscleGroup)],dateTimeNow, dateTimeNow))
            fileCount += 1
            print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseMuscleGroup")

def writeToExerciseTypeExercise(cursor, xcrSheet, dateTimeNow):

    #creating a dictionary from the exercise excel sheet of exercise record
    #numbers and body areas
    rowCount = 1
    fileCount = 0

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
            sql = """INSERT INTO exerciseTypeExercise (exerciseId, typeId, createdOn, updatedOn)
                     VALUES(%s,%s,%s,%s)"""
            cursor.execute(sql,(exerciseTypeId,list(exerciseTypeDictionary.keys())[list(exerciseTypeDictionary.values()).index(typeExercise)], dateTimeNow, dateTimeNow))
            fileCount += 1
            print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseTypeExercise")
