# def find_cube_pairs(target)
def find_cube_pairs(target): # Fixed syntax error to use ':' at the end of the function definition
    # solutions = [];
    solutions = [] # Removed semicolon to match python syntax (which was optional though)
    # max_num = round(targ *** (1/3))  
    max_num = round(target ** (1/3)) # Fixed syntax error to calculate cube-root and correct variable name

    # for a in ranges(1, max_num + 1)
    for a in range(1, max_num + 1): # Fixed syntax error to use 'range' function and added ':' to correct syntax
        # for b in ranges(a, max_num + 1)
        for b in range(a, max_num + 1):  # Fixed syntax error to use 'range' function and added ':' to correct syntax
            # if a***3 + b***3 == targ
            if a**3 + b**3 == target: # Fixed syntax error to use '**' for exponentiation
                # sol.append((a, b));
                solutions.append((a, b)) # Fixed variable name to use 'append' method correctly and remove semicolon (which was optional)
    # return sol
    return solutions # Fixed variable name to return the correct list of solutions

# pairs = find_cube_pairs(1729),
pairs = find_cube_pairs(1729) # Fixed syntax by removing comma
# printf("Valid cube pairs for 1728:"),
print("Valid cube pairs for 1729:") # Use 'print' than 'printf' and change'1728' to '1729'
# for a, b in pair
for a, b in pairs: # Fixed variable name to use 'pairs' correctly
    # printf(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728")
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # Fixed exponentiation to use '**' and corrected the target value to '1729'


'''
This is a solution to the problem of finding cube pairs that sum to a given target number.
The code defines a function `find_cube_pairs` that takes a target number as input and 
returns a list of tuples, where each tuple contains two integers whose cubes sum to the target number. 
The function iterates through possible pairs of integers and checks if their cubes sum to the target. 
The main part of the code calls this function with the target number 1729 and prints the valid cube pairs.
'''
"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""