"""CSV better than excel."""

# parse excel file
pip install openpyxl

from openpyxl import load_workbook
wb = load_workbook('temp_data_01.xlsx')
result = []
ws = wb.worksheets[0]
for row in ws.iter_row():
    results.append([cell.value for cell in row]

print(results)

# but excel is trublemaker for parsing, csv - better, man.
