#!/usr/bin/env python
# coding: utf-8

# # Activity: Explore confidence intervals

# ## Introduction

# The Air Quality Index (AQI) is the Environmental Protection Agency's index for reporting air quality. A value close to 0 signals little to no public health concern, while higher values are associated with increased risk to public health. The United States is considering a new federal policy that would create a subsidy for renewable energy in states observing an average AQI of 10 or above. <br>
# 
# You've just started your new role as a data analyst in the Strategy division of Ripple Renewable Energy (RRE). **RRE operates in the following U.S. states: `California`, `Florida`, `Michigan`, `Ohio`, `Pennsylvania`, `Texas`.** You've been tasked with constructing an analysis which identifies which of these states are most likely to be affected, should the new federal policy be enacted.

# Your manager has requested that you do the following for your analysis:
# 1. Provide a summary of the mean AQI for the states in which RRE operates.
# 2. Construct a boxplot visualization for AQI of these states using `seaborn`.
# 3. Evaluate which state(s) may be most affected by this policy, based on the data and your boxplot visualization.
# 4. Construct a confidence interval for the RRE state with the highest mean AQI.

# ## Step 1: Imports
# 
# ### Import packages
# 
# Import `pandas` and `numpy`.



# Import relevant packages

### YOUR CODE HERE ###
import pandas as pd
import numpy as np

# ### Load the dataset
# 
# The dataset provided gives national Air Quality Index (AQI) measurements by state over time.  `Pandas` is used to import the file `c4_epa_air_quality.csv` as a DataFrame named `aqi`. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 
# *Note: For the purposes of your analysis, you can assume this data is randomly sampled from a larger population.*



# RUN THIS CELL TO IMPORT YOUR DATA

### YOUR CODE HERE ###
aqi = pd.read_csv('c4_epa_air_quality.csv')


# ## Step 2: Data exploration

# ### Explore your dataset
# 
# Before proceeding to your deliverables, spend some time exploring the `aqi` DataFrame. 



# Explore your DataFrame `aqi`.

### YOUR CODE HERE ###
print("Use describe() to summarize AQI")

print(aqi.describe(include='all'))

print("For a more thorough examination of observations by state use␣ ,→values_counts()")

print(aqi['state_name'].value_counts())

# **Question:** What time range does this data cover?
# 2018-01-01 
# 

# **Question:** What are the minimum and maximum AQI values observed in the dataset?
# min: 0 
# max: 50

# **Question:** Are all states equally represented in the dataset?
# No, all states are not equally represented. Some states have only reported 1, 2, 3 (and so on) AQIs whereas Arizona has reported 14 and California reported 66.




# ## Step 3: Statistical tests
# 
# ### Summarize the mean AQI for RRE states
# 
# Start with your first deliverable. Summarize the mean AQI for the states in which RRE operates (California, Florida, Michigan, Ohio, Pennsylvania, and Texas).




# Summarize the mean AQI for RRE states.

# Create a list of RRE states.
rre_states = ['California', 'Florida', 'Michigan', 'Ohio', 'Pennsylvania', 'Texas']


# Subset `aqi` to only consider these states.
aqi_rre = aqi[aqi['state_name'].isin(rre_states)]


# Find the mean aqi for each of the RRE states.
aqi_rre.groupby(['state_name']).agg({"aqi":"mean", "state_name":"count"})





# ### Construct a boxplot visualization for the AQI of these states
# 
# Seaborn is a simple visualization library, commonly imported as `sns`. Import `seaborn`. Then utilize a boxplot visualization from this library to compare the distributions of AQI scores by state.




# Import seaborn as sns.

### YOUR CODE HERE ###
import seaborn as sns



# ### Create an in-line visualization showing the distribution of `aqi` by `state_name`
# 
# Now, create an in-line visualization showing the distribution of `aqi` by `state_name`.


### YOUR CODE HERE ###
sns.boxplot(x=aqi_rre["state_name"],y=aqi_rre["aqi"])



