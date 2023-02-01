import sys

n = int(sys.stdin.readline())
p = 1000000007

matrix = [[1, 1], [1, 0]]

def matrix_multiplication(A, B):
    tmp_matrix = [[0, 0], [0, 0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp_matrix[i][j] += A[i][k] * B[k][j]

            tmp_matrix[i][j] %= p

    return tmp_matrix


def recursive(A, c):
    if c == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= p

        return A

    else:
        tmp = recursive(A, c // 2)

        if c % 2 == 0:
            return matrix_multiplication(tmp, tmp)
        else:
            return matrix_multiplication(matrix_multiplication(tmp, tmp), A)

print(recursive(matrix, n)[0][1])
