def writeToProgram(cursor, workoutSheet, dateTimeNow):

    rowCount = 0
    programNames = []

    #Looping through the excel sheet
    for row in workoutSheet.rows:

        #keeping track of the row count so we dont include the label row and we
        #can output how many rows have been staged for commit
        if rowCount > 1:

            #Testing if the program name field in the excel document is not null
            #and not already in the programNames List
            if row[0].value is not None and programNames.count(row[0].value) is not 1:

                #Adding the to programNames List
                programNames.append(row[0].value)

            rowCount += 1
        else:
            rowCount += 1

    #looping through the programNames list and iserting them into the DB
    for name in programNames:

        sql = """INSERT INTO program (creatorId, programName,createdOn, updatedOn) VALUES(%s,%s,%s,%s) """

        cursor.execute(sql,( "1", name, dateTimeNow, dateTimeNow))

        print("Stacked " + str(rowCount) + " queries for commit in writeToProgram")

def writeToVideo(cursor, workoutSheet, dateTimeNow):

    rowCount   = 0
    fileCount  = 0
    videoLinks = []

    #Looping through each row in the worksheet
    for row in workoutSheet.rows:

        #keeping track of the rowCount to avoid the label row and to print out
        #how many rows are staged for commit
        if rowCount > 1:

            #If the cell is not null and not already in the videoLinks
            if row[3].value is not None and videoLinks.count(row[3].value) is not 1:

                #add the cell value to the videoLinks list
                videoLinks.append(row[3].value)

            if row[4].value is not None and videoLinks.count(row[4].value) is not 1:
                videoLinks.append(row[4].value)

            if row[5].value is not None and videoLinks.count(row[5].value) is not 1:
                videoLinks.append(row[5].value)

            if row[6].value is not None and videoLinks.count(row[6].value) is not 1:
                videoLinks.append(row[6].value)

            if row[7].value is not None and videoLinks.count(row[7].value) is not 1:
                videoLinks.append(row[7].value)

            if row[8].value is not None and videoLinks.count(row[8].value) is not 1:
                videoLinks.append(row[8].value)

            if row[9].value is not None and videoLinks.count(row[9].value) is not 1:
                videoLinks.append(row[9].value)

            if row[10].value is not None and videoLinks.count(row[10].value) is not 1:
                videoLinks.append(row[10].value)

            if row[11].value is not None and videoLinks.count(row[11].value) is not 1:
                videoLinks.append(row[11].value)

            if row[12].value is not None and videoLinks.count(row[12].value) is not 1:
                videoLinks.append(row[12].value)

            if row[13].value is not None and videoLinks.count(row[13].value) is not 1:
                videoLinks.append(row[13].value)

            if row[14].value is not None and videoLinks.count(row[14].value) is not 1:
                videoLinks.append(row[14].value)

            rowCount += 1
        else:
            rowCount += 1

    for link in videoLinks:

        sql = """INSERT INTO video (videoLink, createdOn, updatedOn) VALUES(%s,%s,%s) """

        cursor.execute(sql,( link, dateTimeNow, dateTimeNow))

        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToVideo")

def writeToWorkout(cursor, workoutSheet, dateTimeNow):

    fileCount = 0
    rowCount = 0
    workouts = []

    for row in workoutSheet.rows:

        if rowCount > 1:

            if row[1].value is not None and workouts.count(row[1].value) is not 1:
                workouts.append(row[1].value)

            rowCount += 1
        else:
            rowCount += 1

    for workout in workouts:

        sql = """INSERT INTO workout (workoutName, createdOn, updatedOn) VALUES(%s,%s,%s) """

        cursor.execute(sql,( workout, dateTimeNow, dateTimeNow))

        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToWorkout")

