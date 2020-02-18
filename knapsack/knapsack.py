#!/usr/bin/python

import sys
from collections import namedtuple


# find the ratio of size/value of each item
# sort the tuple from great to last ratio
# add elements from tuple until threshold is reached
# return item indexes, total cost(max), (total value from input)

Item = namedtuple('Item', ['index', 'size', 'value'])
#items = Item[0]
# capacity = Item[1][1]
mylist = []
storeSize = []
#mySortedList = []
thing = []
newBag = []
profit = []


def knapsack_solver(items, capacity):
    #print("capacity", capacity)
    # items = all items in txt files
    # items[0] = first item in first file
    # item[1] = 2nd item in first file
    # item[0][1] = capacity/size of item
    # item[0][2]= value of item
    # capcity[0] =10
    # capacity[3]= 200
    # capcity[5]=1000
    for a, b, c in items:
        ratio = int(c/b)
        mylist.append((ratio, a, b, c))  # ratio, index, size, profit
        mylist.sort()
        thing = reversed(mylist)
    for a, b, c, d in thing:
        storeSize.append(c)
        totalsize = sum(storeSize)
        if totalsize < capacity:
            newBag.append((b, c, d))
    profit = [x[2] for x in newBag]
    totalprofit = sum(profit)
    itemlist = [x[0] for x in newBag]
    size = [x[1] for x in newBag]
    ntotalsize = sum(size)
    #print("newBag", len(newBag), totalsize, totalprofit)
    #totalprofit = [a]
    print("Items to select: ", itemlist, "TotalCost: ",
          ntotalsize, "TotalValue: ", totalprofit)
    return


"""
mytuple = ([1, 42, 81, ], [2, 42, 42], [3, 68, 56], [4, 68, 25], [5, 77, 14], [
           6, 57, 63], [7, 17, 75], [8, 19, 41], [9, 94, 19], [10, 34, 12])
knapsack_solver(mytuple, 100)
"""

# for a, b, c, d in reversed(mylist):
# storeSize.append(c)
# totalsize = sum(storeSize)
# while totalsize < capacity:
# newBag.append((b, c, d))
#print("newbag: ", newBag[0])

"""
def myHelper(items, capacity):
    for a, b, c, d in mylist:
        if mylist[-1]
"""

#print(" ")
#print("CAP", capacity)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
