#Exercise 1: List Creation using two lists

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd = list1[1::2]

even = list2[0::2]

list3 = odd + even

print("Element at odd-index positions from list one")
print(odd)

print("Element at even-index positions from list two")
print(even)

print("Printing Final third list")
print(list3)



#Exercise 2: Remove and add item in a list

list1 = [54, 44, 27, 79, 91, 41]

print("Original list:", list1)

removed = list1.pop(4)

print("After removing:", list1)

list1.insert(2, removed)

print("After inserting:", list1)

list1.append(removed)

print("After appending:", list1)


#Exercise 3: Slice list into 3 equal chunks and reverse each chunk

sample_list = [11,45,8,23,14,12,78,45,89]

for i in range(0, len(sample_list), 3):

    chunk = sample_list[i:i+3]

    print("Chunk", (i//3)+1, chunk)

    print("After reversing", chunk[::-1])


#Exercise 4: Count the occurrence of each element from a list

sample_list = [11,45,8,11,23,45,23,45,89]

count = {}

for item in sample_list:

    if item in count:

        count[item] += 1

    else:

        count[item] = 1



#Exercise 5: Paired Elements from Two Lists as a Set

first_list = [2,3,4,5,6,7,8]

second_list = [4,9,16,25,36,49,64]

result = set(zip(first_list, second_list))

print("Result is")

print(result)

print(count)

#Exercise 6: Set Intersection and Removal

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Find common elements
intersection = first_set.intersection(second_set)

# Remove common elements from the first set
first_set.difference_update(intersection)

print("Intersection is", intersection)
print("First Set after removing common elements", first_set)


#Exercise 7: Subset or Superset of another set

first_set = {1,2,3,4,5,6,7,8,9,10}
second_set = {1,2,3,4,5,6}

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of first set -", second_set.issubset(first_set))

print()

print("First set is Super set of second set -", first_set.issuperset(second_set))
print("Second set is Super set of first set -", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()
elif second_set.issubset(first_set):
    second_set.clear()
else:
    first_set.difference_update(second_set)
    second_set.difference_update(first_set)
print("\nFirst Set", first_set)
print("Second Set", second_set)


#Exercise 8: Filter List Against Dictionary Values

roll_number = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]

sample_dict = {
    'Jhon': 20,
    'Emma': 14,
    'Kelly': 2,
    'Jason': 8
}

roll_number[:] = [num for num in roll_number if num in sample_dict.values()]

print("After removing unwanted elements from list", roll_number)


#Exercise 9: Extract Unique Dictionary Values to List

speed = {
    'jan': 1,
    'feb': 3,
    'march': 1,
    'April': 2,
    'May': 3,
    'June': 4,
    'july': 5,
    'Aug': 2,
    'Sept': 3
}

unique_values = list(set(speed.values()))

print(unique_values)

#Exercise 10: remove duplicates from a list

sample_list = [1,3,5,3,7,1,9,5]

# Remove duplicates while preserving order
unique_list = list(dict.fromkeys(sample_list))

# Convert to tuple
sample_tuple = tuple(unique_list)

print("Unique items", unique_list)
print("Tuple", sample_tuple)
print("Min:", min(sample_tuple))
print("Max:", max(sample_tuple))