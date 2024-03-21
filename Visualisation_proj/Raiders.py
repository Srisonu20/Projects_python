import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde



# Load the dataset
kabaddi_data = pd.read_csv(r'C:\My_PersonaL\sonu docs\New folder\Sport_Kabbaddi.csv')


# Distribution of Raids for any Raider
raider_counts = kabaddi_data['Raider_Name'].value_counts()
raider_percentages = raider_counts / raider_counts.sum() * 100

# Plot
plt.figure(figsize=(10, 6))
raider_counts.plot(kind='bar', color='#4254f5',alpha = 0.9, label='Counts')
plt.xlabel('Raider Name')
plt.ylabel('Counts')
plt.title('Distribution of Raids for any Raider')
plt.legend()
plt.show()

# ('line', 'bar', 'barh', 'kde', 'density', 'area', 'hist', 'box', 'pie', 'scatter', 'hexbin') alpha=0.7,
