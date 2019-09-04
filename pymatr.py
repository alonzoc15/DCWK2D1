DC = [[1, 2],
      [2, 3],
      [4, 5]]
TF = [[1, 2],
      [2, 3],
      [4, 5]]
result = [[0, 0],
          [0, 0],
          [0, 0]]

for i in range(len(DC)):
    for n in range(len(TF[0])):
        result[i][n] = DC[i][n] + TF[i][n]
        
for r in result:
    print(r)