import pymysql.cursors

def callAllExerciseReset(cursor, cnx):

    stopRefChecks(cursor, cnx)
    #resetDB("famGroup", cursor, cnx)
    resetDB("bodyArea", cursor, cnx)
    #resetDB("certificationAuthority", cursor, cnx)
    #resetDB("certifications", cursor, cnx)
    #resetDB("days", cursor, cnx)
    resetDB("equipment", cursor, cnx)
    resetDB("exercise", cursor, cnx)
    resetDB("exerciseBodyArea", cursor, cnx)
    resetDB("exerciseEquipment", cursor, cnx)
    resetDB("exerciseMeasurementType", cursor, cnx)
    resetDB("exerciseMuscleGroup", cursor, cnx)
    resetDB("exerciseTypeExercise", cursor, cnx)
    resetDB("exerciseVideo", cursor, cnx)
    resetDB("exerciseWorkout", cursor, cnx)
    #resetDB("fitnessNeeds", cursor, cnx)
    #resetDB("fitnessTip", cursor, cnx)
    resetDB("measurementType", cursor, cnx)
    resetDB("muscleGroup", cursor, cnx)
    resetDB("program", cursor, cnx)
    resetDB("programWorkout", cursor, cnx)
    #resetDB("trainerCertifications", cursor, cnx)
    resetDB("typeExercise", cursor, cnx)
    #resetDB("famUser", cursor, cnx)
    #resetDB("userFavoriteTrainer", cursor, cnx)
    #resetDB("userFitnessNeeds", cursor, cnx)
    #resetDB("userProgram", cursor, cnx)
    #resetDB("userProgramChoice", cursor, cnx)
    #resetDB("userProgramDays", cursor, cnx)
    #resetDB("userProgramWorkout", cursor, cnx)
    #resetDB("userProgramWorkoutExercise", cursor, cnx)
    #resetDB("userProgress", cursor, cnx)
    #resetDB("userRole", cursor, cnx)
    resetDB("userStats", cursor, cnx)
    resetDB("video", cursor, cnx)
    resetDB("workout", cursor, cnx)
    startRefChecks(cursor, cnx)

    print("FAM completely reset")

def stopRefChecks(cursor, cnx):

    stopSql = "SET FOREIGN_KEY_CHECKS = 0"
    cursor.execute(stopSql)
    cnx.commit()
    print("Ref Checks Stopped")

def startRefChecks(cursor, cnx):

    startSql = "SET FOREIGN_KEY_CHECKS = 1"
    cursor.execute(startSql)
    cnx.commit()
    print("ref checks started")


def resetDB(name, cursor, cnx):
    deleteSql = "DELETE FROM " + name
    incrementSql = "ALTER TABLE " + name + " AUTO_INCREMENT = 0"
    cursor.execute(deleteSql)
    cursor.execute(incrementSql)
    cnx.commit()

    print(name + " reset")
