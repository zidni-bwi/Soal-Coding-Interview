matrix = [[ 11, 2,  4 ],[  4, 5,  6 ],[ 10, 8, 12 ]]
print("Matrix 3x3: "+str(matrix))

def Hitung(matrix, dimensi):
    diagonal_a = 0
    diagonal_b = 0
    for i in range(0, dimensi):
        diagonal_a += matrix[i][i]
        diagonal_b += matrix[i][dimensi - i - 1]
    print("Diagonal A:"+str(diagonal_a)+" Sedangkan Diagonal B: "+str(diagonal_b))
    print("Total Diagonal A+B: "+str(diagonal_a+diagonal_b))

Hitung(matrix, 3)
