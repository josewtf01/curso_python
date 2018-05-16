import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name('Sheet1')

# imprimimos la celda "A1"
# de nuestra hoja "Sheet1"
print(sheet['A1'],"\n")

# imprimimos el valor de nuestra celda "A1"
print(sheet['A1'].value,"\n")

# asignamos a la variable c toda la información
# de la celda "B1"
c = sheet['B1']

# imprimimos el valor de la celda "B1"
print(c.value,"\n")

# le damos un mejor formato a la información
# de la celda "B1"
print("Row ",end='')
print(str(c.row) + ' ,Column ',end='')
print(c.column + " is " + c.value,"\n")

# Otro formato más corto para la celda "B1"
print('Cell ' + c.coordinate,end='')
print(' is ' + c.value,"\n")

# imprimimos el valor de la celda "C1"
print(sheet['C1'].value,"\n")