# **Question:** Based on the data and your visualizations, which state(s) do you suspect will be most affected by this policy?

#California, not just a large portion of the boxplot but also the mean ranges over ten.
#With this idea, Michigan may also be affected to a high extent as their boxplot is also over ten.




# ### Construct a confidence interval for the RRE state with the highest mean AQI
# 
# Recall the 4-step process in constructing a confidence interval:
# 
# 1.   Identify a sample statistic.
# 2.   Choose a confidence level.
# 3.   Find the margin of error. 
# 4.   Calculate the interval.


# ### Construct your sample statistic
# 
# To contruct your sample statistic, find the mean AQI for your state.


# Find the mean aqi for your state.

### YOUR CODE HERE ###
aqi_ca = aqi[aqi['state_name']=='California']

sample_mean = aqi_ca['aqi'].mean()
print(sample_mean)





# ### Choose your confidence level
# 
# Choose your confidence level for your analysis. The most typical confidence level chosen is 95%; however, you can choose 90% or 99% if you want decrease or increase (respectively) your level of confidence about your result.




# Input your confidence level here:

### YOUR CODE HERE ###
confidence_level = 0.95
confidence_level


# ### Find your margin of error (ME)
# 
# Recall **margin of error = z * standard error**, where z is the appropriate z-value for the given confidence level. To calculate your margin of error:
# 
# - Find your z-value. 
# - Find the approximate z for common confidence levels.
# - Calculate your **standard error** estimate. 
# 
# | Confidence Level | Z Score |
# | --- | --- |
# | 90% | 1.65 |
# | 95% | 1.96 |
# | 99% | 2.58 |
# 



# Calculate your margin of error.


# Begin by identifying the z associated with your chosen confidence level.
z_value = 1.96

# Next, calculate your standard error.
standard_error = aqi_ca['aqi'].std() / np.sqrt(aqi_ca.shape[0])

print("standard error:")

print(standard_error)

# Lastly, use the preceding result to calculate your margin of error.
margin_of_error = standard_error * z_value

print("margin of error:")

print(margin_of_error)


# ### Calculate your interval
# 
# Calculate both a lower and upper limit surrounding your sample mean to create your interval.




# Calculate your confidence interval (upper and lower limits).

### YOUR CODE HERE ###
upper_ci_limit = sample_mean + margin_of_error
lower_ci_limit = sample_mean - margin_of_error
(lower_ci_limit, upper_ci_limit)





# ### Alternative: Construct the interval using `scipy.stats.norm.interval()`
# 
# `scipy` presents a simpler solution to developing a confidence interval. To use this, first import the `stats` module from `scipy`.



# Import stats from scipy.

### YOUR CODE HERE ###
from scipy import stats



# ## Step 4: Results and evaluation
# 
# ### Recalculate your confidence interval
# 
# Provide your chosen `confidence_level`, `sample_mean`, and `standard_error` to `stats.norm.interval()` and recalculate your confidence interval.




### YOUR CODE HERE ###
stats.norm.interval(alpha=confidence_level, loc=sample_mean,␣ ,→scale=standard_error)


# # Considerations
# 
# **What are some key takeaways that you learned from this lab?**
# 
# more questions regarding the AQI's that were reported, how different would the graph look with more evenly collected data.
# Californa and Michigan may currently be effected the most by the possible policy change.

# **What findings would you share with others?**
# 
# The results I collected from the confidence interval. Just to provide my process and get tips on whether or not there are better ways, alternative ways in constructing accurate results.
# and determine whether or not their version will also yeild a confidence level of between 10.36 and 13.88 for California.
#I may also try changing the confidence level to show the varied results and find best practices to move forward.

# 
# **What would you convey to external stakeholders?**
# 
# I would explain the significance of the stats produced in a way they are able to fully understand and ask further questions.
# I would talk about the results collected on California and discuss potential focus on the state as they are most likely to be effected.
# I would also discuss the imbalance of data collected for the data analysis and the short timeframe, suggesting there can be more EDA performed if time and further data is obtained.



# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
