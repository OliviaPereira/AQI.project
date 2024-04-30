#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore probability distributions

# ## **Introduction**

# The ability to determine which type of probability distribution best fits data, calculate z-score, and detect outliers are essential skills in data work. These capabilities enable data professionals to understand how their data is distributed and identify data points that need further examination.
# In this activity, you are a member of an analytics team for the United States Environmental Protection Agency (EPA). The data includes information about more than 200 sites, identified by state, county, city, and local site names. One of your main goals is to determine which regions need support to make air quality improvements. Given that carbon monoxide is a major air pollutant, you will investigate data from the Air Quality Index (AQI) with respect to carbon monoxide.

# ## **Step 1: Imports** 

# Import relevant libraries, packages, and modules. For this lab, you will need `numpy`, `pandas`, `matplotlib.pyplot`, `statsmodels.api`, and `scipy`.


# Import relevant libraries, packages, and modules.

### YOUR CODE HERE ###

import numpy as np
import pandas as pd
import matplotlib.plypot as plt
import statsmodels.api as sm


# A subset of data was taken from the air quality data collected by the EPA, then transformed to suit the purposes of this lab. This subset is a .csv file named `modified_c4_epa_air_quality.csv`. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.


### YOUR CODE HERE ###
data = pd.read_csv("modified_c4_epa_air_quality.csv")




# ## **Step 2: Data exploration** 

# Display the first 10 rows of the data to get a sense of how the data is structured.

# Display first 10 rows of the data.

### YOUR CODE HERE ###
data.head(10)




# The `aqi_log` column represents AQI readings that were transformed logarithmically to suit the objectives of this lab. Taking a logarithm of the aqi to get a bell-shaped distribution is outside the scope of this course, but is helpful to see the normal distribution.

# To better understand the quantity of data you are working with, display the number of rows and the number of columns.




# Display number of rows, number of columns.

### YOUR CODE HERE ###
print(data.shape)




# Create a histogram to visualize distribution of aqi_log.

### YOUR CODE HERE ###
data["aqi_log"].hist();



# The `hist()` function can be called directly on the `aqi_log` column from the data.
# A semicolon can be used at the end as a quick way to make sure only the plot gets displayed (other text does not get displayed).


# **Question:** What do you observe about the shape of the distribution from the histogram?
# The shape still comes across as a bell although it seems tilted. The bell shape tells me the data span is quite normal.



# ## **Step 3: Statistical tests**

# Use the empirical rule to observe the data, then test and verify that it is normally distributed.


#  As you have learned, the empirical rule states that, for every normal distribution: 
# - 68% of the data fall within 1 standard deviation of the mean
# - 95% of the data fall within 2 standard deviations of the mean
# - 99.7% of the data fall within 3 standard deviations of the mean


# First, define two variables to store the mean and standard deviation, respectively, for `aqi_log`. Creating these variables will help you easily access these measures as you continue with the calculations involved in applying the empirical rule. 



# Define variable for aqi_log mean.

### YOUR CODE HERE ###
mean_aqi_log = data["aqi_log"].mean()


# Print out the mean.

### YOUR CODE HERE ###
print(mean_aqi_log)



# Define variable for aqi_log standard deviation.

### YOUR CODE HERE ###
std_aqi_log = data["aqi_log"].std()



# Print out the standard deviation.

### YOUR CODE HERE ###
print(std_aqi_log)





# Now, check the first part of the empirical rule: whether 68% of the `aqi_log` data falls within 1 standard deviation of the mean.
# 
# To compute the actual percentage of the data that satisfies this criteria, define the lower limit (for example, 1 standard deviation below the mean) and the upper limit (for example, 1 standard deviation above the mean). This will enable you to create a range and confirm whether each value falls within it.


# Define variable for lower limit, 1 standard deviation below the mean.

### YOUR CODE HERE ###
lower_limit = mean_aqi_log - 1 * std_aqi_log


# Define variable for upper limit, 1 standard deviation above the mean.

### YOUR CODE HERE ###
upper_limit = mean_aqi_log + 1 * std_aqi_log



# Display lower_limit, upper_limit.

### YOUR CODE HERE ###
print(lower_limit, upper_limit)



# The lower limit here is $mean - 1 * std$.

# The upper limit here is $mean + 1 * std$.



# Display the actual percentage of data that falls within 1 standard deviation of the mean.

### YOUR CODE HERE ### 
((data["aqi_log"] >= lower_limit) & (data["aqi_log"] <= upper_limit)).mean() * 100






