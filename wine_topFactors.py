import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/ulixe/OneDrive/Desktop/Python/FCA/wine_top_factors.csv")

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

#Separate dependent and independent variables
y = data.iloc[:, -1] # Dependent variable is on the last column
X = data.iloc[:, :-1] # Independent variables are on all columns except the last one
features = list(X.columns) # Create list of features (column names)

# Function for counting unique values in each feature
def countUniqueValues(data, features):
    for feature in features:
        print(feature, " has ", data[feature].nunique(), " unique values")

# Call function used to get unique values count
countUniqueValues(X, features)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() # Initialize label encoder object
for feature in features:
    X[feature] = labelencoder.fit_transform(X[feature]) # Apply encoding to all feature columns

#Create Random Forest Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X, y)
importances = model.feature_importances_

# Transform numpy array into Pandas DataFrame
final_df = pd.DataFrame({"Features": pd.DataFrame(X).columns, "Importances":importances})
final_df.set_index("Importances") # Set index of DataFrame

# Sort values based on Importance (descending order)
final_df = final_df.sort_values("Importances", ascending=False)

# Plot data using bar graph
final_df.plot.bar(color = 'teal')
print(final_df.to_string()) #Print table containing Features and their importance

# Add graphical properties to the plot
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks([0, 1, 2, 3], ["price", "variety", "taster_name", "country"])
plt.show() # Show the plot
