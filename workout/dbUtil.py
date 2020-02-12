import pymysql.cursors

def callAllWorkoutReset(cursor, cnx):

    stopRefChecks(cursor, cnx)
    resetDB("program", cursor, cnx)
    resetDB("video", cursor, cnx)
    resetDB("workout", cursor, cnx)
    resetDB("exerciseWorkout", cursor, cnx)
    resetDB("programWorkout", cursor, cnx)
    resetDB("exerciseWorkout", cursor, cnx)
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
