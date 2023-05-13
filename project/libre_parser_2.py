import os
import csv
import uno
from ooodev import *

# specify the csv file and ods file paths
csv_file_path = "/home/mete/yazilim/projects/project/output.csv"
ods_file_path = "/home/mete/yazilim/projects/project/work2.ods"

# specify the beginning cell to insert the csv data
beginning_cell = "C3"

# Get the Uno component context from the PyUNO runtime
localContext = uno.getComponentContext()

# Get the Uno service manager from the component context
smgr = localContext.ServiceManager

# Create the Uno desktop object
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", localContext)

# Load the ODS file into a Calc document
document = desktop.loadComponentFromURL(
    uno.systemPathToFileUrl(ods_file_path), "_blank", 0, ()
)

# Get the first sheet in the Calc document
sheet = document.getSheets().getByIndex(0)

# Open the CSV file
with open(csv_file_path, "r") as csv_file:
    # Parse the CSV data
    csv_data = csv.reader(csv_file)

    # Loop through each row in the CSV data
    for i, row in enumerate(csv_data):
        # Loop through each cell in the row
        for j, cell in enumerate(row):
            # Calculate the destination cell based on the beginning cell and the current row and column indices
            destination_cell = sheet.getCellByPosition(j, i).getAbsoluteName()

            # Set the value of the destination cell to the value of the current cell in the CSV data
            sheet.getCellRangeByName(destination_cell).setString(cell)

# Save the changes to the ODS file
document.store()
document.close(True)