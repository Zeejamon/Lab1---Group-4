#!/usr/bin/env python
# coding: utf-8

# In[1]:


def median(lst):
    n = len(lst)
    s = sorted(lst)
    mid = n//2
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


# In[ ]:


filename = input("Enter name of file: ")

with open(filename, 'r') as f:
    lines = f.readlines()
    
num_lines = len(lines)

while True:
    print(f"The file has {num_lines} lines.")
    line_num = input("Enter a line number (or 0 to quit): ")
    line_num = int(line_num)
    
    if line_num == 0:
        break
    elif 1 <= line_num <= num_lines:
        print (f"Line{line_num}: {lines[line_num - 1]}")
    else:
        print(f"Invalid line number. Enter a number between 1 and {num_lines}.")


# In[ ]:




