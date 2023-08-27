for i in range(1, 11,3):
    pass

# Loop syntax requires one instruction in the loops' body
# If pass wasn't used above, an error will be seen when the code is run
# pass instruction can be used when you don't know what to put yet in the loop.
# pass can also be used with if, elif, else

for a in range (1,6):
    for b in range (1,6):
        print(a, 'x', b, '=', a*b)