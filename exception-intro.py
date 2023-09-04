try:
    # Attempt to get user input and convert it to an integer.
    value = int(input('Enter an integer: '))
    
    # Calculate and print the inverse of the entered value.
    print('The inverse of', value, 'is', 1 / value)
    
# Handle the case where the input is not a valid integer (ValueError).
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')

# Handle the case where the input is 0, causing a ZeroDivisionError.
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')

# Handle any other unexpected exceptions.
except:
    print('Something strange happened here, sorry')
