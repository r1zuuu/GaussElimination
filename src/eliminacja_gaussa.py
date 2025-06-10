import numpy as np


def eliminacja_gaussa(macierz, constants):
    n = len(macierz)
    A = macierz.astype(float)
    b = constants.astype(float)
    for i in range(n):
        if A[i, i] == 0: 
            for k in range(i + 1, n):
                if A[k, i] != 0:
                    A[[i, k]] = A[[k, i]]  
                    b[[i, k]] = b[[k, i]]  
                    break
                else:
                    raise ValueError(
                        "Macierz jest osobliwa, nie można znaleźć rozwiązania."
                    )
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]  
            A[j, i:] = (
                A[j, i:] - m * A[i, i:]
            )  
            b[j] = (
                b[j] - m * b[i]
            )  

    x = np.zeros(n) 
    for i in range(n - 1, -1, -1): 

        x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[
            i, i
        ]  
    return x
