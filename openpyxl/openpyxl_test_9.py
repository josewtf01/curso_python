import openpyxl

# ningún cambio en el código sera guardado
# a menos que llamemos la función save
# además de tener la elección de cambiar el nombre
# del archivo cargado en el código
# y así generar otro archivo

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_active_sheet()

# cambiamos el nombre de la hoja activa
# en el archivo excel que hemos cargado
# previamente
sheet.title = "Hoja 1 XD"

# guardamos los cambios en una nueva
# copia del archivo excel previamente cargado
wb.save("example_copy.xlsx")

# imprimos una cadena si todo ha ido bien
print("Documento guardado")
