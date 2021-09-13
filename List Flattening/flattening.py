def flatten(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item,list):
          flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list


example_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(example_list))
