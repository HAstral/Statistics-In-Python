import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
food_consumption = pd.read_csv("food_consumption.csv")
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var,np.std]))

# Create histogram of co2_emission for food_category 'beef'
food_consumption['co2_emission'][food_consumption['food_category']=='beef'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
plt.figure()
food_consumption['co2_emission'][food_consumption['food_category']=='eggs'].hist()
plt.show()

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0,0.25,0.5,0.75,1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0,1,6)))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0,1,11)))

