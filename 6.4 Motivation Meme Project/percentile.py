import numpy as np

def calculate_percentile(arr, percentile):
    return np.percentile(arr, percentile)

# Example usage
arr = [3,5,8,8,9,11,12,12,13,13,16]
percentile_value = 75 # Median (50th percentile)
result = calculate_percentile(arr, percentile_value)
print(f"{percentile_value}th Percentile: {result}")
