
#Exercise 1. Arithmetic Product and Conditional Logic

input1 = int(input("Enter a number: "))
input2 = int(input("Enter second number: "))
product = input1 * input2
if product <= 1000:
    print("The product is:", product)
else:
    print("The sum is:", input1 + input2) 


#Exercise 2. Cumulative Sum of a Range

previous = 0

for current in range(10):
    total = current + previous

    print(
        "Current:", current,
        "Previous:", previous,
        "Sum:", total
    )

    previous = current


#Exercise 3. String Indexing and Even Slicing

text = input("Enter a string: ")

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i])


#Exercise 4. String Slicing and Substring Removal

word = str(input("Enter a word: "))
def remove_chars(word, n):
    return word[n:]


print(remove_chars(word, 4))
print(remove_chars(word, 2))

#Exercise 5. Variable Swapping (The In-Place Method)
a = 5
b = 10

print("Before Swap")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swap")
print("a =", a)
print("b =", b)



#Exercise 6. Calculating Factorial with a Loop

number = 5

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)


#Exercise 7. List Manipulation: Add and Remove

fruits = ["apple", "Pear", "cherry", "Lemon", "Mango"]

fruits.append("Watermelon")

fruits.pop(1)


#Exercise 8. String Reversal

text = "Learning Python"

reverse = text[::-1]

print(reverse)



#Exercise 9. Vowel Frequency Counter

sentence = "This is a new Biggening"

count = 0

vowels = "aeiouAEIOU"

for i in sentence:
    if i in vowels:
        count += 1

print("Number of vowels:", count)

print(fruits)



#Exercise 10. Finding Extremes (Min/Max) in a List

numbers = [45, 2, 45, 54, 54, 23 , 54, 89, 12, 7]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


#Exercise 11. Removing Duplicates from a List

data = [1, 2, 2,  2, 4, 4, 3, 4, 1, 2, 2, 4, 4, 5]

unique = list(set(data))

print(unique)



#Exercise 12. List Comparison and Boolean Logic

def first_last_same(numbers):
    return numbers[0] == numbers[-1]


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("Given list: [10, 20, 30, 40, 10] | result is  " + str(first_last_same(numbers_x)))
print("Given list: [75, 65, 35, 75, 30] | result is " + str(first_last_same(numbers_y)))


#Exercise 13. Filtering Lists with Conditional Logic

num_list = [10, 20, 33, 46, 55]

print("Divisible by 5:")

for number in num_list:
    if number % 5 == 0:
        print(number)


#Exercise 14. Substring Frequency Analysis

text = "A person who does not know and does not know that he does not know is a fool."

count = text.count("know")

print("'know' appeared", count, "times")


#Exercise 15. Nested Loops for Pattern Generation

for i in range(11):
    for j in range(i):
        print(i, end=" ")
    print()
