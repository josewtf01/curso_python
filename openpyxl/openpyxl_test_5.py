import openpyxl

from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string

# la función get_column_letter nos da
# la representación con letras como se
# mostraría en excel

print(get_column_letter(1),"\n")
print(get_column_letter(2),"\n")
print(get_column_letter(27),"\n")
print(get_column_letter(900),"\n")

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name("Sheet1")

# imprimimos la letra de la columna más alta que
# contiene información
print(get_column_letter(sheet.max_column),"\n")

# imprimimos el indice de la comlumna dada su
# representación con letras
print(column_index_from_string('A'),"\n")
print(column_index_from_string('AA'),"\n")
