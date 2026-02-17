def matrixSum(matA, matB):
    result = []
    for i in range(len(matA)):
        for j in range(len(matA[i])):
            result.append(matA[i][j] + matB[i][j])

        print(f"{result} ",end="\n")

matA=[[1,2],
      [3,4]]
matB=[[1,2],
      [3,4]]
matrixSum(matA, matB)
