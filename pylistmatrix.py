m1 = [[1, 3],
      [2, 4]]
m2 = [[5, 2], 
      [1, 0]]
result = [[0, 0],
          [0, 0]]

for i in range(len(m1)):
    for n in range(len(m1[0])):
        result[i][n] = m1[i][n] + m2[i][n]
        
for r in result:
    print(r)