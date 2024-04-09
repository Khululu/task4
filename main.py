def sort_by_length(strings):
    # По возрастанию длины
    ascending_sorted = sorted(strings, key=len)
    # По убыванию длины
    descending_sorted = sorted(strings, key=len, reverse=True)
    return ascending_sorted, descending_sorted
