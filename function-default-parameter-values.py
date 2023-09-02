# print('Hello', 'How are you?', end ='.', sep='-')

# end argument has default value of new line character
# sep argument has default value of a wide spaced character

# Define a function print_letter_count with two parameters: text and letter, both with default values.
def print_letter_count(text='This is the default string to search', letter='a'):
    # Initialize a counter to keep track of the number of occurrences of the 'letter' in 'text'.
    counter = 0
    
    # Iterate through each character in the 'text'.
    for char in text:
        # Check if the current character is equal to the specified 'letter'.
        if char == letter:
            # If it is, increment the counter.
            counter += 1
    
    # Print the result, indicating the number of occurrences of the 'letter' in the 'text'.
    print('Number of', letter, 'is', counter)

# Call the function with a specific 'text' and 'letter'.
print_letter_count('How many letters a are there?')

# Call the function without specifying any arguments, using the default values.
print_letter_count()
