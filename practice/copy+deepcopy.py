import copy
spam = ['A', 'B', 'C', 'D', ['a', 'b']]
cheese = copy.copy(spam)
cheese[1] = 42
cheese[4][1] = 4
bacon = copy.deepcopy(spam)
bacon[4][0] = 3
print(spam)
print(cheese)
print(bacon)
