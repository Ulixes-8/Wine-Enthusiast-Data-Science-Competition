import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/ulixe/OneDrive/Desktop/Python/FCA/wine_top_3_wines.csv")

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

# Get the number of unique varieties
print("Number of unique varieties: ", len(data.variety.unique()))

# Get the number of non-unique varieties
print("Number of non-unique varieties: ", len(data.variety) - len(data.variety.unique()))

# Get the number of unique titles
print("Number of unique titles: ", len(data.title.unique()))

# Get the number of non-unique titles
print("Number of non-unique titles: ", len(data.title) - len(data.title.unique()))

# Initalize standard deviation of price
std_price = data.price.std()

# Print Standard Deviation and Mean Price
print("Standard deviation of price: ", std_price)
print("Mean price: ", data.price.mean())
print("Median price: ", data.price.median())

# Initialize mean price
mean_price = data.price.mean()

# Plot distplot of prices
sns.distplot(data.price[data.price < 500])
plt.show()

# Plot distplot of points
sns.distplot(data.points)
plt.show()

# Print Mean and Median points
print("Mean points: ", data.points.mean())
print("Median points: ", data.points.median())

# Print Standard Deviation of points
print("Standard deviation of points: ", data.points.std())

# Sort data by points
data = data.sort_values(by=['points'], ascending=False)

# Iterate through each row in data
best_bottles = []
for i in range(len(data)):
    if len(best_bottles) < 3:
        # Check that price satisfies the stated condition
        if (data.price.values[i] > mean_price - std_price * 0.5) and (data.price.values[i] < mean_price + std_price * 0.5):
            # Check that title and variety are both not already in best_bottles
            if data.title.values[i] not in best_bottles:
                if data.variety.values[i] not in best_bottles:
                    # Append the title to best_bottles 
                    best_bottles.append(data.title.values[i])
    # Break from loop after 3 bottles have been added
    else:
        break

# Print the best bottles
print("The best bottles are: ")
for bottle in best_bottles:
    print(bottle)
    print("Variety: ", data[data.title == bottle].variety.values[0])
    print("Points: ", data[data.title == bottle].points.values[0])
    print("Price: ", data[data.title == bottle].price.values[0])