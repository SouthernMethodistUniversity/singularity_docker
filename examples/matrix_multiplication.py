import time, random
import numpy as np

def initialize_matrix(m, n, fill=0):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            if fill == 0:
                f = 0
            else:
                f = random.random()
            row.append(f)
        matrix.append(row)
    return matrix

def gemm(matrix_a, matrix_b):
    m = len(matrix_a[:][0])
    n = len(matrix_b[:][0])
    p = len(matrix_a[0][:])
    matrix_c = initialize_matrix(m, p)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                matrix_c[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return matrix_c

def py_gemm(i):
    start = time.time()
    matrix_a = initialize_matrix(i, i, fill=1)
    matrix_b = initialize_matrix(i, i, fill=1)
    matrix_c = gemm(matrix_a, matrix_b)
    stop = time.time()
    return stop - start

def numpy_gemm(i):
    start = time.time()
    matrix_a = np.random.rand(i, i)
    matrix_b = np.random.rand(i, i)
    matrix_c = np.matmul(matrix_a, matrix_b)
    stop = time.time()
    return stop - start
    
def compare_gemm():
    for i in [300, 400, 500]:
        py_dt = py_gemm(i)
        numpy_dt = numpy_gemm(i)
        print("Size: {}, Speed-up: {}".format(i, py_dt / numpy_dt))

if __name__ == '__main__':
    compare_gemm()

