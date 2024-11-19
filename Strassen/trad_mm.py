import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def matrix_multiplication(A, B):
    C = np.zeros((len(A),  len(B[0])))
    for n in range(len(A[0])):
        C += np.dot(np.atleast_2d(A[:,n]).T,  np.atleast_2d(B[n,:]))
    return C


def gen_matrix(num_rows=10, num_cols=10, lowest_int_num=10, highest_int_num=50):
    """Generate a 2D dataset of integer numbers."""
    num_of_nums_to_generate = num_rows * num_cols
    # NOTE: The reshape member fun will take the number of genrerated numbers as
    # specified by num_of_nums_to_generate   and generates a 2D matrix of the genrated numbers.
    # This means the value of num_of_nums_to_generate  must =  num_rows * num_cols.
    X = np.random.randint(lowest_int_num,
                          highest_int_num,
                          num_of_nums_to_generate).reshape(num_rows, num_cols)
    return X


def test_trad_mult():
    trad_mult_times = []

    for matrix_size in range(5, 10):
        matrix_A = gen_matrix(2**matrix_size, 2**matrix_size)
        matrix_B = gen_matrix(2**matrix_size, 2**matrix_size)
        MM_start_time = datetime.now()
        matrix_multiplication(matrix_A, matrix_B)
        MM_stop_time = datetime.now()
        MM_time = float((MM_stop_time - MM_start_time).total_seconds())
        trad_mult_times.append(MM_time)
    print(trad_mult_times)


    p = sns.lineplot(data=trad_mult_times)
    p.set_title('multiplication duration against matrix size')
    p.set_xlabel('Matrix Size')
    p.set_ylabel('Duration')
    plt.show()

if __name__ == "__main__":
    test_trad_mult()
    # A = [[1, 2, 3, 4],
    #      [5, 6, 7, 8],
    #      [9, 10, 11, 12],
    #      [13, 14, 15, 16]]
    #
    # B = [[16, 15, 14, 13],
    #      [12, 11, 10, 9],
    #      [8, 7, 6, 5],
    #      [4, 3, 2, 1]]
    # A = [[1, 2], [3, 4]]
    # B = [[5, 6], [7, 8]]
    #
    # print(matrix_multiplication(np.array(A), np.array(B)))