#TODO
def writeToProgramWorkout(cursor, workoutSheet, dateTimeNow):

    fileCount = 0
    rowCount = 0
    workoutObject = {}

    #Looping through the Xlsx sheet row by row
    for row in workoutSheet.rows:

        #counting how many rows so we can skip the label row
        if rowCount > 1:

            #If the xlsx row is not null and the dictionary doesnt already
            #contain the value. This is testing for repeated values in the dictionaries key
            if row[1].value is not None and row[1].value in workoutObject is not 1:

                #Adding another key if it doesnt exist
                workoutObject.append(row[1].value)

                #if the value in the row is not null and dictionary doesnt already
                # contain a value at that key
                if row[15].value is not None and workoutObject[row[1].value].count(row[15].value):
                    #append a value to that key
                    workoutObject[row[1].value].append(row[15].value)

                if row[16].value is not None and workoutObject[row[1].value].count(row[16].value):
                    workoutObject[row[1].value].append(row[16].value)

                if row[17].value is not None and workoutObject[row[1].value].count(row[17].value):
                    workoutObject[row[1].value].append(row[17].value)

                if row[18].value is not None and workoutObject[row[1].value].count(row[18].value):
                    workoutObject[row[1].value].append(row[18].value)

                if row[19].value is not None and workoutObject[row[1].value].count(row[19].value):
                    workoutObject[row[1].value].append(row[19].value)

                if row[20].value is not None and workoutObject[row[1].value].count(row[20].value):
                    workoutObject[row[1].value].append(row[20].value)

                if row[21].value is not None and workoutObject[row[1].value].count(row[21].value):
                    workoutObject[row[1].value].append(row[21].value)

                if row[22].value is not None and workoutObject[row[1].value].count(row[22].value):
                    workoutObject[row[1].value].append(row[22].value)

                if row[23].value is not None and workoutObject[row[1].value].count(row[23].value):
                    workoutObject[row[1].value].append(row[23].value)

                if row[24].value is not None and workoutObject[row[1].value].count(row[24].value):
                    workoutObject[row[1].value].append(row[24].value)

                if row[25].value is not None and workoutObject[row[1].value].count(row[25].value):
                    workoutObject[row[1].value].append(row[25].value)

                if row[26].value is not None and workoutObject[row[1].value].count(row[26].value):
                    workoutObject[row[1].value].append(row[26].value)

            rowCount += 1
        else:
            rowCount += 1

    for workout in workoutObject:

        #sql = """INSERT INTO programWorkout (workoutName, createdOn, updatedOn) VALUES(%s,%s,%s) """

        #cursor.execute(sql,( workout, dateTimeNow, dateTimeNow))

        fileCount += 1

        print("Stacked " + str(fileCount) + " queries for commit in writeToProgramWorkout")


#TODO
def writeToExerciseWorkout(cursor, workoutSheet, dateTimeNow):

    rowCount       = 0
    fileCount      = 0
    workoutExerciseObject = {}

    #Looping through the Xlsx sheet row by row
    for row in workoutSheet.rows:

        #See if the exercise is in the exercise table and link the exerciseId and the WorkoutId
        listOfExercise = []

        #counting how many rows so we can skip the label row
        if rowCount > 1:

            if row[15].value is not None and listOfExercise.count(row[15].value):

            if row[26].value is not None and listOfExercise.count(row[26].value):


            #If the xlsx row is not null and the dictionary doesnt already
            #contain the value. This is testing for repeated values in the dictionaries key
            if row[2].value is not None and row[2].value in workoutExerciseObject is not 1:

                #Adding another key if it doesnt exist
                workoutObject.append(row[1].value)

                #if the value in the row is not null and dictionary doesnt already
                # contain a value at that key
                if row[15].value is not None and workoutObject[row[1].value].count(row[15].value):
                    #append a value to that key
                    workoutObject[row[1].value].append(row[15].value)

                if row[16].value is not None and workoutObject[row[1].value].count(row[16].value):
                    workoutObject[row[1].value].append(row[16].value)

                if row[17].value is not None and workoutObject[row[1].value].count(row[17].value):
                    workoutObject[row[1].value].append(row[17].value)

                if row[18].value is not None and workoutObject[row[1].value].count(row[18].value):
                    workoutObject[row[1].value].append(row[18].value)

                if row[19].value is not None and workoutObject[row[1].value].count(row[19].value):
                    workoutObject[row[1].value].append(row[19].value)

                if row[20].value is not None and workoutObject[row[1].value].count(row[20].value):
                    workoutObject[row[1].value].append(row[20].value)

                if row[21].value is not None and workoutObject[row[1].value].count(row[21].value):
                    workoutObject[row[1].value].append(row[21].value)

                if row[22].value is not None and workoutObject[row[1].value].count(row[22].value):
                    workoutObject[row[1].value].append(row[22].value)

                if row[23].value is not None and workoutObject[row[1].value].count(row[23].value):
                    workoutObject[row[1].value].append(row[23].value)

                if row[24].value is not None and workoutObject[row[1].value].count(row[24].value):
                    workoutObject[row[1].value].append(row[24].value)

                if row[25].value is not None and workoutObject[row[1].value].count(row[25].value):
                    workoutObject[row[1].value].append(row[25].value)

                if row[26].value is not None and workoutObject[row[1].value].count(row[26].value):
                    workoutObject[row[1].value].append(row[26].value)

            rowCount += 1
        else:
            rowCount += 1

    for workout in workoutObject:

        #sql = """INSERT INTO workout (workoutName, createdOn, updatedOn) VALUES(%s,%s,%s) """

        #cursor.execute(sql,( workout, dateTimeNow, dateTimeNow))

        fileCount += 1
        print("Stacked " + str(fileCount) + " queries for commit in writeToExerciseWorkout")


def populateDataSet(cursor):

        sql = """ SELECT * FROM exercise"""

        cursor.execute(sql, tuple)
