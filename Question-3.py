"""Calculate the Probability of all Possible Sums occurring among the number of
combinations from (2) """
def probabilities_of_sum(combinations):
    for i in range(6):
        row=[]
        for j in range(6):
            row.append(0)
        combinations.append(row)

    # Generating the combinations matrix
    for i in range(6):
        for j in range(6):
            combinations[i][j] = (i + 1) + (j + 1)  # Storing the sum of the combination

    # Counting occurrences of each sum in combinations
    sum_count = {}
    total_combinations = 0

    for row in combinations:
        for sum_val in row:
            if sum_val in sum_count:
                sum_count[sum_val] += 1
            else:
                sum_count[sum_val] = 1

    # Calculating probabilities for each sum
    probabilities = {}
    for key, value in sum_count.items():
        probabilities[key] = value / 36
    return probabilities
    # Displaying the probabilities

combinations=[]
probabilities = probabilities_of_sum(combinations)
print("\nProbability of each sum:")
for key, value in probabilities.items():
    print("P(sum={}) = {:.3f}".format(key, value))
