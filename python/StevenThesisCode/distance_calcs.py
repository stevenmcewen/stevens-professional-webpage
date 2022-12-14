import openpyxl
import math
from collections import defaultdict

OUTPUT_FILE_PATH = 'C:/Users/Steven McEwen/OneDrive - University of Cape Town/Desktop/Masters thesis/thesis_data_testing/combined/output.xlsx'

wb = openpyxl.load_workbook(OUTPUT_FILE_PATH)

# Iterate over the sheet names in the workbook
for sheet_name in wb.sheetnames:
    # Select the sheet you want to work with
    sheet = wb[sheet_name]

    grid = defaultdict(int)
    for x in range(-10, 11):
        for y in range(-10, 11):
            for i, (x_value, y_value) in enumerate(zip(sheet['AA'], sheet['AB'])):
                # Skip the first row
                if i == 0:
                    continue
                x_value = x_value.value
                y_value = y_value.value
                distance = math.sqrt((x - x_value)**2 + (y - y_value)**2)

                if distance <= 1:
                    grid[(x, y)] += 1
                else:
                    continue
    print(grid)
    # code to save the grid in some format or use it for further analysis




