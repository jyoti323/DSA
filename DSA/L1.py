rows=3
cols=4
firstMatrix=[]

for i in range(rows):
    rowArray=[]
    for j in range(cols):
        rowArray.append(int(input("Enter the value of the matrix: ")))
    firstMatrix.append(rowArray)

print(firstMatrix)


#traversal of matrix
# fatching all elements of the matrix

for i in range(rows):
    for j in range(cols):
        print(firstMatrix[i][j],end=" ")
    print()

#col - wise traversal of the matrix

for i in range(cols):
    for j in range(rows):
        print(firstMatrix[j][i],end=" ")
    print()
