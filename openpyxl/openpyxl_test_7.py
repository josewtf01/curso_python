import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

# obtenemos la hoja activa, la cual
# es la última en ser modificada
sheet = wb.get_active_sheet()

# Podemos obtener los valores de cierta
# columna usando la varaible columns
# la cual nos da una tupla de tuplas
for CellObject in sheet.columns:
	for column in CellObject:
		print(column,end=' ')
	print("\n")
print("\n")

# aquí los valores de cada celda en cada columna
for CellObject in sheet.columns:
	for column in CellObject:
		print(column.value,end=' ')
	print("\n")
print("\n")

# por lo cual la siguiente parte del código
# tranforma cada tupla en una lista que son
# anidadas dentro de otra lista la cual
# es "x"
x = []
for CellObject in sheet.columns:
	x.append(list(CellObject))
#	for column in CellObject:
#		print(column.value,end=' ')
#	print("\n")

# print("\n")
# print(x)
print("columna B ","\n")
for CellObject in x[1]:
	print(CellObject.value)

print("\n")

# el mismo proceso ocurre solo en este caso
# usando la variable rows

print("Renglon 2 ","\n")
x = []
for CellObject in sheet.rows:
	x.append(list(CellObject))
for CellObject in x[1]:
	print(CellObject.value)
