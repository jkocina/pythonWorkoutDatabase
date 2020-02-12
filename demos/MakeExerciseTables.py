import openpyxl, pprint, datetime
import pymysql.cursors

public class MakeExerciseTables {
    def writeToExerciseTable(xlsxFile):

        def __init__(xlsxFile):
            dateTimeNow = datetime.datetime.today().strftime('%Y-%m-%d')
            exerciseXlsx   = openpyxl.load_workbook(xlsxFile)
            first_sheet    = exerciseXlsx.get_sheet_names()[0]
            xcrSheet       = exerciseXlsx.get_sheet_by_name(first_sheet)

            cnx = pymysql.connect(host='localhost',
                                  user='root',
                                  password='Pa$$w0rd',
                                  db='FAM',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
            cursor = cnx.cursor()
}
