import pyexcel as pe

# Specify CSV files beginning column and row
start_row = 0  # Row 1 contains the header row
start_col = 0  # Column 0 is the first column

# Load the CSV file using pyexcel
data = pe.get_sheet(file_name='/home/mete/yazilim/projects/project/output2.csv', start_row=start_row, start_column=start_col).array

# Create a pyexcel sheet and populate it with the data
sheet = pe.Sheet(data)

sheet.save_as('/home/mete/yazilim/projects/project/data.ods')
