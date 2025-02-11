
# open function to read the pelican text and then using read method to read it. r is the mode and stands for read. t stands for text
poem = open('pelican.txt', 'rt').read()
# used f string to print whole poem which has been printed underneath on a new line with \n
print(f"Whole poem:\n{poem}")
# data type is a string
print(type(poem))
# using splitlines method to print poem as a list
poem_as_list = open('pelican.txt', 'r').read().splitlines()
print(f"Whole poem as a list:\n{poem_as_list}")

print(type(poem_as_list))
# printing how many items are in the list, console will show 5 as there are 5 lines in the poem
print(len(poem_as_list))
# created a for loop to iterate through each item in the list
for items in poem_as_list:
    print(items)
