def original_probabilities(Die_A, Die_B):
    # Calculate probabilities for original dice configurations
    probabilities = {}

    for roll_a in Die_A:
        for roll_b in Die_B:
            sum_val = roll_a + roll_b
            if sum_val in probabilities:
                probabilities[sum_val] += 1
            else:
                probabilities[sum_val] = 1

    # Calculate probabilities for each sum
    for key, value in probabilities.items():
        probabilities[key] = value / 36

    return probabilities


def generate_unique_combinations():
    def backtrack(start, path):
        if len(path) == 6:
            combinations.append(path[:]) #Copy the entire list to combinations
            return

        for i in range(start, 9):
            if i not in path:  # To avoid the duplication of elements
                path.append(i)
                backtrack(i + 1, path)
                path.pop() # To delete the last element

    combinations = []
    backtrack(1, []) # Function call for backtracking
    return combinations



def generate_unique_patterns():
   patterns = set()  

   def generate_pattern(pattern):
       if len(pattern) == 6:
           patterns.add(tuple(sorted((pattern))))
           return   #returns to last function call

       start = pattern[-1] if pattern else 1
	  #Assigning start value based on the current pattern
       for i in range(start, 5):
           new_pattern = pattern + [i]
           generate_pattern(new_pattern) #function call

   generate_pattern([])
   return list(patterns)

unique_patterns = generate_unique_patterns()



def undoom_dice(Die_A, Die_B):
   original_probs = original_probabilities(Die_A, Die_B)
   unique_patterns = generate_unique_patterns()
   unique_combs = generate_unique_combinations()
   new_probs = {}
   for i in unique_patterns :
       for j in unique_combs:
           new_probs = original_probabilities(i,j)
           if(new_probs == original_probs):
		   #comparing the values of probabilities
               return i,j
   return 0

# Example input: original dice configurations
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

# Generate transformed dice configurations
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("Dice - A =",list(New_Die_A))
print("Dice - B =",New_Die_B)

