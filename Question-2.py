"""Calculate and display the distribution of all possible combinations that can be
obtained when rolling both Die A and Die B together. Show the math along with
the code!"""

# Initializing a 6x6 matrix to represent all possible combinations
def all_possible_combinations(combinations):
    # Creating a 6x6 matrix with zeros
    for i in range(6):
        row = []  # Creating an empty row
        for j in range(6):
            row.append(0)  # Adding 0 to the row for each column
        combinations.append(row)

    # Generating the combinations matrix
    for i in range(6):
        for j in range(6):
            combinations[i][j] = (i + 1, j + 1)  # Storing the combination as a tuple

    # returning the combinations matrix
    return combinations

combinations = []
result = all_possible_combinations(combinations)
for row in result:
    print(row)




