import sys

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices in the chain
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example Usage
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of scalar multiplications:", m[1][len(matrix_dimensions) - 1])
print("Optimal Parenthesization: ", end="")
print_optimal_parens(s, 1, len(matrix_dimensions) - 1)
