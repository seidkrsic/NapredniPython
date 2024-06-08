import numpy as np

def matrica_nxn(n):
    X = np.array([np.arange(1, n+1) for _ in range(n)])
    Y = np.array([np.full(n, i+1) for i in range(n)])
    return X, Y



n = int(input("Unesi n: ")) 
X, Y = matrica_nxn(n) 


print("Matrica X: ")
print(X)
print("Matrica Y") 
print(Y) 
