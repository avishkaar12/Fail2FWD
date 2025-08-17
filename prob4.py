def spiral_order(matrix):
    result = []  # This will store the spiral order numbers
    while matrix:  # Keep going until the matrix is empty
        result += matrix.pop(0)  # Take the first row (top) from left to right
        if matrix:
            result += [row.pop() for row in matrix if row]  # Go down the last column
        if matrix:
            result += matrix.pop()[::-1]  # Take the last row (bottom) from right to left
        if matrix:
            result += [row.pop(0) for row in matrix[::-1] if row]  # Go up the first column
    return result  

for m in range(int(input("How many matrices do you want to process? "))):
    rows = int(input("Enter number of rows: "))  # Ask for number of rows
    print("Enter the matrix row by row, with elements separated by spaces:")
    matrix = [list(map(int, input().split())) for _ in range(rows)]  # Build the matrix
    print("Spiral order:", spiral_order(matrix))  # Show the spiral order
