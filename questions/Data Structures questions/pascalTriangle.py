n = int(input("Enter the height of the Pascal's Triangle: "))
matrix = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
    matrix.append(row)


def print_triangle(matrix):
    n = len(matrix)
    for i in range(n):
        print(" " * (n - i), matrix[i])

print_triangle(matrix)