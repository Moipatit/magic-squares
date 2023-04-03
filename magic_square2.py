# get the user input and store in a variable called N
N = int(input("Please enter a positive odd integer: "))

#validation for the user input
if (N % 2) == 0:
    print("The number is NOT odd")
elif (N < 0):
    print("The number is NOT positive")
else:
    #initialise the rows and columns with the user input
    rows, cols = (N, N)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    #initialise the variables 
    n = 1
    a = 0
    b = N // 2

    #while n is less than N**2, increment n
    while n <= N**2:
        arr[a][b] = n 
        n += 1

        #moving diagonal up and right, wrapping to the first column
        # or the last row if the move leads outside of the grid
        a2 = (a-1) % N
        b2 = (b + 1) % N

        #if the cell is filled, move vertivally by one
        if arr[a2][b2]:
            a += 1
        else:
            a = a2
            b = b2

    #checking the sum of the rows and columns
    if n * (n * n + 1) // 2:
        print("correct")

    #print out the magic square
    for row in arr:
        print(row)

# I got some help with 2d lists from geeks for geeks, here is the link:https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
        




