
import pandas as pd
import os
from datetime import datetime

def new_records(df):
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Construct filename with current date
    filename = f"../updated_{current_date}.xlsx"

    with pd.ExcelWriter(filename, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False, startrow=0)

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

        # defining column settings
        (max_row, max_col) = df.shape
        column_settings = [{"header": col} for col in df.columns]

        # Define table range & add table
        worksheet.add_table(0, 0, max_row, max_col -1,{
            "columns": column_settings,
            "name": "Table1",
    })

def records(df):
    file_path = "../records.xlsx"

    # Check if file exists and determine mode and start row
    if os.path.exists(file_path):
        workbook = load_workbook(file_path)
        sheet = workbook.active
        start_row = sheet.max_row
        mode = "a"
        sheet_exists_option = {"if_sheet_exists": "overlay"}
        write_header = False
    else:
        start_row = 0
        mode = "w"
        sheet_exists_option = {}
        write_header = True

    # Use unpacking to only include 'if_sheet_exists' when needed
    with pd.ExcelWriter(file_path, engine="openpyxl", mode=mode, **sheet_exists_option) as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False, startrow=start_row,header=write_header)

    print(f"Data written to {file_path}")

def export_data(df):
    new_records(df)
    records(df)
