import pandas as pd

data = pd.read_csv("C:/Users/ulixe/OneDrive/Desktop/Python/FCA/wine_dry_citrus.csv")

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
# Print number of unique varieties and descriptions 
print("Number of unique varieties: ", len(data.variety.unique()))
print("Number of unique descriptions: ", len(data.description.unique()))
print("Number of non-unique descriptions: ", len(data.description) - len(data.description.unique()))

# Print variety counts for duplicate descriptions 
print(data[data.description.duplicated()].variety.value_counts())

# Remove duplicate description entries 
print("before removing duplicates: ", data.shape)
data = data.drop_duplicates(subset = "description")
print("after removing duplicates: ", data.shape)

# Function to check if a description contains both 'dry' and 'citrus'
def isDryCitrus(description):
    if "dry" in description and "citrus" in description:
        return 1
    else:
        return 0

# Select only descriptions that include the words 'dry' and 'citrus'
dry_and_citrus = data[data.description.apply(isDryCitrus) == 1]

# Print number of dry and citrus wines
print("Number of dry and citrus wines: ", len(dry_and_citrus))

# Select top 5 varieties for dry and citrus wines
dry_and_citrus = dry_and_citrus.variety.value_counts().head(5)

# Print top 5 varieties of dry and citrus wines
print(dry_and_citrus)

# Select recommended variety from the top 5
recommended_variety = dry_and_citrus.index[0]

# Print recommended variety
print("Recommended variety: ", recommended_variety)
