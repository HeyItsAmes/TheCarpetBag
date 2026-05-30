# Multi Source Dashboard (Python API Integration Project)

## Overview

This project is a Python-based data aggregation tool that pulls real-time information from multiple external APIs and processes it into structured, readable output.

It combines weather data and news data into a single backend script to simulate the foundation of a dashboard application.

## Features

- Fetches real-time weather data using OpenWeatherMap API
- Retrieves news articles using Mediastack API
- Uses environment variables to securely store API keys
- Parses JSON responses into Python data structures
- Extracts and formats nested API data (dictionaries and lists)
- Iterates through API results using loops
- Outputs clean, readable summaries in the terminal

## Technologies Used

- Python 3
- Requests library
- Python-dotenv
- REST APIs
- JSON data handling

## Key Concepts Practiced

- API authentication
- HTTP requests and response handling
- JSON parsing
- Data extraction from nested structures
- Environment variable management
- Control flow with loops

## Example Output

- Current temperature and weather conditions for a selected city
- Top news headlines with descriptions and sources

## Planned Improvements

- Build a web dashboard to display weather and news in a browser
- Add HTML/CSS frontend with structured “news card” layout
- Implement filtering options (news category, region, and keywords)
- Add JavaScript for dynamic content updates without page refresh
- Auto-refresh data at intervals
- Improve error handling and API response validation
- Deploy as a live web application

## Purpose

This project was built as a learning exercise to simulate real-world API integration workflows commonly used in backend development and data driven applications. It is a working backend prototype that successfully integrates multiple APIs and processes real-time data and is being developed iteratively, where features are added in stages.
