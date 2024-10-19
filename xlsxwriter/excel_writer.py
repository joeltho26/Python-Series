import xlsxwriter

file = "./xlsxwriter/sample.xlsx"
workbook = xlsxwriter.Workbook(file)
cell_format = [workbook.add_format({'font_color': 'red'}), workbook.add_format({'bold': True})]
worksheet = workbook.add_worksheet()

row, col = 0, 0
worksheet.write(row, col, "Alphabets", cell_format[1])
worksheet.write(row, col + 1, "Number", cell_format[1])

row+=1
worksheet.write(row, col, "A")
worksheet.write(row, col+1, 1)

worksheet.write(row+1, col, "B")
worksheet.write(row+1, col+1, 2)

worksheet.write(row+1, col, "C")
worksheet.write(row+2, col+1, 3) 

workbook.close()