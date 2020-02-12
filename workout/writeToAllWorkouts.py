import openpyxl, pprint, datetime
import pymysql.cursors
from workoutWriteFunctions import *
from dbUtil import *

def writeWorkouts():
    dateTimeNow    = datetime.datetime.today().strftime('%Y-%m-%d')

    workoutXlsx    = openpyxl.load_workbook('../files/WorkoutDB.xlsx')
    workout_first_sheet    = workoutXlsx.get_sheet_names()[0]
    exerciseSheet  = exerciseXlsx.get_sheet_by_name(exercise_first_sheet)

    cnx = pymysql.connect(host='localhost',
                          user='root',
                          password='Pa$$w0rd',
                          db='FAM',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor = cnx.cursor()

    try:
        with cnx.cursor() as cursor:

            stopRefChecks(cursor, cnx)

            callAllWorkoutReset(cursor, cnx)


            writeToVideo(cursor, workoutSheet, dateTimeNow)
            writeToProgram(cursor, workoutSheet, dateTimeNow)
            writeToWorkout(cursor, workoutSheet, dateTimeNow)
            writeToExerciseWorkout(cursor, workoutSheet, dateTimeNow)
            #writeToProgramWorkout(cursor, workoutSheet, dateTimeNow)

            startRefChecks(cursor, cnx)

            print("Thanks, may I have another?")

        cnx.commit()
        print("All changes have been commited")
    finally: cnx.close()

writeWorkouts()
