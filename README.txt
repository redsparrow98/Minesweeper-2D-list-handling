====================	minesweeper program description		=========================

This program has 4 functions and is created to generate a grid for a minesweeper game
and finally generates a final grid showing all the numbers of mines to each adjacent
cell that doesn't have a mine.

if you are not familiar with the minesweeper game please refer to the wiki for a more
in depth explanation of how the game functions.
> https://en.wikipedia.org/wiki/Minesweeper_(video_game)

* PLEASE NOTE
this isn't a fully functional game it is just a project to cover 2D lists and their
manipulation within the Python language.

=================================	functions	=======================================

* create_grids(rows, columns)

This function takes 2 inputs:
> rows
> columns

with those inputs it generates a grid of the specified size with the 2 given inputs
it generates an empty list grid
and a mine_or_not list with 12 mixed "-" and "#"
"-"	-	represents a safe cell
"#"	-	represents a cell with a mine

it randomly chooses how many mines it will have and appends it in to the empty grid list
in the form of a nested list.
Finally ite returns the grid list.


* print_grid_format(nest_list)

This function takes one input:
> nest_list

it takes any nested list and and loops trough it for every list item within the
main list(row), and it joins every row printing out a 2D grid that is easier to understand


* count_adjacent_mines(grid)
(THIS FUNCTION CONTAINS A FUNCTION WITHIN ITSELF count_mines(row_of_cell, col_of_Cell)
IT WILL BE COWERED IN THIS SECTION)

This function takes 1 input
> grid

- firstly it take the length of rows and cols from the input grid. Since in minesweeper
all rows are the same length we can get the len of columns by just selecting a single row
and measuring its length.

- using those lengths it creates a new_grid filled with 0 as a place holder so it can be
replaced down the line when it calculates the adjacent mines

############# count_mines(row_of_cell, col_of_Cell)

it then creates the inside function which will calculate adjacent cells with mines for every
cell that we will be iterating trough in the next part.

takes 2 inputs:
> row_of_cell (the row of the cell that we will be counting for)
> col_of_Cell (the col of the cell that we will be counting for)

function sets the count to 0

this is relevant to the cell that we will be counting the mines for:
- then it starts a loop for surrounding_rows in the range -1 and 1(list)
- and same for the surrounding_cols in the same range -1 and 1(list)

while its looping trough these col and rows it checks for 3 statements
-	0 <= row_of_cell + surrounding_rows < rows
	*checks that the rows are within the grid around the given cell

-	0 <= col_of_Cell + surrounding_cols < cols
	*checks the col is within the grids around the given cell

-	grid[row_of_cell + surrounding_rows][col_of_Cell + surrounding_cols] == "#"
	* checks that the given iteration of the surrounding_row and surrounding_cols have
	a mine in them

If all 3 statements are correct it increases the count variable.
After the loop is finished with all the surrounding_row and surrounding_cols it returns
the count. it returns it in the form of a string so it can be joined later on.
#############

it starts a loop trough the rows and cols of the input grid
and checks for 2 statements
if the cell has a mine "#" then it appends a mine to the new_grid
and if the cell doesnt have a mine "-" it calls on to the count_mines function passing
cell row and col of the input grid and changing the value of the new_grid equivalent
to the exact same position of the provided cell it sets its value of the item in the list
to what the count return will be

==========================	Final code explanation	=====================================

it makes the initial grid with random mines and safe cells within it saves it to first_grid
variable
using the print_grid_format it prints the first grid in a 2D fir thats more visually pleasing
and easier to understand.

prints 2 empty spaces so the new grid can be compared to the given one.

it calls count_adjacent_mines and passes the first_grid in and saves the new_grid return to
final_grid variable

finally prints the final_grid in a print_grid_format.