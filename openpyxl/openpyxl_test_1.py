import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

# imprimimos los nombres de todas
# las hojas de nuestro archivo excel
print(wb.get_sheet_names(),"\n")

#creamos un objeto que contendrá
# toda la información de la hoja 3
# de nuestro archivo excel
sheet = wb.get_sheet_by_name("Sheet3")

# imprimimos el tipo de sheet
print(sheet,"\n")

print(type(sheet),"\n")
