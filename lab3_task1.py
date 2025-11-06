# getting input
user_input = input("Please, insert your expression in the format of x # y: ")

# Doing calculation with inputs
# Finding x and y in "x # y"
# Finding where "x"
pound_index = user_input.find("#")

# Finding what the number is before "x" and let it be x
x = int(user_input[:pound_index])

# Finding what the number is before "x" and let it be x
y = int(user_input[pound_index + 1:])

# Calculating the result based on the definition of "x"
# which is x # y = x2 - y2
result = x * x - y * y

# Showing the result
print(result)