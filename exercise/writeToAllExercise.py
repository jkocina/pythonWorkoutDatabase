
import openpyxl, pprint, datetime
import pymysql.cursors
from exerciseWriteFunctions import *
from dbUtil import *

def writeExercises():

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

            stopRefChecks(cursor, cnx)
            callAllExerciseReset(cursor, cnx)

            writeToBodyArea(cursor, xcrSheet, dateTimeNow)
            writeToEquipment(cursor, xcrSheet, dateTimeNow)
            writeToExercise(cursor, xcrSheet, dateTimeNow)
            writeToMeasurementType(cursor, xcrSheet, dateTimeNow)
            writeToMuscleGroup(cursor, xcrSheet, dateTimeNow)
            writeTypeExercise(cursor, xcrSheet, dateTimeNow)
            writeToExerciseBodyArea(cursor, xcrSheet, dateTimeNow)
            writeToExerciseEquipment(cursor, xcrSheet, dateTimeNow)
            writeToExerciseMeasurementType(cursor, xcrSheet, dateTimeNow)
            writeToExerciseMuscleGroup(cursor, xcrSheet, dateTimeNow)
            writeToExerciseTypeExercise(cursor, xcrSheet, dateTimeNow)

            startRefChecks(cursor, cnx)

            print("Thank you very much, may I have another")
        cnx.commit()
        print("All Changes Commited")
    finally: cnx.close()

writeExercises()
