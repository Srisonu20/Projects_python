import seaborn as sns
from matplotlib import pyplot as plt

from Raiders import kabaddi_data

# Plot Attacking Skills Distribution for any Raider
plt.figure(figsize=(10, 6))
sns.countplot(data=kabaddi_data, x='Attacking_Skill', hue='Raider_Name', palette='viridis')
plt.xlabel('Attacking Skill')
plt.ylabel('Counts')
plt.title('Attacking Skills Distribution for any Raider')
plt.legend(title='Raider Name', bbox_to_anchor=(1, 1))
plt.show()