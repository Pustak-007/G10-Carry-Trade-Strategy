import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#Code for access to the modules of the larger G10 Folder.
import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = datetime(2000,1,1)
end = datetime(2025,1,1)

# Function to retrieve interbank rates for Belgium
def give_belgiumRate():
    try:
        data = fred.get_series("IR3TIB01BEM156N", start, end)
        df = data.to_frame(name="Belgium Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Italy
def give_italyRate():
    try:
        data = fred.get_series("IR3TIB01ITM156N", start, end)
        df = data.to_frame(name="Italy Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Japan
def give_japanRate():
    try:
        data = fred.get_series("IR3TIB01JPM156N", start, end)
        df = data.to_frame(name="Japan Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Australia
def give_australiaRate():
    try:
        data = fred.get_series("IR3TIB01AUM156N", start, end)
        df = data.to_frame(name="Australia Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Netherlands
def give_netherlandsRate():
    try:
        data = fred.get_series("IR3TIB01NLM156N", start, end)
        df = data.to_frame(name="Netherlands Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Switzerland
def give_switzerlandRate():
    try:
        data = fred.get_series("IR3TIB01CHM156N", start, end)
        df = data.to_frame(name="Switzerland Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for France
def give_franceRate():
    try:
        data = fred.get_series("IR3TIB01FRM156N", start, end)
        df = data.to_frame(name="France Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Canada
def give_canadaRate():
    try:
        data = fred.get_series("IR3TIB01CAM156N", start, end)
        df = data.to_frame(name="Canada Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Sweden
def give_swedenRate():
    try:
        data = fred.get_series("IR3TIB01SEM156N", start, end)
        df = data.to_frame(name="Sweden Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for United States
def give_unitedStatesRate():
    try:
        data = fred.get_series("IR3TIB01USM156N", start, end)
        df = data.to_frame(name="United States Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for United Kingdom
def give_unitedKingdomRate():
    try:
        data = fred.get_series("IR3TIB01GBM156N", start, end)
        df = data.to_frame(name="United Kingdom Interbank Rate")
        df.index.name = "Date"
        return df
    except ValueError as err:
        print(f"Error: {err}")
print(give_unitedKingdomRate())