import openpyxl, pprint

exerciseXlsx = openpyxl.load_workbook('ExerciseDB.xlsx')
first_sheet  = exerciseXlsx.get_sheet_names()[0]
xcrSheet     = exerciseXlsx.get_sheet_by_name(first_sheet)


for row in xcrSheet.rows:
    if row[22].value is None:
        print("Nothing")
    else:
        print(type(row[22].value))
        print(row[22].value)
