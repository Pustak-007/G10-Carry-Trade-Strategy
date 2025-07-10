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
start = datetime(2004,1,1)
end = datetime(2025,1,1)
daily_index = pd.date_range(start = start, end = end, freq = 'D')
# Function to retrieve interbank rates for Belgium
def give_belgiumRate():
    try:
        data = fred.get_series("IR3TIB01BEM156N", start, end)
        df = data.to_frame(name="Belgium Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Italy
def give_italyRate():
    try:
        data = fred.get_series("IR3TIB01ITM156N", start, end)
        df = data.to_frame(name="Italy Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Japan
def give_japanRate():
    try:
        data = fred.get_series("IR3TIB01JPM156N", start, end)
        df = data.to_frame(name="Japan Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Australia
def give_australiaRate():
    try:
        data = fred.get_series("IR3TIB01AUM156N", start, end)
        df = data.to_frame(name="Australia Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Netherlands
def give_netherlandsRate():
    try:
        data = fred.get_series("IR3TIB01NLM156N", start, end)
        df = data.to_frame(name="Netherlands Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Switzerland
def give_switzerlandRate():
    try:
        data = fred.get_series("IR3TIB01CHM156N", start, end)
        df = data.to_frame(name="Switzerland Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for France
def give_franceRate():
    try:
        data = fred.get_series("IR3TIB01FRM156N", start, end)
        df = data.to_frame(name="France Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Canada
def give_canadaRate():
    try:
        data = fred.get_series("IR3TIB01CAM156N", start, end)
        df = data.to_frame(name="Canada Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for Sweden
def give_swedenRate():
    try:
        data = fred.get_series("IR3TIB01SEM156N", start, end)
        df = data.to_frame(name="Sweden Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for United States
def give_unitedStatesRate():
    try:
        data = fred.get_series("IR3TIB01USM156N", start, end)
        df = data.to_frame(name="United States Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

# Function to retrieve interbank rates for United Kingdom
def give_unitedKingdomRate():
    try:
        data = fred.get_series("IR3TIB01GBM156N", start, end)
        df = data.to_frame(name="United Kingdom Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

#Function to retrieve interbank rates for Norway
def give_norwayRate():
    try:
        data = fred.get_series("IR3TIB01NOM156N", start, end)
        df = data.to_frame(name="Norway Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

#Storing each function's result in a variable
#Refer to this variable when you need the data - saves from redundant computation

belgium = give_belgiumRate()
italy = give_italyRate()
japan = give_japanRate()
australia = give_australiaRate()
netherlands = give_netherlandsRate()
switzerland = give_switzerlandRate()
france = give_franceRate()
canada = give_canadaRate()
sweden = give_swedenRate()
united_states = give_unitedStatesRate()
united_kingdom = give_unitedKingdomRate()
norway = give_norwayRate()


# List of DataFrames for concatenation
concat_list = [
    belgium,italy,japan,australia,netherlands,switzerland,france,canada,sweden,
    united_states,united_kingdom, norway
]

#temp, just for checking

#Combination of all the prior dataframes - The Large set
def give_largeSet():
    df = pd.concat(concat_list, axis = 1)
    return df
date_for_ascen = datetime(2005,12,4)
def give_ascending(Date = date_for_ascen):
    try:
        # List to store (country, rate) tuples
        rates = [
            ("Belgium", belgium.loc[Date, "Belgium Interbank Rate"]),
            ("Italy", italy.loc[Date, "Italy Interbank Rate"]),
            ("Japan", japan.loc[Date, "Japan Interbank Rate"]),
            ("Australia", australia.loc[Date, "Australia Interbank Rate"]),
            ("Netherlands", netherlands.loc[Date, "Netherlands Interbank Rate"]),
            ("Switzerland", switzerland.loc[Date, "Switzerland Interbank Rate"]),
            ("France", france.loc[Date, "France Interbank Rate"]),
            ("Canada", canada.loc[Date, "Canada Interbank Rate"]),
            ("Sweden", sweden.loc[Date, "Sweden Interbank Rate"]),
            ("United States", united_states.loc[Date, "United States Interbank Rate"]),
            ("United Kingdom", united_kingdom.loc[Date, "United Kingdom Interbank Rate"])
            ("Norway", norway.loc[Date, "Norway Interbank Rate"])
        ]
        sorted_rates = sorted(rates, key=lambda x: x[1])
        return sorted_rates
    except KeyError as err:  # Dataframe and Series give KeyError when the index is not matched.
        print(f"Error: Date {Date} not found in data - {err}")
    except ValueError as err:
        print(f"Error: {err}")
def show_ascending(list):
    for country, rate in list:
        print(f"{country} : {rate:.2f}")
    return   
print(give_largeSet())

"""if __name__ == "__main__": 
 print(give_ascending())

"""