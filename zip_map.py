grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]
mylist = list(zip(avgs, grades))
print(mylist)
#Functional equivalent using map
otherlist = list(map(lambda *a: a, avgs, grades))
print(otherlist)
