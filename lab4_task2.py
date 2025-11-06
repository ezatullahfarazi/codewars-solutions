import doctest

def pound(expression: str) -> str
    """
    Return the result of the pound operation that is defined as "x # y" = x^2 - y^2
    
    >>> pound("2 # 3")
    -5
    >>> pound("0 # 0")
    0
    >>> pound(7)
    Traceback (most recent call last):
    ...
    AssertionError: invalid argument type
    >>> pound("1 # ")
    Traceback (most recent call last):
    ...
    AssertionError: must provide a value for y
    >>> pound("5 3")
    Traceback (most recent call last):
    ...
    AssertionError: expression must include # character
    >>> pound("6.7 # 1.5")
    Traceback (most recent call last):
    ...
    AssertionError: y should not be float
    """
    
    assert type(expression) == str, "invalid argument type"
    assert not '#' in expression, "expression must include # character"
    
    # Do some calculation with the input
    # 1 Find x and y in "x # y"
    # 1.1 Find where '#' is 
    pound_index = expression.find('#')
    
    # 1.2Find what the number is before '#' and let it be x
    x_str = expression[:pound_index]
    assert not '.' in x_str, "x should not be float"
    assert len(x_str) > 0, "must provide a value for x"
    x = int(x_str)
    
    # 1.3Find what the number is before '#' and let it be y
    y_str = expression[pound_index + 1:].strip()
    assert not '.' in y_str, "y should not be float"
    assert len(y_str) > 0, "must provide a value for y"
    y = int(y_str)
    
    # 2 Calculate the result based on the definition of '#'
    # which is x # y = x2 – y2 
    result = x * x - y * y
    
    # Show the result
    result

#doctest.testmod()
pound("2 # 3")

