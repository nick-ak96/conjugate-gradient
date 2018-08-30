import conjgrad as c

def printMatrix(M):
    for row in M:
        print(row)

#test 1
A1 = [[4,1],[1,3]]
b1 = [1,2]

# test 2
A2 = [[4,-1,1],[-1,4,-2],[1,-2,4]]
b2 = [12,-1,5]

# test 3
A3 = [[5,-2,0],[-2,5,1],[0,1,5]]
b3 = [20,10,-10]

# test 4
A4 = [[34,12,0,0],[12,41,0,0],[0,0,1,0],[0,0,0,1]]
b4 = [29,47,5,2]

# run test 1
print("Test 1")
print("Matrix A")
printMatrix(A1)
print("Vector b") 
print(b1)
print("Answer")
c.cg(A1,b1)

print("\n\n")

# run test 2
print("Test 2")
print("Matrix A")
printMatrix(A2)
print("Vector b")
print(b2)
print("Answer")
c.cg(A2,b2)

print("\n\n")

# run test 3
print("Test 3")
print("Matrix A")
printMatrix(A3)
print("Vector b")
print(b3)
print("Answer")
c.cg(A3,b3)

print("\n\n")

# run test 4
print("Test 4")
print("Matrix A")
printMatrix(A4)
print("Vector b")
print(b4)
print("Answer")
c.cg(A4,b4)
