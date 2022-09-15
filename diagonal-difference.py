def diagonalDifference(arr):
    # Write your code here
    diag_l = 0
    diag_r = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                diag_l += arr[i][j]
            if (j+i) == (len(arr)-1):
                diag_r += arr[i][j]
    
    return abs(diag_l - diag_r)

if __name__ == "__main__":
    a = [[11,2,4],[4,5,6],[10,8,-12]]

    print(diagonalDifference(a))