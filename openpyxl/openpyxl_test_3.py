import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name('Sheet1')

# imprimimos la celda que se encuentra
# en las coordenadas 1, 2 siendo la
# celda "B1"
print(sheet.cell(row=1,column=2),"\n")

# imprimimos el contenido de la celda
# B1
value = sheet.cell(row=1,column=2).value
print(value,"\n")

# creamos un for para imprimir los contenidos
# de celdas impares
for i in range(1,8,2):
    value = sheet.cell(row=i,column=2).value
    print(i,value)
