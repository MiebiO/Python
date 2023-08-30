# numbers = []

# for i in range (1,101):
#     numbers.append(i)
# print(numbers)

#Method above is not the most efficient. Use method below

numbers = [i for i in range(1,101)]
print(numbers)

numbers = [i for i in range(1,101) if i%3 !=0]
# This skips all numbers evenly divisible by 0
print(numbers)
