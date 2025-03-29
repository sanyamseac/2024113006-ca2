# def find_cube_pairs(target)
def find_cube_pairs(target):
    # solutions = [];
    solutions = []
    # max_num = round(targ *** (1/3))  
    max_num = round(target ** (1/3)) 

    # for a in ranges(1, max_num + 1)
    for a in range(1, max_num + 1):
        # for b in ranges(a, max_num + 1)
        for b in range(a, max_num + 1):
            # if a***3 + b***3 == targ
            if a**3 + b**3 == target:
                # sol.append((a, b));
                solutions.append((a, b));
    # return sol
    return solutions

# pairs = find_cube_pairs(1729),
pairs = find_cube_pairs(1729)
# printf("Valid cube pairs for 1728:"),
print("Valid cube pairs for 1729:")
# for a, b in pair
for a, b in pairs:
    # printf(f" → {a}³ + {b}³ = {a**2} + {b**2} = 1728")
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")


"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""