import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
world_happiness= pd.read_csv('world_happiness.csv')
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp',y='happiness_score',data=world_happiness,ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()
  
# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor)