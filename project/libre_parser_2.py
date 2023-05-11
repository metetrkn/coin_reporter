# Importing the necessary LibreOffice modules
import uno
from com.sun.star.beans import PropertyValue

# Create a new LibreOffice desktop instance
local_context = uno.getComponentContext()
resolver = local_context.ServiceManager.createInstanceWithContext(
    "com.sun.star.bridge.UnoUrlResolver", local_context )

ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

# Set the file path of the document to open
document_path = "/home/mete/yazilim/projects/project/sample.ods"

# Create a new PropertyValue object to set the load properties
load_properties = (
    PropertyValue("Hidden", 0, False, 0),
    PropertyValue("ReadOnly", 0, False, 0),
)

# Load the document using the loadComponentFromURL method
document_url = uno.systemPathToFileUrl(document_path)
document = desktop.loadComponentFromURL(document_url, "_blank", 0, load_properties)

# Set the active document to the newly loaded document
document_controller = document.getCurrentController()
document_frame = document_controller.getFrame()
document_frame.activate()