import sys

def diagonalDifference(a):
    # Complete this function
    diag_a = 0; diag_b = 0
    
    d = len(a) - 1

    for i in range(len(a)): 
        diag_a += a[i][i]
        
        i_2 = (i - d) * (-1)
        diag_b += a[i][i_2]
        
    return abs(diff_diag)
    

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
