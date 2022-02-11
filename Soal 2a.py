array = [(11, 2, 4),(4, 5, 6),(10, 8, 12)]
d_a = array[0][0]+array[1][1]+array[2][2]
d_b = array[0][2]+array[1][1]+array[2][0]
print("Matrix 3x3: "+str(array))
print("Diagonal A = "+str(d_a))
print("Diagonal B = "+str(d_b))
print("Total DA + DB = "+str(d_a+d_b))
