# State Travel Data Report

## Overview

The State Travel Data Report is a Python-based data integration and reporting project completed as the capstone assignment for the [Vets In Tech](https://vetsintech.co/) Python Fundamentals Bootcamp, sponsored by [DraftKings](https://www.draftkings.com/).

The project retrieves data from two separate API endpoints, combines the datasets using a shared key, and generates a structured Excel workbook containing travel and demographic information for all 50 U.S. states.

This project demonstrates practical experience with API consumption, JSON processing, data transformation, Excel automation, and collaborative development.

## Project Scenario

A travel research organization maintains two separate data sources:

- State demographic information
- State travel and tourism information

The objective was to combine these datasets into a single reporting solution that could be used to analyze travel-related information across the United States.

## Technologies Used

- Python
- requests
- json
- openpyxl
- REST APIs
- Excel (.xlsx)

## Skills Demonstrated

- API integration
- JSON data processing
- Data merging and transformation
- Working with lists and dictionaries
- Nested loop logic
- Excel report generation
- Multi-sheet workbook creation
- Data organization and reporting
- Team collaboration using GitHub

## Data Sources

### State Details API

Provides:

- State name
- Region
- Population

### State Travel API

Provides:

- State name
- Top attraction
- Average trip cost

The two datasets are merged using the shared `state` field.

## Report Output

The program generates an Excel workbook containing two worksheets.

### Sheet 1: State Travel Report

Includes:

- State
- Region
- Population
- Top Attraction
- Average Trip Cost

### Sheet 2: States by Region

Groups states into:

- Midwest
- West
- South
- Northeast

Additional formatting includes:

- Frozen header rows
- Auto-sized columns
- Improved workbook readability
- Enhanced terminal output with formatted completion messages

## Learning Outcomes

This project provided hands-on experience with:

- Retrieving data from external APIs
- Converting JSON data into Python objects
- Combining datasets using a common key
- Automating Excel report creation
- Structuring data for business reporting purposes

## Bootcamp Information

The 4 week Python 3.x Fundamentals course is offered by the non-profit [Vets In Tech](https://vetsintech.co/) for Veterans and Military Spouses. Funding for this cohort was provided in partnership with [DraftKings](https://www.draftkings.com/).

## Course topics included:

- Python fundamentals
- Functional programming
- Object-oriented programming
- API interaction
- JSON processing
- Excel, CSV, and PDF data workflows
- Web scraping
- Automation concepts

Instruction was delivered through Zoom, Canvas, Visual Studio Code, and terminal-based development workflows.

## Collaborative Project

Team Name: cache_me_outside
May 2026 Cohort

Contributors:

- Amy Oglesbee
- Blake La Touf
- Craig Guffey
- Irina La Touf
- Carl Daniels

The planning, programming and development was completed collaboratively as part of the capstone experience.

## Acknowledgments

Special thanks to instructor [Jaël Andre](https://www.linkedin.com/in/jael-andre/) for her guidance throughout the Python Fundamentals Bootcamp and for providing the technical foundation that supported this project.

Additional thanks to [Vets In Tech](https://vetsintech.co/) and [DraftKings](https://www.draftkings.com/) for expanding access to technical education for the military through scholarship-supported training opportunities.

## Files

- `project.py` — main application
- `state_travel_report.xlsx` — generated Excel report
