import random  # Import the random module to generate random numbers

# Generate a random integer between 1 and 10 (inclusive) and assign it to the variable "number"
number = random.randint(1, 10)

counter = 0  # Initialize a counter to keep track of attempts

# Execute the following loop as long as the generated number is not 7
while number != 7:
    number = random.randint(1, 10)  # Generate a new random number
    counter += 1  # Increment the counter by 1 with each iteration
    
    # Check if the counter has exceeded 1
    if counter > 1:
        break  # Exit the loop if the counter is greater than 1

# Print the counter value and the final generated number
print(counter, number)

# For loop: iterate over the range from 0 to 9 (inclusive)
# The loop will run 10 times, printing the values 0 through 9
for i in range(10):
    print(i)
