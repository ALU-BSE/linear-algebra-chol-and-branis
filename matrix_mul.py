#Maltiplication of Matrices
Prices = [[300, 500],
          [1000, 120.85]]

Total = [200, 100]


#Looping through

for i in range(len(Prices)):
  for j in range(len(Prices[0])):
    res1 = ((Prices[0][0])*(Total[0])) + ((Prices[0][1])*(Total[1]))
    res2 = ((Prices[1][0])*(Total[0])) + ((Prices[1][1])*(Total[1]))

print(res1, res2)


