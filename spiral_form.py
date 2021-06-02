def spiralTraverse(ending_row_index, ending_col_index, a):
    starting_row_index = 0
    starting_col_index = 0

    while starting_row_index < ending_row_index and starting_col_index < ending_col_index:
        # print first row
        for i in range(starting_col_index, ending_col_index):
            print(a[starting_row_index][i], end=" ")
        starting_row_index += 1

        # print last col
        for i in range(starting_row_index, ending_row_index):
            print(a[i][ending_col_index - 1], end=" ")

        ending_col_index -= 1

        # Print the last row from
        # the remaining rows
        if starting_row_index < ending_row_index:

            for i in range(ending_col_index - 1, (starting_col_index - 1), -1):
                print(a[ending_row_index - 1][i], end=" ")

            ending_row_index -= 1

        if starting_col_index < ending_col_index:
            for i in range(ending_row_index - 1, starting_row_index - 1, -1):
                print(a[i][starting_col_index], end=" ")

            starting_col_index += 1


inputMatrix = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

total_row = 3
total_col = 4

# Function Call
spiralTraverse(total_row, total_col, inputMatrix)
