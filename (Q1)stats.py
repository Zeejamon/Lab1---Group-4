def median(lst):

    n = len(lst)
    s = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid-1] + s[mid]) / 2
    else:
        return s[mid]


def mode(lst):
    
    freq = {}
    for x in lst:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    mode = None
    mode_count = 0
    for x in freq:
        if freq[x] > mode_count:
            mode_count = freq[x]
            mode = x
    return mode


def mean(lst):

    return sum(lst) / len(lst)

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print("Data: ", data)
print("Median: ", median(data))
print("Mode: ", mode(data))
print("Mean: ", mean(data))