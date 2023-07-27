

# Importing the necessary python libraries (data wrangling and visualisation)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def eligibilityCheck(reason):
    if reason == "Clean Alternative Fuel Vehicle Eligible":
        return "Yes"
    elif reason == "Not eligible due to low battery range":
        return "No"
    else:
        return "Eligibility unknown as battery range has not been researched"
    
    
    
# Importing the dataset
rawdataframe = pd.read_csv('./dataset/Electric_Vehicle_Population_Data.csv')


# Get some summary statistics of the dataset
# print(rawdataframe.describe())


# Check the null values and the dimensions of the data now
# rawdataframe.shape
# rawdataframe.isnull().sum()


# Step-Iterate over the rows in the DataFrame
for index, row in rawdataframe.iterrows():
    if pd.isnull(row["Postal Code"]):
        print(row)
        print(index)


# coincidently we find that the 3 rows posses lot of null values.
locateddataframe = rawdataframe[~pd.isnull(rawdataframe["Postal Code"])]
# locateddataframe.isnull().sum()


# Repeating the Step-Iterate over the rows in the DataFrame
for index, row in rawdataframe.iterrows():
    if pd.isnull(row["Vehicle Location"]):
        print(row)
        print(index)
        


vehicledataframe = rawdataframe[~pd.isnull(rawdataframe["Vehicle Location"])]
vehicledataframe.isnull().sum()



# Convert the floating point value to an integer / string
vehicledataframe['Postal Code'] = vehicledataframe['Postal Code'].astype(int)

# Replace NaN with 0
vehicledataframe = vehicledataframe.fillna(0)
vehicledataframe['Legislative District'] = vehicledataframe['Legislative District'].astype(int)

# Column '2020 Census has big value so we consider it as string and then handle the formatting
vehicledataframe["2020 Census Tract"] = vehicledataframe["2020 Census Tract"].astype(str).str[:-2]



# standardizing the data and formatting as appropriate
std_EV_type = vehicledataframe['Electric Vehicle Type'].str.extract(r'\((.*?)\)')
vehicledataframe['Electric Vehicle Type'] = std_EV_type


# distinct_values = rawdataframe['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].unique()
# distinct_values
    
   
vehicledataframe['CAFV Eligibility'] = vehicledataframe['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].apply(eligibilityCheck)
# vehicledataframe.head(10)


# Get the POINT data from the column
column_data = vehicledataframe['Vehicle Location']


# Split the POINT data into two columns
latitude_column = column_data.str.split(' ').str[1].str[1:]
longitude_column = column_data.str.split(' ').str[2].str[:-1]
# print(latitude_column)
# print(longitude_column)


# Add the two new columns to the DataFrame
vehicledataframe['latitude'] = latitude_column
vehicledataframe['longitude'] = longitude_column



# Iterate over the rows in the DataFrame
for index, row in rawdataframe.iterrows():
    if pd.isnull(row["PostCode"]):
        pass
    else:
        row['Postal Code'] = row['Postal Code'].astype(int)
        
    

    