def quick_sort_dict(d):
    if len(d) <= 1:
        return d
    pivot = list(d.keys())[len(d) // 2]
    left = {k: v for k, v in d.items() if k < pivot}
    middle = {k: v for k, v in d.items() if k == pivot}
    right = {k: v for k, v in d.items() if k > pivot}
    return {**quick_sort_dict(left), **middle, **quick_sort_dict(right)}

d = {'e': 5, 'a': 1, 'c': 3, 'b': 2, 'd': 4}
sorted_d = dict(quick_sort_dict(d).items())
print(sorted_d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
