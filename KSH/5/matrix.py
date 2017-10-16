# python "/Users/gimseonghun/Desktop/study-python/KSH/5/matrix.py"
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)]) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

tempMatrix = []

for i in range(4):
    tempMatrix.append([])
    for row in matrix:
        tempMatrix[i].append(row[i])
print(tempMatrix) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

del tempMatrix[0]
print(tempMatrix) # [[2, 6, 10], [3, 7, 11], [4, 8, 12]]