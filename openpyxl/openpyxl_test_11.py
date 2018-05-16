import openpyxl

wb = openpyxl.Workbook()

sheet = wb.get_sheet_by_name("Sheet")
sheet['A1'] = 'Hello World'

print(sheet['A1'],"\n")

print(sheet['A1'].value,"\n")

wb.save("cp.xlsx")
