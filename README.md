# Test Automation Framework

## Overview
This project provides a suite of automated tests for both Web UI and API components.

## Requirements
- Python 3.x
- Selenium WebDriver
- pytest
- requests library

## Setup and Running Tests
Python 3.x (3.10+ is preferred)
pip (Python package installer)
Clone the repository: git clone https://github.com/Osmolianchuk/final_project.git
Navigate to the project directory: cd -final_project
Install the required Python packages: pip install -r requirements.txt

## Test Execution and Reporting
$  pytest api_tests/ --html=reports/api_report.html
$  pytest ui_tests/ --html=reports/ui_report.html
After execution, report will be automatically generated with captured logs for each test in reports/ folder
