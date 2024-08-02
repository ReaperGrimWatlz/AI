def hash_table_search(arr, target):
    hash_table = {x: i for i, x in enumerate(arr)}
    return hash_table.get(target, -1)  # return -1 if not found
