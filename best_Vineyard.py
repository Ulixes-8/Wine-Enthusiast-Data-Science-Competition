import pandas as pd

data = pd.read_csv("C:/Users/ulixe/OneDrive/Desktop/Python/FCA/wine_W_V.csv")

# Function to remove bad examples from data
def removeBadExamples(data):
    """
    Remove data that has points value of 0 or 150, these are considered outliers 
    and would bias the results
    """
    
    count = len(data) # get initial length of data
    data = data[data.points != 150] # remove points with value of 150
    data = data[data.points != 0] # remove points with value of 0
    count2 = len(data) # recount data lenght
    print("Removed ", count - count2, " bad examples") # print how many bad examples removed
    return data # return the processed data

# Output shape of data before bad example filter
print("Before removing bad examples: ", data.shape)

# Run the data through the removeBadExample filter
data = removeBadExamples(data)

# Output shape of data after bad example filter
print("After removing bad examples: ", data.shape)

# Function to remove missing values
def handleMissingValues(data):
    """
    Drop any missing values that may exist
    """
    
    count = len(data) # Get initial length of data
    data = data.dropna() # Drop all missing values
    count2 = len(data) # Recount data length
    print("Removed ", count - count2, " missing values") # Print how many values were dropped
    return data # Return the processed data

# Output shape of data before missing value filter
print("Before removing missing values: ", data.shape)

# Run the data through the handleMissingValue filter
data = handleMissingValues(data)

# Output shape of data after missing value filter
print("After removing missing values: ", data.shape)

# Output number of vineyards that belong to more than one winery
print("Number of vineyards that belong to more than one winery: ", 
      len(data[data.duplicated(subset=['designation', 'winery'])]))

# Output number of vineyards that belong to only one winery
print("Number of vineyards that belong to only one winery: ", 
      len(data[~data.duplicated(subset=['designation', 'winery'])]))

# Output total number of vineyards
print("Number of vineyards: ", len(data.designation))

# Compute average count for designations
print("Average count for designations: ", data.designation.value_counts().mean())
avg_designation_count = data.designation.value_counts().mean()

# Get counts and mean points for designations
designations = data.groupby('designation').agg({'points': ['count', 'mean']})

# Change column names
designations.columns = ['count', 'mean']

# Sort values and output top 10 designations
designations = designations.sort_values(by=['count'], ascending=False)
print(designations.sort_values(by=['count'], ascending=False).head(10))

# Get only designations with count greater than 4 times the average
designations = designations[designations['count'] > 4 * avg_designation_count]

# Sort values and output top 10 designations
top_vineyards = designations.sort_values(by=['mean'], ascending=False).head(10)
print(top_vineyards)

# Check if does the first element belongs to only one winery
print("Does the first element in the top vineyards list belong to only one winery? ", 
      len(data[data.designation == top_vineyards.index.values[0]].winery.unique()) == 1)

# Find best vineyard which is belong to only one winery
best_vineyard = ""
for vineyard in top_vineyards.index.values:
    if len(data[data.designation == vineyard].winery.unique()) == 1:
        best_vineyard = vineyard
        break
print("The best vineyard is: ", best_vineyard)
