# what is wrong with this?

# 'Oke' hasn't been defined as a list, it is missing []
# If 'Oke' is added as a string, each letter will become an item in the list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'

print(cheese)

# this is the correct way to add Oke to the end of the list, in order to add it correctly we had to use square brackets to make it a list

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
print(cheese)

# to add two new cheeses to the list with a single command, used extend method
cheese.extend(['Mozzarella', 'Red Leicester'])
print(cheese)