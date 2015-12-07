import xlrd

file_location = 'c:/users/peter/documents/git/pythonexcel/data.xlsx'
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
"""
rows and columns are referenced by their index 
"""
print(sheet.cell_value(0 ,0))
print(sheet.nrows) #  number of active rows
print(sheet.ncols) #  number of active cols 

for col in range(sheet.ncols):
    print(sheet.cell_value(0, col))


    


