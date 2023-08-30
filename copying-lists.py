# name_original = 'Jon Snow'
# name_new = name_original
# name_original = "Daenerys Targaryen"
# print(name_original, name_new)

#Method above does not work with lists. See below
list_original= [1,2,3]
list_new = list_original
list_original [0] = -5
print('Original: ',list_original, '\nNew: ', list_new)

#To make a true copy, use slicing
list_original= [1,2,3]
list_new = list_original[:]
list_original [0] = -5
print('Original: ',list_original, '\nNew: ', list_new)