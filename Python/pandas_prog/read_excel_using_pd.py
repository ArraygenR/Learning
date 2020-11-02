import pandas as pd

excel_file = "DEG.hya_antibiotic_Vs_WT.xlsx"
second_sheet_name = pd.ExcelFile(excel_file).sheet_names[2]
DEG_data = pd.read_excel(excel_file, sheet_name=second_sheet_name)
print(DEG_data.head())