# please use the README.txt file for more explanation the comets try to be brief

#===========================	Dependencies	=======================================

import random

#=============================	Functions	============================================

def create_grid(rows, columns):
    """
    Returns the nested list "grid"
    Takes 2 inputs for setting up the grid: height and width of the grid
    
    Creates a nested list filled with random choice from the mine_or_not list
    > "-" no mine in cell
    > "#" has mine in cell
    
    the random sample selects the random selection from the mine_or_not by the number
    of random samples is selected by the width input
    this loop runs in range of the height input
    """
    grid = []
    mine_or_not = ["-", "#", "-", "-", "-", "#", "-", "-", "-", "#", "-", "#"]
    for _ in range(0, rows):
        grid.append(random.sample(mine_or_not, columns))
    return grid

def print_grid_format(nest_list):
    """
    Takes a nested list and prints it out so that every list inside of the list is a row
    """
    for row in nest_list:
        print("  ".join(row))

def count_adjacent_mines(grid):
    """
    This function contains a function within it count_mines that counts adjacent 
    mines for each cell in the grid and returns a new grid where each cell contains
    the count of adjacent mines.
    
    it take the grid input the grid needs to be a nested list otherwise it will not
    wok
    """
    #gets the length of rows and cols for the provided input grid
    # since all row ar the same in the grid we can
    # just take len of the 1st row or grid[0]
    rows = len(grid)
    cols = len(grid[0])

    # makes a new grid same size as the original grid just filled with
    # 0's as a place holder
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]


    def count_mines(row_of_cell, col_of_cell):
        """This function returns the count of all the mines around a given cell
        count_mines that takes two inputs:
        > row
        > col

        These inputs represent the row and column of a cell in the grid for which we
        are counting adjacent mines.
        """
        # sets a count variable
        count = 0

        # starts a row and column index iteration in these ranges to cover all the
        # adjacent cells to the row, colum of the cell we are counting for(the arguments)
        for surrounding_rows in [-1, 0, 1]:
            for surrounding_cols in [-1, 0, 1]:

                # these statements check if the row and column indexes are within
                # the grid boundaries and if any cell contains a mine if all are true
                # it increases the count by 1
                if (0 <= row_of_cell + surrounding_rows < rows and
                    0 <= col_of_cell + surrounding_cols < cols and
                    grid[row_of_cell + surrounding_rows][col_of_cell + surrounding_cols] == "#"):
                    count += 1

        # returns the count in string format so the list can be joined later
        # looks more readable that way
        return str(count)

    # rows is the length of the grid and col is the length of the 1st row
    # determined in the beginning of the function this iterates trough the
    # entire provided nester list (original_grid)
    for row in range(rows):
        for col in range(cols):

            # as it iterates trough the original list if it finds a mine in the
            # current cell iteration it just appends the mine to the new lis
            # if it doesn't find the mine then it calls the count method and
            # changes the current value of the cell to the return count of the method
            if grid[row][col] == "#":
                new_grid[row][col] = "#"
            else:
                new_grid[row][col] = count_mines(row, col)

    # this entire method returns the new_grid list
    return new_grid

#===========================    Final program code 	====================================

# make a initial grid and print it for comparison
print("The randomly generated grid with mines\n")
first_grid = create_grid(rows=5, columns=5)
print_grid_format(first_grid)

# print some space in between the 2 grids
print("\nGrid with the count for all mines\n")

# make a final grid with the numbers showing as well and print
final_grid = count_adjacent_mines(first_grid)
print_grid_format(final_grid)
