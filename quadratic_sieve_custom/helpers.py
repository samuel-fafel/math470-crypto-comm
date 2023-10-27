import numpy as np
import sympy as sp
import math
from itertools import chain
from collections import Counter


"""
This code does not belong to me, but belongs to NachiketUN, Maosef, and others on Github
All credit for the original code goes to him.

All code here is strictly for linear algebra
I have made slight alterations to improve efficiency in gauss_elim()
"""
def factor(n,factor_base):#trial division from factor base
        factors = []
        if n < 0:
            factors.append(-1)
        for p in factor_base:
            if p == -1:
                pass
            else:
                while n % p == 0:
                    factors.append(p)
                    n //= p
        return factors

def build_matrix(smooth_nums, factor_base):
    factor_base = [-1] + factor_base
    # Initialize a matrix of zeros with dimensions (len(factor_base), len(smooth_nums))
    M = [[0 for _ in smooth_nums] for _ in factor_base]

    for col, n in enumerate(smooth_nums):
        n_factors = factor(n, factor_base)
        for f in n_factors:
            if f in factor_base:
                row = factor_base.index(f)
                M[row][col] ^= 1  # Toggle between 0 and 1

        # Check for a square number
        if all(M[row][col] == 0 for row in range(len(M))):
            return True, n

    return False, M  # M is already transposed
 
def transpose(matrix):
#transpose matrix so columns become rows, makes list comp easier to work with
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return(new_matrix)

def xor_list(A, B, length): # O(length)
    for i in range(length):
        A[i] = A[i] ^ B[i]
    return A

def gauss_elim(M):
    return gauss_elim_custom(M)
#reduced form of gaussian elimination, finds rref and reads off the nullspace
#https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf
    
    #M = optimize(M)
    marks = [False]*len(M[0])
    
    for i in range(len(M)): #do for all rows
        row = M[i]
        #print(row)
        
        for num in row: #search for pivot
            if num == 1:
                #print("found pivot at column " + str(row.index(num)+1))
                j = row.index(num) # column index
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): #search for other 1s in the same column
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
    
    M = transpose(M)
        
    sol_rows = []
    for i in range(len(marks)): #find free columns (which have now become rows)
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return("No solution found. Need more smooth numbers.")
    print("Found {} potential solutions".format(len(sol_rows)))
    return sol_rows,marks,M

def gauss_elim_custom(M):
    M_length = len(M)
    row_length = len(M[0])
    print(f"\tNum Rows: {M_length}, Num Cols: {row_length}")
    marks = [False] * row_length
    
    for r, row in enumerate(M): # For all rows
        #print(f"in row {r}")
        for c, col in enumerate(row): # For all cols
            if col != 0:
                marks[c] = True # Mark the column
                for k in chain(range(0,r),range(r+1,M_length)): #search for other 1s in the same column
                    if M[k][c] == 1:
                        M[k] = xor_list(M[k], row, row_length)
                
                break
    
    print("Transposing Matrix")
    M = transpose(M)
    print("Finding Solution Rows")
    sol_rows = []
    for i in range(len(marks)): #find free columns (which have now become rows)
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return("No solution found. Need more smooth numbers.")
    #print("Found {} potential solutions".format(len(sol_rows)))
    return sol_rows, marks, M

def solve_row(sol_rows,M,marks,K=0):
    solution_vec, indices = [],[]
    free_row = sol_rows[K][0] # may be multiple K
    for i in range(len(free_row)):
        if free_row[i] == 1: 
            indices.append(i)
    for r in range(len(M)): #rows with 1 in the same column will be dependent
        for i in indices:
            if M[r][i] == 1 and marks[r]:
                solution_vec.append(r)
                break
            
    solution_vec.append(sol_rows[K][1])       
    return(solution_vec)
    
def solve(solution_vec,smooth_nums,xlist,N):
    
    solution_nums = [smooth_nums[i] for i in solution_vec]
    x_nums = [xlist[i] for i in solution_vec]
    
    Asquare = 1
    for n in solution_nums:
        Asquare *= n
        
    b = 1
    for n in x_nums:
        b *= n

    a = math.isqrt(Asquare)
    
    factor = math.gcd(b-a,N)
    return factor

# ----------------------------------- #

