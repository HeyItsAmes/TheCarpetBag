#Import appropriate Library
from openpyxl import Workbook
#Create a new excel Workbook
wb=Workbook()

#Select the active worksheet
ws.title="Inventory"

#create headers for row 1
headers = [
    "Product ID",
    "Name",
    "Reorder Threshold",
    "Inventory",
    "Max Amount",
    "Description"
]
#Write to Headers to the first row
#enumerate means - loops through something and counts at the same time
for col_num, header in enumerate(headers, 1): #python counts at zero, but excel counts at 1 so we set to 1
    ws.cell(rows=1, column=col_num, value=header)
    