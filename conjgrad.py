import numpy as np

def is_valid_matrix(A):
    """
    The method checks whether the matrix A is symmetric and positive-definite.
    """
    # check if matrix is symmetric
    if np.array_equal(A,np.matrix.transpose(A)):
        try:
            # check if matrix is positive definite
            np.linalg.cholesky(A)
            return True
        except np.linalg.LinAlgError:
            return False
    else:
        return False



def cg(A, b, x=None):
    """
    The method implements 'Conjudate Gradient' algorithm for solving system of the form 
        Ax=b, 
    where A is a symmetric, positive-definite, real matrix.
    """

    # convert variables to numpy
    A = np.array(A)
    b = np.array(b)

    # check the matrix A
    if not is_valid_matrix(A):
        raise ValueError("The matrix A is not valid. Please, make sure that the matrix A is symmetric and positive-definite.")

    n = len(A)
    # check dimensions
    if len(b) != n:
        raise ValueError("Vector b does not satisfy the dimensions of matrix A.")

    # conpute x iteratively
    x = np.ones(n)
    r = b - np.matmul(A,x)
    p = r
    rsold = np.dot(r,r)
    for i in range(n):
        Ap = np.matmul(A,p)
        alpha = rsold / np.dot(r,Ap)
        x = x + np.dot(alpha,p)
        r = r - np.dot(alpha,Ap)
        rsnew = np.dot(r,r)
        if rsnew ** .5 < 1e-10:
            break
        p = r + np.dot((rsnew / rsold),p)
        rsold = rsnew
    print(x)
