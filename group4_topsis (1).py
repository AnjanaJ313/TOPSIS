import pandas as pd
import numpy as np

# defining the input data
data = pd.DataFrame({
    'Route': ['A', 'B', 'C', 'D'],
    'Distance': [10000, 9500, 9000, 9200],
    'Weather': [7, 9, 2, 6],
    'Port facilities': [8, 7, 9, 6],
    'Shipping traffic': [6, 7, 8, 9]
})

# defining the weights and impact of each criterion
weights = [0.25, 0.25, 0.25, 0.25]
impact = [-1, 1, 1, -1]  # 'Distance' and 'Shipping traffic' are cost criteria

# normalizing the data
normalized = data.iloc[:, 1:].apply(lambda x: x / np.sqrt(sum(x**2)), axis=0)

# applying the weights and impact to the normalized data
weighted = normalized.apply(lambda x: x * weights* impact , axis=1)

# calculating the ideal and negative ideal solutions
ideal = weighted.max()
negative_ideal = weighted.min()

# calculating the distance to ideal and negative ideal solutions
distance_ideal = np.sqrt(((weighted - ideal) ** 2).sum(axis=1))
distance_negative_ideal = np.sqrt(((weighted - negative_ideal) ** 2).sum(axis=1))

# calculating the closeness coefficient
closeness = distance_negative_ideal / (distance_ideal + distance_negative_ideal)

# adding the closeness coefficient to the original data
data['Closeness'] = closeness

# sorting the data by closeness coefficient in descending order
sorted_data = data.sort_values(by='Closeness', ascending=False)

print(sorted_data)
