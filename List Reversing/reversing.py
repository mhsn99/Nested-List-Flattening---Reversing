def reversing(lst):
    lst.reverse()
    for item in lst:
        if isinstance(item,list):
            reversing(item)
    return lst

example_list = [[1,2], [3, 4], [5, 6, 7]]
print(reversing(example_list))