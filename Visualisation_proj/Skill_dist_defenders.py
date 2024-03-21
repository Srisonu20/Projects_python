# Plot Defensive Skills Distribution for any Defender
from matplotlib import pyplot as plt
import seaborn as sns

from Raiders import kabaddi_data

plt.figure(figsize=(10, 6))
sns.countplot(data=kabaddi_data, x='Defensive_Skill', hue='Defender_1_Name', palette='plasma')
plt.xlabel('Defensive Skill')
plt.ylabel('Counts')
plt.title('Defensive Skills Distribution for any Defender')
plt.legend(title='Defender Name', bbox_to_anchor=(1, 1))
plt.show()