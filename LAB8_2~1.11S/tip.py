# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):

ok = True

# Check if all rows are good.
for r in range(9):


# Check if all columns are good.
if ok:
    for c in range(9):


# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):


# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
