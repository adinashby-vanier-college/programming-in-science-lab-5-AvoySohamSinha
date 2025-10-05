# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n == 1:
        return "*"
    
    result = ""
    for i in range (n):
        result += "*"
    result += "\n"

    for j in range (n-2):
        result += "*"
        for k in range (n-2):
            result += " "
        result += "*"
        result += "\n"
    
    for i in range (n):
        result += "*"

    return result

# print(hollow_square(5))





# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    
    for i in range (1, n +1):
        for j in range (1, i + 1):
            result += str(j) + ""
        result = result.strip()
        result += "\n"
        
    return result.rstrip()

# print(number_pattern(4))





# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total





# Example for n = 4:
#    *
#   ***
#  *****
# *******

def centered_star_pyramid(n):
    if n <= 0:
        return ""
    result = ""

    for i in range(n):
        for j in range(n-1-i):
            result += " "
            
        for k in range (i * 2 + 1):
            result += "*"
            
        result += "\n"

    return result.rstrip()


print(centered_star_pyramid(4))
