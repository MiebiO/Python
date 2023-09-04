# Define a function called 'unique' that takes a list as an argument, with a default empty list if no argument is provided.
def unique(list_entry=[]):
    # Create an empty list called 'empty_list'.
    empty_list = []
    
    # Iterate through each 'item' in the input 'list_entry'.
    for item in list_entry:
        # Check if the 'item' is not already in the 'empty_list'.
        if item not in empty_list:
            # If it's not, add the 'item' to the 'empty_list'.
            empty_list.append(item)
    
    # Return the 'empty_list' containing unique elements.
    return empty_list


unique()
unique([1, 1, 4, 5, 1])