# aquí empezaremos a ver lo básico para
# escribir archivos de excel
# con código de python
import openpyxl

# abrimos una variable
# que contendra el archivo
# de trabajo
wb = openpyxl.Workbook()

# conseguimos los nombres de la hojas
# que estan en el archivo creado
print(wb.get_sheet_names(),"\n")

# conseguimos al hoja activa
# en este caso solo hay una hoja
# la cual creo el código
# por lo cual al obtener su nombre
# nos dará el nombre por defecto
sheet = wb.get_active_sheet()
print(sheet.title,"\n")

# podemos cambiar el nombre de la hoja

sheet.title = "Hoja 1"
print(wb.get_sheet_names())
