import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("trai_data.csv")
#Sort by total subscribers
df_sorted = df.sort_values('Total_Subscribers', ascending=False).head(10)

#Create a bar chart 
plt.figure(figsize=(12,6))
plt.bar(df_sorted['Service_Area'],df_sorted['Total_Subscribers'])
plt.xlabel('State')
plt.ylabel('Total Subscribers (millions)')
plt.title('Top 10 States by Total Telecom Subscribers (march 2026)')
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.savefig('subscribers_by_state.png')
print('chart saved as subscribers_by_state.png')