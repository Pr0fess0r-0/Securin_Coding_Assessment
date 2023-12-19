def original_probabilities(Die_A, Die_B):
    # Calculate probabilities for original dice configurations
    probabilities = {}

    for roll_a in Die_A:
        for roll_b in Die_B:
            sum_val = roll_a + roll_b
            if sum_val > 12:
                break
            else:
                if sum_val in probabilities:
                    probabilities[sum_val] += 1
                else:
                    probabilities[sum_val] = 1

    # Calculate probabilities for each sum
    for key, value in probabilities.items():
        probabilities[key] = value / 36

    return probabilities

def undoom_dice(Die_A, Die_B):
    original_probs = original_probabilities(Die_A, Die_B)
    New_Die_A = []
    count=0
    New_Die_B = []
    for i in range(1,5):
        for j in range(i,5):
            count=0
            New_Die_A = [1,2,i,i,j,4]
            for x in range(1,12):
                for y in range(x,6):
                    New_Die_B = [1,2,x,x,y,8]
                    new_probs = original_probabilities(New_Die_A, New_Die_B)
                    for z in range(2,12):
                        try:
                            if(original_probs[z] == new_probs[z]):
                                count+=1
                            else:
                                count=0
                        except KeyError:
                            break
                    if(count == 12):
                        return New_Die_A,New_Die_B

    return New_Die_A, New_Die_B

# Example input: original dice configurations
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

# Generate transformed dice configurations
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("A =",New_Die_A)
print("B =",New_Die_B)
