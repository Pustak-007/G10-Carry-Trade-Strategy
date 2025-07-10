import pandas as pd 
import numpy as np 
from fredapi import Fred 
from datetime import datetime 
api_key = "23dd8644a8456a82f3dc0e07c51e2a9b"
fred = Fred(api_key = api_key)
start = pd.Timestamp(2002,1,2)
end = pd.Timestamp(2025,1,1)
daily_index = pd.date_range(start = start, end = end, freq = 'D')


# Function to retrieve interbank rates for Japan
def give_japanRate():
    try:
        data = fred.get_series("IR3TIB01JPM156N", start, end)
        df = data.to_frame(name="Japan Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        new_df.bfill(inplace = True)
        #We are doing this backwards fill only for japan because of incomplete Interbank data
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

#Function to retrieve interbank rates for New Zealand
def give_newzealandRate():
    try:
        data = fred.get_series("IR3TIB01NZM156N", start, end)
        df = data.to_frame(name="New Zealand Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

#Function to retrieve interbank rates for Europe
def give_europeRate():
    try:
        data = fred.get_series("IR3TIB01EZM156N", start, end)
        df = data.to_frame(name="Europe Interbank Rate")
        new_df = df.reindex(daily_index, method="ffill")
        new_df.index.name = "Date"
        return new_df
    except ValueError as err:
        print(f"Error: {err}")

#Storing each function's result in a variable
#Refer to this variable when you need the data - saves from redundant computation

japan = give_japanRate()
australia = give_australiaRate()
switzerland = give_switzerlandRate()
canada = give_canadaRate()
sweden = give_swedenRate()
united_states = give_unitedStatesRate()
united_kingdom = give_unitedKingdomRate()
norway = give_norwayRate()
newzealand = give_newzealandRate()
europe = give_europeRate()


# List of DataFrames for concatenation
concat_list = [ japan,australia, switzerland, canada,sweden,
    united_states,united_kingdom, norway, newzealand, europe
]

#temp, just for checking
concat_list2 = [newzealand, europe]

#Combination of all the prior dataframes - The Large set
def give_largeSet():
    df = pd.concat(concat_list, axis = 1)
    return df
Large_Interbank_Set = give_largeSet()
date_for_ascen = datetime(2002,1,1)
def give_ascending(Date):
    try:
        # List to store (country, rate) tuples
        rates = [
            ("Japan", japan.loc[Date, "Japan Interbank Rate"]),
            ("Australia", australia.loc[Date, "Australia Interbank Rate"]),
            ("Switzerland", switzerland.loc[Date, "Switzerland Interbank Rate"]),
            ("Canada", canada.loc[Date, "Canada Interbank Rate"]),
            ("Sweden", sweden.loc[Date, "Sweden Interbank Rate"]),
            ("United States", united_states.loc[Date, "United States Interbank Rate"]),
            ("United Kingdom", united_kingdom.loc[Date, "United Kingdom Interbank Rate"]),
            ("Norway", norway.loc[Date, "Norway Interbank Rate"]),
            ("Europe", europe.loc[Date, "Europe Interbank Rate"]),
            ("New Zealand", newzealand.loc[Date, "New Zealand Interbank Rate"])
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
big_storage = pd.DataFrame()
big_storage.index = daily_index
big_storage['Ascending_Data_for_Portfolio'] = big_storage.index.to_series().apply(give_ascending)




if __name__ == "__main__":
    #print(big_storage['Ascending_Data_for_Portfolio'])
    #print(big_storage)
    print(Large_Interbank_Set)
