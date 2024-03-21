import matplotlib.pyplot as plt
import pandas as pd

from Raiders import kabaddi_data

# Distribution of Tackles for any Defender
defender_counts = kabaddi_data['Defender_1_Name'].value_counts()
defender_percentages = defender_counts / defender_counts.sum() * 100

# Plot
plt.figure(figsize=(10, 6))
defender_counts.plot(kind='bar', color='salmon', alpha=0.7, label='Counts')
plt.xlabel('Defender Name')
plt.ylabel('Counts')
plt.title('Distribution of Tackles for any Defender')
plt.legend()
plt.show()