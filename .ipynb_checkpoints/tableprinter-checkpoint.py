# def printTable(alist):
#     colWidths = [0] * len(tableData)
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose

for column in range(4):
    for row in range(3):
        print(tableData[row][column].rjust(10), end='!')
    print('@')
# #        print(tableData[row] [column].rjust(10), end='')