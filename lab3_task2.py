# get input
# type 1 for True, press enter without input any value is False
a = bool(input("a = "))
b = bool(input("b = "))
    
# do the calculation
# The result is True iff it is not both True and both False
is_both_true = a and b
is_one_different = a or b
    
result = (not is_both_true or is_one_different)
    
# show the result
print(result)