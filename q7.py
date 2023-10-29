def in_mat():
    row=9
    col=9
    mat=[]
    for x in range(row):
        p=[]
        for a in range(col):
            n=float(input("enter a number:"))
            p.append(n)
        mat.append(p)
    return mat

def sudoku(mat):
    m1=[[mat[0][0],mat[0][1],mat[0][2],mat[1][0],mat[1][1],mat[1][2],
            mat[2][0],mat[2][1],mat[2][2]],
           
           [mat[0][3],mat[0][4],mat[0][5],mat[1][3],mat[1][4],mat[1][5],
            mat[2][3],mat[2][4],mat[2][5]],
           
           [mat[0][6],mat[0][7],mat[0][8],mat[1][6],mat[1][7],mat[1][8],
           mat[2][6],mat[2][7],mat[2][8]],
           
           [mat[3][0],mat[3][1],mat[3][2],mat[4][0],mat[4][1],mat[4][2],
            mat[5][0],mat[5][1],mat[5][2]],
           
           [mat[3][3],mat[3][4],mat[3][5],mat[4][3],mat[4][4],mat[4][5],
            mat[5][3],mat[5][4],mat[5][5]],
           
           [mat[3][6],mat[3][7],mat[3][8],mat[4][6],mat[4][7],mat[4][8],
            mat[5][6],mat[5][7],mat[5][8]],
           
           [mat[6][0],mat[6][1],mat[6][2],mat[7][0],mat[7][1],mat[7][2],
            mat[8][0],mat[8][1],mat[8][2]],
           
           [mat[6][3],mat[6][4],mat[6][5],mat[7][3],mat[7][4],mat[7][5],
            mat[8][3],mat[8][4],mat[8][5]],
           
           [mat[6][6],mat[6][7],mat[6][8],mat[7][6],mat[7][7],mat[7][8],
            mat[8][6],mat[8][7],mat[8][8]],
           ]
    return m1

def transpose(mat):
    q=[]
    for i in range(len(mat[0])):
        p=[]
        for j in range(len(mat)):
            tra = mat[j][i]
            p.append(tra)
        q.append(p)
    return q

def issudoku(mat):
    for i in range(9):
        for j in range(9):
            if mat[i].count(mat[i][j]) == 1:
                continue
            else:
                return "not sudoku"
    mat_2 = transpose(mat)
    for i in range(9):
        for j in range(9):
            if mat_2[i].count(mat[i][j]) == 1:
                continue
            else:
                return "not sudoku"
    mat_3 = sudoku(mat)
    for i in range(9):
        for j in range(9):
            if mat_3[i].count(mat[i][j])==1:
                continue
            else:
                return "not sudoku"
    return "is sudoku"
print(issudoku(in_mat()))