import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
# Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)):
  for j in range(len(Prices[0])):
    res1 = ((Prices[0,0])*(Total[0])) + ((Prices[0,1])*(Total[1]))
    res2 = ((Prices[1,0])*(Total[0])) + ((Prices[1,1])*(Total[1]))

print(res1, res2)
