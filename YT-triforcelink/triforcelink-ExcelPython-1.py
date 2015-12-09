import xlrd
import os



try:
    file_location = os.getcwd()
   print( os.path.join(file_location, data.xlsx))
    print(file_location)
    workbook = xlrd.open_workbook(file_location + '/' + 'data.xlsx')
    sheet = workbook.sheet_by_index(0)
    """
    rows and columns are referenced by their index 
    """
    print(sheet.cell_value(0 ,0))
    print(sheet.nrows) #  number of active rows
    print(sheet.ncols) #  number of active cols 

    for col in range(sheet.ncols):
        print(sheet.cell_value(0, col))

except:
    print('Something went wrong')




    


