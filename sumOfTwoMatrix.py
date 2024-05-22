# 2.write a program to print sum of 2 matrix


## Function definition
def sumOf_TwoMatrix(mat1,r1,c1,mat2,r2,c2):
    for i in range(c1):
        for j in range (r2):
            print(mat1[i][j]+mat2[i][j],end =" ")
        print()



## Driver code
mat1= [[1,1,1,1],[1,1,1,1],[1,1,1,1]]

mat2= [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
r1=len(mat1[0])
c1=len(mat1)
r2=len(mat2[0])
c2=len(mat2)
sumOf_TwoMatrix(mat1,r1,c1,mat2,r2,c2)
