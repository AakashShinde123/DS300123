def insertion_sort(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and key < strings[j]:
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
    return strings

strings = ['cat', 'dog', 'bird', 'zebra', 'elephant', 'ant']
sorted_strings = insertion_sort(strings)
print(sorted_strings)