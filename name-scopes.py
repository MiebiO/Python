# Define a function called show_truth.
def show_truth():
    # Create a local variable named 'mysterious_var' inside the function.
    mysterious_var = 'New Surprise'
    
    # Print the value of the local 'mysterious_var'.
    print(mysterious_var)

# Create a global variable 'mysterious_var' with the initial value 'Surprise!'.
mysterious_var = 'Surprise!'

# Print the value of the global 'mysterious_var'.
print(mysterious_var)

# Call the show_truth function, which prints the local 'mysterious_var'.
show_truth()

# Print the value of the global 'mysterious_var' again.
print(mysterious_var)
