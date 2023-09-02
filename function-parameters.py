# input_numbers = [5.0,3.5,7.8,9.9,10.0]

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum+= number
    average = sum/len(input_numbers)
    
    print(average)
    
get_average([5.0,3.5,7.8,9.9,10.0])


def print_letter_count (text,letter):
    counter = 0
    for char in text:
        if char == letter:
            counter +=1
    print('Number of ', letter, ' is ',counter)

print_letter_count('magnanimous','m')
print_letter_count('magnanimous','i')

print_letter_count('People say nothing is impossible, but I do nothing every day','a')