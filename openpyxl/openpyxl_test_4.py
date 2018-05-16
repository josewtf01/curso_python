import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name('Sheet1')

# imprimimos el renglo más alto
print("highest row ",sheet.max_row,"\n")

# imprimimos la columna más alta
print("highest column ",sheet.max_column,"\n")

# imprimimos las dimensiones de la celdas
# que tienen contenido teniendo
# renglones x columnas 
print("dimensions of the sheet ",end='')
print(sheet.max_row,end='')
print(" x ",end='')
print(sheet.max_column,"\n")
