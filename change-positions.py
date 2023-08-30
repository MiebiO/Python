first = input ('Enter first number:')
second = input ('Enter second number: ')
print('Before swapping',first,second)

#Swap value of variables

first, second = second, first
print('After swapping',first,second)

cities = ['nyc','la','nola','htx','phx']
cities [0], cities[4] = cities [4], cities [0]
print(cities)

cities.sort()
print(cities)

#Sort in descending order
cities.sort(reverse=True)
print(cities)