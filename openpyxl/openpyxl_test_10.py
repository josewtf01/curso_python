import openpyxl

wb = openpyxl.Workbook()

print(wb.get_sheet_names(),"\n")

# creamos una hoja de trabajo
# con la función create_sheet
print(wb.create_sheet(),"\n")

#obtenemos los nombres de la hojas
# de trabajo en nuestro archivo
print(wb.get_sheet_names(),"\n")

# creamos una hoja y poniendola al inicio de las
# demás hojas , además de ponerle un titulo
print(wb.create_sheet(index=0,title="primera hoja"),"\n")

print(wb.get_sheet_names(),"\n")

# creamos una hoja y poniendola en la tercera posición
# de las demás hojas , además de ponerle un titulo
print(wb.create_sheet(index=2,title="hoja intermedia"),"\n")

print(wb.get_sheet_names(),"\n")

# podemos remover hojas de nuestro archivo
# con la función remove_sheet

wb.remove_sheet(wb.get_sheet_by_name("hoja intermedia"))

wb.remove_sheet(wb.get_sheet_by_name("Sheet1"))

print(wb.get_sheet_names())
