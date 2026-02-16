#Diagonal traversal
#primary diagonal: (row index=column index)

from matplotlib.pylab import matrix
from pyparsing import col


rows=3
for i in range(rows):
    print(matrix[i][i])

#Secoundary diagonal: ro index+column=total no rows-1

c=cols-1
for i in range(rows):
    print(matrix[i][c])
    c-=1


