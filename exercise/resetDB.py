import pymysql.cursors

def resetDB(name):
    deleteSql = "DELETE FROM " + name
    incrementSql = "ALTER TABLE " + name + " AUTO_INCREMENT = 0"
    cursor.execute(deleteSql)
    cursor.execute(incrementSql)
    cnx.commit()

def runExerciseReset():
    cnx = pymysql.connect(host='localhost',
                          user='root',
                          password='Pa$$w0rd',
                          db='FAM',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor = cnx.cursor()

    try:
        #resetDB("famGroup")
        resetDB("bodyArea")
        #resetDB("certificationAuthority")
        #resetDB("certifications")
        #resetDB("days")
        resetDB("equipment")
        resetDB("exercise")
        resetDB("exerciseBodyArea")
        resetDB("exerciseEquipment")
        resetDB("exerciseMeasurementType")
        resetDB("exerciseMuscleGroup")
        resetDB("exerciseTypeExercise")
        resetDB("exerciseVideo")
        resetDB("exerciseWorkout")
        #resetDB("fitnessNeeds")
        #resetDB("fitnessTip")
        resetDB("measurementType")
        resetDB("muscleGroup")
        resetDB("program")
        resetDB("programWorkout")
        #resetDB("trainerCertifications")
        resetDB("typeExercise")
        #resetDB("famUser")
        #resetDB("userFavoriteTrainer")
        #resetDB("userFitnessNeeds")
        #resetDB("userProgram")
        #resetDB("userProgramChoice")
        #resetDB("userProgramDays")
        #resetDB("userProgramWorkout")
        #resetDB("userProgramWorkoutExercise")
        #resetDB("userProgress")
        #resetDB("userRole")
        resetDB("userStats")
        resetDB("video")
        resetDB("workout")

    finally: cnx.close()
