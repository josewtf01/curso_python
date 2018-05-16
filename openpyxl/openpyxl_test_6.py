import openpyxl

wb = openpyxl.load_workbook("example.xlsx")

sheet = wb.get_sheet_by_name("Sheet1")

print(tuple(sheet["A1":"C3"]),"\n")

for x in sheet['A1':'C3']:
	for y in x:
		print(y.coordinate, y.value)
	print('--- END OF ROW ---',"\n")
