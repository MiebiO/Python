list_us = ['New York City','Chicago']
list_uk = ['London','Bristol']
list_all = list_us + list_uk
print(list_all)

list_numbers = [1,2]*10
print(list_numbers)

num1= [0,1,2]
num2 = [4,5,6]

num3 = num1 +num2
#Note the + operator doesn't add the values of the lists. It joins them together
print(num3)

num_new =[]
for i in num2:
    num_new.append(i*4)
print(num_new)