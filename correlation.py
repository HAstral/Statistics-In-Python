import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
world_happiness= pd.read_csv('world_happiness.csv')
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp',y='happiness_score',data=world_happiness,ci=None)

# Show plot
plt.show()