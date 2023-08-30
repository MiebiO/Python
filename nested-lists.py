#Lists can be nested. i.e. a list within a list
numbers = [1,2,3,4]
countries =['UK','US','Nigeria']

cells =[['A1','A2','A3'],['B1','B2','B3']]
print(cells[0][0])

for x in cells:
    for i in x:
        print(i)
        
        
table = [[[i for i in range (1,6)] for j in range (4)] for k in range (4)]
print(table)