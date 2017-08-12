test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))
#Exactly the same
print(list(filter(lambda x: x, test)))
#Keep x > 4
print(list(filter(lambda x: x > 4, test)))
