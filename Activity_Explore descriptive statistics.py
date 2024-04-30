#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore descriptive statistics

# ## **Introduction**
# Data professionals often use descriptive statistics to understand the data they are working with and provide collaborators with a summary of the relative location of values in the data, as well an information about its spread.
# For this activity, you are a member of an analytics team for the United States Environmental Protection Agency (EPA). You are assigned to analyze data on air quality with respect to carbon monoxide, a major air pollutant. The data includes information from more than 200 sites, identified by state, county, city, and local site names. You will use Python functions to gather statistics about air quality, then share insights with stakeholders.

# ## **Step 1: Imports** 


# Import the relevant Python libraries `pandas` and `numpy`.


# Import relevant Python libraries.

### YOUR CODE HERE ###
import pandas as pd
import numpy as np


# The dataset provided is in the form of a .csv file named `c4_epa_air_quality.csv`. It contains a subset of data from the U.S. EPA. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.





### YOUR CODE HERE
epa_data = pd.read_csv("c4_epa_air_quality.csv", index_col = 0)


#   There is a function in the `pandas` library that allows you to read in data from a .csv file and load it into a DataFrame. 

#   Use the `read_csv` function from the pandas `library`. The `index_col` parameter can be set to `0` to read in the first column as an index (and to avoid `"Unnamed: 0"` appearing as a column in the resulting DataFrame).


# ## **Step 2: Data exploration** 

# To understand how the dataset is structured, display the first 10 rows of the data.




# Display first 10 rows of the data.

### YOUR CODE HERE
epa_data.head(10)


#   There is a function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame. 


#   Use the `head()` function from the `pandas` library.


# **Question:** What does the `aqi` column represent?
# It represents the EPA's AQI.



# Now, get a table that contains some descriptive statistics about the data.


# Get descriptive stats.

### YOUR CODE HERE
epa_data.describe()



#   There is a function in the `pandas` library that allows you to generate a table of basic descriptive statistics about the numeric columns in a DataFrame.



# **Question:** Based on the table of descriptive statistics, what do you notice about the count value for the `aqi` column?
# There are 260 representations of AQI in the dataset.

# **Question:** What do you notice about the 25th percentile for the `aqi` column?
#  You can use this measurement to determine where the values lie.

# **Question:** What do you notice about the 75th percentile for the `aqi` column?
# Like the previous question, it allows me to see where the values lie.



# ## **Step 3: Statistical tests** 

# Next, get some descriptive statistics about the states in the data.




# Get descriptive stats about the states in the data.

### YOUR CODE HERE
epa_data["state_name"].describe()



#   There is a function in the `pandas` library that allows you to generate basic descriptive statistics about a DataFrame or a column you are interested in.


#  Use the `describe()` function from the `pandas` library. Note that this function can be used:
# - "on a DataFrame (to find descriptive statistics about the numeric columns)" 
# - "directly on a column containing categorical data (to find pertinent descriptive statistics)"


# **Question:** What do you notice while reviewing the descriptive statistics about the states in the data? 
# There are 260 state values. California is the most repeated state reported in the data.

# Note: Sometimes you have to individually calculate statistics. To review to that approach, use the `numpy` library to calculate each of the main statistics in the preceding table for the `aqi` column.



# ## **Step 4. Results and evaluation**

# Now, compute the mean value from the `aqi` column.


### YOUR CODE HERE
np.mean(epa_data["aqi"])


#   There is a function in the `numpy` library that allows you to get the mean value from an array or a Series of values.

#   Use the `mean()` function from the `numpy` library.


# **Question:** What do you notice about the mean value from the `aqi` column?
# It's important to have so I am aware of what the average should be if I try to look for outliers, range etc.



# Next, compute the median value from the aqi column.


# Compute the median value from the aqi column.

### YOUR CODE HERE
np.median(epa_data["aqi"])



#   There is a function in the `numpy` library that allows you to get the median value from an array or a series of values.


# **Question:** What do you notice about the median value from the `aqi` column?
#  It shows me the middle value of the dataset which is 5.0.


# Next, identify the minimum value from the `aqi` column.

# Identify the minimum value from the aqi column.

### YOUR CODE HERE
np.min(epa_data["aqi"])


#   There is a function in the `numpy` library that allows you to get the minimum value from an array or a Series of values.

# **Question:** What do you notice about the minimum value from the `aqi` column?
# It shows me the smallest value which is 0.

# Now, identify the maximum value from the `aqi` column.


# Identify the maximum value from the aqi column.

### YOUR CODE HERE
np.max(epa_data["aqi"])


#   There is a function in the `numpy` library that allows you to get the maximum value from an array or a Series of values.


# **Question:** What do you notice about the maximum value from the `aqi` column?
# The maximum value is 50.


# Now, compute the standard deviation for the `aqi` column.

# By default, the `numpy` library uses 0 as the Delta Degrees of Freedom, while `pandas` library uses 1. To get the same value for standard deviation using either library, specify the `ddof` parameter to 1 when calculating standard deviation.


# Compute the standard deviation for the aqi column.

### YOUR CODE HERE
np.std(epa_data["aqi"], ddof=1)



#   There is a function in the `numpy` library that allows you to get the standard deviation from an array or a series of values.


# **Question:** What do you notice about the standard deviation for the `aqi` column? 
# It shows me how the data is spread out.


# ## **Considerations**

# **What are some key takeaways that you learned during this lab?**
# The foundations of understanding the dataset through the head, describe, min, max, median, and standard deviation methods.


# **How would you present your findings from this lab to others? Consider the following relevant points noted by AirNow.gov as you respond:**
# When AQI values are above 100, air quality is unhealthy for at risk individuals and then as it gets higher, it is unhealthy for everyone.
# From Exemplar - "An AQI of 100 for carbon monoxide corresponds to a level of 9.4 parts per million."



# **What summary would you provide to stakeholders? Use the same information provided previously from AirNow.gov as you respond.**
# 75% of the values provided are under 9 and can be classified as good quality, however for the 25%, further understanding to better the AQI is necessary, whether it's through green policies, funding for clean air movements etc.


# **References**
# 
# [Air Quality Index - A Guide to Air Quality and Your Health](https://www.airnow.gov/sites/default/files/2018-04/aqi_brochure_02_14_0.pdf). (2014,February)
# 
# [Numpy.Std — NumPy v1.23 Manual](https://numpy.org/doc/stable/reference/generated/numpy.std.html)
# 
# US EPA, OAR. (2014, 8 July).[*Air Data: Air Quality Data Collected at Outdoor Monitors Across the US*](https://www.epa.gov/outdoor-air-quality-data). 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
