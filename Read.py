# file = open('test.txt', )
# read all the contents of the file
# print(file.read())

# another way to open and close the file
# with open('test.txt', 'r') as reader:

# if you want only first few characters - new line characters are included in the count
# print(file.read(5))

# read one line
# print(file.readline())

# read the whole file line by line
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# readlines method will take the whole file and make each line an entry in a list
# recs = file.readlines()
# for rec in recs:
#     print(rec)

# not sure if this is as useful cuz not sure about addressing each rec specifically but seems to work just as a read
# for rec in file.readlines():
#     print(rec)
#
#
# file.close()