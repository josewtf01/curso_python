# instalar vía PIP
# pip install openpyxl

# instalar vía anaconda
# conda install -c anaconda openpyxl
import openpyxl

# cargamos el archivo en excel
# con el que trabajaremos
# en la variable wb
wb = openpyxl.load_workbook('example.xlsx')

# imprimimos el tipo de la varaible wb
print(type(wb))

# documentación
# https://openpyxl.readthedocs.io/en/stable/
