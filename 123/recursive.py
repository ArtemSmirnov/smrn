list123 = [2, 3, 4,[6,7,[4,8,67,45,11,[90,65,1],8,9,[55,66]],4,5,67,88,[23,32,[765]]]]

def print_list(lst):
    [print_list(element) if isinstance(element,list) else print(element) for element in lst]

print_list(list123)