# Now, consider the second part of the empirical rule: whether 95% of the `aqi_log` data falls within 2 standard deviations of the mean.
# 
# To compute the actual percentage of the data that satisfies this criteria, define the lower limit (for example, 2 standard deviations below the mean) and the upper limit (for example, 2 standard deviations above the mean). This will enable you to create a range and confirm whether each value falls within it.




# Define variable for lower limit, 2 standard deviations below the mean.

### YOUR CODE HERE ###
lower_limit = mean_aqi_log - 2 * std_aqi_log



# Define variable for upper limit, 2 standard deviations below the mean.

### YOUR CODE HERE ###
upper_limit = mean_aqi_log + 2 * std_aqi_log



# Display lower_limit, upper_limit.

### YOUR CODE HERE ###
print(lower_limit, upper_limit)




# The lower limit here is $mean - 2 * std$.
# 
# The upper limit here is $mean + 2 * std$.




# Display the actual percentage of data that falls within 2 standard deviations of the mean.

### YOUR CODE HERE ### 
((data["aqi_log"] >= lower_limit) & (data["aqi_log"] <= upper_limit)).mean() * 100





# Define variable for lower limit, 3 standard deviations below the mean.

### YOUR CODE HERE ###
lower_limit = mean_aqi_log - 3 * std_aqi_log


# Define variable for upper limit, 3 standard deviations above the mean.

### YOUR CODE HERE ###
upper_limit = mean_aqi_log + 3 * std_aqi_log



# Display lower_limit, upper_limit.

### YOUR CODE HERE ###
print(lower_limit, upper_limit)



# Display the actual percentage of data that falls within 3 standard deviations of the mean.

### YOUR CODE HERE ### 
((data["aqi_log"] >= lower_limit) & (data["aqi_log"] <= upper_limit)).mean() * 100





# ## **Step 4: Results and evaluation** 

# **Question:** What results did you attain by applying the empirical rule? 

# 76.15% of the data falls within 1 standard deviation of the mean.
# 95.77% of the data falls within 2 standard deviation of the mean.
# 99.62% of the data falls within 3 standard deviations of the mean.

# **Question:** How would you use z-score to find outliers?
#To find outliers using the z-score:
# 1. Calculate the z-score for each data point, which tells us how far it is from the average.
# 2. Look for values with a z-score greater than 3 or less than -3. These are considered outliers because they're really far from the average.
# 3. Add a column called z_score to store these calculations, making it easy to spot outliers in the data.


# Compute the z-score for every `aqi_log` value. Then, add a column named `z_score` in the data to store those results.
# Compute the z-score for every aqi_log value, and add a column named z_score in the data to store those results.

### YOUR CODE HERE ###
data["z_score"] = stats.zscore(data["aqi_log"], ddof=1)

# edit from exemplar - ddof=degrees of freedom correction (sample vs. population)

# Display the first 5 rows to ensure that the new column was added.

### YOUR CODE HERE ###
data.head(5)


# Call the `zscore()` function and pass in the `aqi` column from the data.


# Identify the parts of the data where `aqi_log` is above or below 3 standard deviations of the mean.



# Display data where `aqi_log` is above or below 3 standard deviations of the mean

### YOUR CODE HERE ###
data[(data["z_score"] > 3) | (data["z_score"] < -3)]




# **Question:** What do you observe about potential outliers based on the calculations?
# West Phoenix is above 3 standard deviations of the mean, so the AQI is worse than the rest.


# **Question:** Why is outlier detection an important part of this project? 
# It is important because they can reveal incorrect measurements, and they can highlight parts of the data that need improvements.

# ## **Considerations**

# **What are some key takeaways that you learned during this lab?**
# Observing the shape of a histogram helps assess if data is normally distributed.
# Use the empirical rule to check for normal distribution.
# Z-score helps spot potential outliers in the data.


# **What summary would you provide to stakeholders? Consider the distribution of the data and which sites would benefit from additional research.**

# Based on the analysis, it seems that the air quality data follows a normal pattern. By crunching the numbers, we found out that the air quality at West Phoenix is worse compared to the other locations. It might be a good idea to focus more attention on this site to figure out how we can make the air better there.

# **Reference**
# 
# US EPA, OAR. 2014, July 8. [Air Data: Air Quality Data Collected at Outdoor Monitors Across the US](https://www.epa.gov/outdoor-air-quality-data). 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
