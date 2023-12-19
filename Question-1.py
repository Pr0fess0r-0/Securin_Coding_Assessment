#How many total combinations are possible? Show the math along with the code!

def Total_combinations(dice_a ,dice_b):
    total_combinations = len(dice_a) * len(dice_b)    # Calculating total combinations
    return total_combinations

# Representing the dice as arrays
dice_a = [1, 2, 3, 4, 5, 6]
dice_b = [1, 2, 3, 4, 5, 6]
print("Total combinations possible: ",  Total_combinations(dice_a,dice_b))