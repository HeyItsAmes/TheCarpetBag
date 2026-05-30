# Part 1: Fetch the data

import requests
import json

states_url = "https://state-data-api.proxy.beeceptor.com/state-details"
travel_url = "https://state-data-api.proxy.beeceptor.com/state-travel-data"

states_response = requests.get(states_url)
travel_response = requests.get(travel_url)

states_text = states_response.text
travel_text = travel_response.text

states_data = json.loads(states_text)
travel_data = json.loads(travel_text)

print(states_data[0])
print(travel_data[0])
 
# Part 2 - Combine the data

combined_data = []

for state in states_data:
    for travel in travel_data:
        if state["state"] == travel["state"]:
            combined_state = {
                "state": state["state"],
                "region": state["region"],
                "population": state["population"],
                "top_attraction": travel["top_attraction"],
                "average_trip_cost": travel["average_trip_cost"]
            }
            combined_data.append(combined_state)

print(combined_data[0])

# Part 3 - Create excel report

import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "State Travel Report"
ws.append(["State", "Region", "Population", "Top Attraction", "Average Trip Cost"])

for data in combined_data:
    ws.append([
        data["state"],
        data["region"],
        data["population"],
        data["top_attraction"],
        data["average_trip_cost"]
    ])
  


# Part 4 - Create second sheet

ws2 = wb.create_sheet("States by Region")
ws2.append(["State", "Top Attraction", "Average Trip Cost", "Region"])

regions = ["Midwest", "West", "South", "Northeast"]

for region in regions:
    for record in combined_data:
        if record["region"] == region:
            ws2.append([
                record["state"],
                record["top_attraction"],
                record["average_trip_cost"],
                record["region"]
            ])
    ws2.append([])

# Fancy auto-formatting
# Freeze top row on both sheets
ws.freeze_panes = "A2"
ws2.freeze_panes = "A2"

# Auto-fit column widths for sheet 1
for column in ws.columns:
    max_length = max(len(str(cell.value)) for cell in column if cell.value)
    ws.column_dimensions[column[0].column_letter].width = max_length + 2

# Auto-fit column widths for sheet 2
for column in ws2.columns:
    max_length = max(len(str(cell.value)) for cell in column if cell.value)
    ws2.column_dimensions[column[0].column_letter].width = max_length + 2

# Final save
wb.save("state_travel_report_fancy_formatting.xlsx")
