import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

from Strassen.trad_mm import gen_matrix


# Function to add two matrices
def add(A, B):
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

# Function to subtract two matrices
def sub(A, B):
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

def strassen_multiply(A, B):
    n = len(A)

    # # Base case: if matrix is 1x1, multiply directly
    # if n == 1:
    #     return [[A[0][0] * B[0][0]]]
    if n <= 2:  # Base case
        return np.dot(A, B)

    # Split the matrices into quadrants
    half = n // 2

    A11, A12, A21, A22 = [], [], [], []
    B11, B12, B21, B22 = [], [], [], []
    for i in range(n):
        if i < half:
            A11.append(A[i][:half])
            A12.append(A[i][half:])
            B11.append(B[i][:half])
            B12.append(B[i][half:])
        else:
            A21.append(A[i][:half])
            A22.append(A[i][half:])
            B21.append(B[i][:half])
            B22.append(B[i][half:])

    # Calculate S matrices
    S1 = sub(B12, B22)
    S2 = add(A11, A12)
    S3 = add(A21, A22)
    S4 = sub(B21, B11)
    S5 = add(A11, A22)
    S6 = add(B11, B22)
    S7 = sub(A12, A22)
    S8 = add(B21, B22)
    S9 = sub(A11, A21)
    S10 = add(B11, B12)

    # Calculate P matrices using Strassen's formulas
    P1 = strassen_multiply(A11, S1)
    P2 = strassen_multiply(S2, B22)
    P3 = strassen_multiply(S3, B11)
    P4 = strassen_multiply(A22, S4)
    P5 = strassen_multiply(S5, S6)
    P6 = strassen_multiply(S7, S8)
    P7 = strassen_multiply(S9, S10)

    # Combine the results into the resulting matrix C
    C11 = add(sub(add(P5, P4), P2), P6) # Corrected formula
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(add(P5, P1), add(P3, P7))  # Corrected formula

    # Initialize the result matrix correctly
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(half):
        for j in range(half):
            C[i][j] = C11[i][j]
            C[i][j + half] = C12[i][j]
            C[i + half][j] = C21[i][j]
            C[i + half][j + half] = C22[i][j]

    return C

def test_strassen_mult():
    strassen_mult_times = []

    for matrix_size in range(5, 10):
        matrix_A = gen_matrix(2**matrix_size, 2**matrix_size)
        matrix_B = gen_matrix(2**matrix_size, 2**matrix_size)
        MM_start_time = datetime.now()
        strassen_multiply(matrix_A, matrix_B)
        MM_stop_time = datetime.now()
        MM_time = float((MM_stop_time - MM_start_time).total_seconds())
        strassen_mult_times.append(MM_time)
    print(strassen_mult_times)

    p = sns.lineplot(y=strassen_mult_times, x=[2**i for i in range(len(strassen_mult_times))])
    p.set_title('multiplication duration against matrix size')
    p.set_xlabel('Matrix Size')
    p.set_ylabel('Duration')
    plt.show()

def plot_sampled_data():
    #Include a sampled run from trad_mm
    trad_mult_time_sample = [0.000181, 0.0008, 0.005171, 0.039026, 0.33597]
    strassen_mult_time_sample = [0.016964, 0.116927, 0.850923, 5.754397, 40.975653]

    p = sns.lineplot(y=trad_mult_time_sample, x=[2 ** (i+5) for i in range(len(trad_mult_time_sample))])
    sns.lineplot(y=strassen_mult_time_sample, x=[2**(i+5) for i in range(len(strassen_mult_time_sample))])
    p.set_title('multiplication duration against matrix size')
    p.set_xlabel('Matrix Size')
    p.set_ylabel('Duration')
    plt.show()

def test_strassen_mult_example():
    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    B = [[16, 15, 14, 13],
         [12, 11, 10, 9],
         [8, 7, 6, 5],
         [4, 3, 2, 1]]

    C = strassen_multiply(np.array(A), np.array(B))

    # Convert result to a NumPy array for better visualization
    C_np = np.array(C)
    print("Result of Strassen's Matrix Multiplication:")
    print(C_np)

if __name__ == "__main__":
    test_strassen_mult_example()
    plot_sampled_data()

