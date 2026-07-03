def multiply_args(*numbers):
    # Initialize result as 1 (multiplication identity element)
    result = 1
    # Loop through all received numbers and multiply them one by one
    for number in numbers:
        result *= number
    return result

def print_even_odd(number):
    # Check if the remainder of division by 2 is zero (even) or not (odd)
    if number % 2 == 0:
        print(f'{number} is even.')
    else:
        print(f'{number} is odd.')

# Ask the user for a list of numbers separated by spaces
user_input = input('Enter numbers separated by spaces: ')

# Try to convert each piece of the string to an integer
try:
    # .split() breaks the string at each space, and the loop converts each piece to int
    numbers = [int(n) for n in user_input.split()]
    # Unpack the tuple with * to pass each number as a separate argument
    print_even_odd(multiply_args(*numbers))

# Handle the case where the user doesn't enter only numbers
except ValueError:
    print('Error: please enter only numbers separated by spaces.')
