A=[[1,2,3][2,3,4][3,44,5][4,5,6]]
def rotate( A):
    n = len(A)
    for i in range(n/2):
        for j in range(n-n/2):
            A[i][j], A[~j][i], A[~i][~j], A[j][~i] = A[~j][i], A[~i][~j], A[j][~i], A[i][j]
rotate(A)
print(A)            
