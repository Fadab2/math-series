def fibonacci(n):
    """
    A function to calculate the fibonacci value of a given number
    If the number is 0 return 0
    If the number is 1 return 1
    If the number is greater than 1 return is found by add the two
    previous numbers (number -1) + (number -2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def lucas(n):
    """
    A function to calculate the lucas value of a given number
    If the number is 0 return 2
    If the number is 1 return 1
    If the number is greater than 1 return is found by add the two
    previous numbers (number -1) + (number -2)

    """
    if (n == 0):
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(num, arg2 = 0, arg3 = 1):
    """
    A function that takes one required arg and 2 optional args. 
    optional args have a default values of 0 and 1.
    If no optional values are passed the function will produce
    fibonacci series.
    Calling with optional values 2 and 1 will produce lucas series.
    Other values for the optional args will produce other series.
   
"""
    # The two optional parameters will have default values of 
    # 0 and 1 and will determine the first two values for the
    # series to be produced.
    # [3, 3, 6, 9, 15]
    # [3, 6, 9, 15]
    # (4, 3, 6)

    # empty list to store the series
    series = []

    if arg2 == 0 and arg3 == 1:
        return fibonacci(num)
    else:
        if arg2 == 2 and arg3 == 1:
            return lucas(num)
    if num == 0:
        return arg2
    if num == 1:
        return arg3
    
    else:
        series.append(arg2)
        series.append(arg3)
        for number in range(1, num-1):
            number = arg2 + arg3
            arg2 = arg3
            arg3 = number
            series.append(number)
        return series

    


if __name__ == "__main__":
    print(f'Fibonacci: {fibonacci(3)}')
    print(f'Lucas: {lucas(15)}')
    #generate fibonacci series
    print(f'sum_series: {sum_series(10)}')
    #generate lucas series
    print(f'sum_series with agrs: {sum_series(10, 2, 1)}')
    # genereate other series starting a 3,6 with total series 4 numbers.
    print(f'sum_series with agrs: {sum_series(4, 3, 6)}')
