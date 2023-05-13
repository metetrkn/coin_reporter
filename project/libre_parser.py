import uno
import os.path
from com.sun.star.beans import PropertyValue

# Open LibreOffice Calc
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
"""

"""
# Replace "/path/to/your/file.csv" with the actual path to your CSV file
file_path = "./output.csv"

# Check if the file exists
if not os.path.isfile(file_path):
    print("Error: The specified file does not exist.")
    exit()

# Open the file for reading
file = open(file_path, "r")
                    
# Read the contents of the file into a 2D list
csv_data = []
for line in file:
    csv_data.append(line.strip().split(","))

# Close the file
file.close()

# Get the current document
model = desktop.getCurrentComponent()


"""

# Create a new sheet
sheets = model.getSheets()


new_sheet = sheets.insertNewByName("output", sheets.getCount())

# Insert the data into the sheet
for i in range(len(csv_data)):
    for j in range(len(csv_data[i])):
        cell = new_sheet.getCellByPosition(j, i)
        cell.setValue(float(csv_data[i][j]))

# Save the document
props = PropertyValue()
props.Name = "FilterName"
props.Value = "calc8"
model.storeToURL("file:///./output.ods", tuple([props]))

# Close the document
model.close(True)

"""
