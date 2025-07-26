

columns = 7
rows = 4
 

 #   *
 #  ***
 # *****
 #*******

for row in range (0,4):
    if row < rows:
        print(" " * (rows - row - 1), end="")    # Print spaces
        print("*" * (2 * row + 1))       # Print stars

     
    