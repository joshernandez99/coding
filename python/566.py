def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:

    # Get the data
    matrixData = []
    for x in mat:
        for y in x:
            matrixData.append(y)

    # Edge Case
    if len(matrixData) != ( r * c ) or (r * c) == 1:
        return mat
    
    # Now reshape
    newMatrix = []
    dataTracker = 0
    for x in range(r):
        tempMatrix = []
        for y in range(c):
            tempMatrix.append(matrixData[dataTracker])
            dataTracker += 1
        newMatrix.append(tempMatrix)
    return newMatrix


print(matrixReshape([[1,2],[3,4]], 1 , 4))
print(matrixReshape([[1,2],[3,4]], 2 , 4))
print(matrixReshape([[1,2],[3,4],[5,6],[7,8]], 2 , 4))