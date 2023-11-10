# Pregunta 3
# The binary_search function returns the position of key in the list if found, or -1 if not found. We want to make sure that it's working c
# orrectly, so we need to place debugging lines to let us know each time that the list is cut in half, whether we're on the left or the right.
# Nothing needs to be printed when the key has been located.   
# For example, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) first determines that the key, 3, is in the left half of the list, and prints "Checking the left side", then determines that it's in the right half of the new list and prints "Checking the right side", before returning the value of 2, which is the position of the key in the list.  
# Add commands to the code, to print out "Checking the left side" or "Checking the right side", in the appropriate places.  

# def binary_search(lst, key):
#     # Devuelve la posición de la clave en la lista si se encuentra, -1 en caso contrario.

#     # La lista debe estar ordenada:
#     lst.sort()
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         middle = (left + right) // 2

#         if lst[middle] == key:
#             return middle
#         if lst[middle] > key:
#             print("Checking the left side")
#             right = middle - 1
#         if lst[middle] < key:
#             print("Checking the right side")
#             left = middle + 1
#     return -1

# print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
# """Should print 2 debug lines and the return value: Checking the left side
# Checking the left side
# 0
# """

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# """Should print no debug lines, as it's located immediately:
# 4"""

# print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
# """Should print 3 debug lines and the return value:
# Checking the right side
# Checking the left side
# Checking the right side
# 6
# """

# print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
# """Should print 3 debug lines and the return value:
# Checking the right side
# Checking the right side
# Checking the right side
# 9
# """
# print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
# """Should print 4 debug lines and the "not found" value of -1:
# Checking the right side
# Checking the right side
# Checking the right side
# Checking the right side
# -1
# """

#Pregunta 5
# The best_search function compares linear_search and binary_search functions, to locate a key in the list, and returns how many steps 
# each method took, and which one is the best for that situation. The list does not need to be sorted, as the binary_search function sorts it 
# before proceeding (and uses one step to do so). Here, linear_search and binary_search functions both return the number of steps that it took 
# to either locate the key, or determine that it's not in the list. If the number of steps is the same for both methods (including the extra 
# step for sorting in binary_search), then the result is a tie. Fill in the blanks to make this work. 

def linear_search(list, key):
    # Returns the number of steps to determine if key is in the list

    # Initialize the counter of steps
    steps = 0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps

def binary_search(list, key):
    # Returns the number of steps to determine if key is in the list

    # List must be sorted:
    list.sort()

    # The Sort was 1 step, so initialize the counter of steps to 1
    steps = 1 
    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return steps

def best_search(list, key):
    steps_linear = linear_search(list, key)
    steps_binary = binary_search(list, key)
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if steps_linear < steps_binary:
        results += "Best Search is Linear."
    elif steps_binary < steps_linear:
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
# Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
# Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
# Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
# Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
# Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.