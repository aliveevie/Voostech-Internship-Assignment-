# The basic code for printing matrix
R = int(input('Enter the number of rows: '))
C = int(input('Enter the number of columns: '))

# Iniatilize matrix
matrix = []
print('Enter the elements of the matrix')

# For User input
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
# for priting the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
