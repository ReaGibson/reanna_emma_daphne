# using open method to open a text file called pelican
# the 'w' allows for writing in the file
# the 't' truncates the file removing the text every time the file is run
# used output variable to define the file
output = open('pelican.txt', 'wt')
# using the write method to write the text on the pelican.txt
# it goes on the pelican text as the method is executed after the output variable
# \n is used to create a new line after the text
text = output.write('A wonderful bird is the pelican, \n')
text = output.write('His bill holds more than his belican. \n')
# created a list in the text, defined by [] and ,
# \n puts each item of the list on a new line
lines = ['He can take in his beak, \n', 'Enough food for a week, \n', "But I'm damned if I see how the helican. \n"]
# writelines method appends the list to the bottom of the text
output.writelines(lines)

