# Python Essentials: Complete Reference Guide

## Quick Summary

### Operators

| Category | Operators | Example |
|----------|-----------|---------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `10 // 3` → `3` |
| **Comparison** | `==`, `!=`, `<`, `>`, `<=`, `>=` | `5 > 3` → `True` |
| **Logical** | `and`, `or`, `not` | `True and False` → `False` |
| **Identity** | `is`, `is not` | `x is None` |
| **Membership** | `in`, `not in` | `'a' in 'apple'` → `True` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` | `x += 5` |

**Important Arithmetic Operators:**

```python
# Division / vs Floor Division //
print(10 / 3)   # 3.3333333333333335 (float result, keeps decimals)
print(10 // 3)  # 3 (integer result, rounds down)
print(10 / 4)   # 2.5
print(10 // 4)  # 2

# Negative numbers with floor division
print(-10 // 3)  # -4 (rounds DOWN to more negative)
print(-10 / 3)   # -3.3333333333333335

# Modulo % (remainder)
print(10 % 3)    # 1 (10 = 3*3 + 1)
print(17 % 5)    # 2
print(10 % 10)   # 0

# Power **
print(2 ** 3)    # 8 (2 * 2 * 2)
print(5 ** 2)    # 25
print(10 ** 0)   # 1

# Common use: Get last digit
number = 12345
last_digit = number % 10      # 5
last_two = number % 100       # 45

# Common use: Check even/odd
if num % 2 == 0:
    print("even")
```

### Reserved Keywords (35)

```python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Built-in Data Types

| Type | Example | Mutable? | Ordered? | When to Use |
|------|---------|----------|----------|-------------|
| **str** | `"hello"` | ❌ No | ✅ Yes | Text manipulation, pattern matching |
| **list** | `[1, 2, 3]` | ✅ Yes | ✅ Yes | Dynamic collections, stacks, queues |
| **tuple** | `(1, 2, 3)` | ❌ No | ✅ Yes | Fixed data, dict keys, return multiple values |
| **dict** | `{'key': 'value'}` | ✅ Yes | ✅ Yes (3.7+) | Fast lookups, counting, caching |
| **set** | `{1, 2, 3}` | ✅ Yes | ❌ No | Unique items, fast membership tests |

---

#### String (str) - Text Processing

**Basic Operations:**
```python
# Creation
s = "hello"
s = 'world'
s = """multi
line"""

# Indexing & Slicing
s = "python"

# Positive indexing (0 to len-1)
s[0]        # 'p' (first)
s[1]        # 'y'
s[5]        # 'n' (last)

# Negative indexing (counts from end)
s[-1]       # 'n' (last element)
s[-2]       # 'o' (second from last)
s[-6]       # 'p' (first element)

# Understanding negative index positions:
#  p   y   t   h   o   n
#  0   1   2   3   4   5    (positive index)
# -6  -5  -4  -3  -2  -1    (negative index)

# Slicing [start:end] - end is NOT included
s[0:3]      # 'pyt' (index 0, 1, 2)
s[2:5]      # 'tho' (index 2, 3, 4)
s[:3]       # 'pyt' (from start to 3)
s[3:]       # 'hon' (from 3 to end)

# Negative slicing
s[-3:]      # 'hon' (last 3 elements: index -3, -2, -1)
s[-5:]      # 'ython' (last 5 elements)
s[:-2]      # 'pyth' (everything except last 2)

# Mixed positive and negative
s[1:-1]     # 'ytho' (from index 1 to second-last)
s[-4:-1]    # 'tho' (from -4 to -1, not including -1)

# Edge cases (important to understand!)
s[-3:-4]    # '' (EMPTY! -3 is to the RIGHT of -4, can't go backwards)
s[-4:-3]    # 't' (from -4 to -3, not including -3)
s[3:1]      # '' (EMPTY! 3 is to the RIGHT of 1, can't go backwards)

# Reverse with step
s[::-1]     # 'nohtyp' (reverse entire string)
s[::2]      # 'pto' (every 2nd character)
s[1::2]     # 'yhn' (every 2nd character starting from index 1)

# Common operations
len("hello")           # 5
"hello" + " world"     # Concatenation
"hello" * 3            # 'hellohellohello'
'e' in "hello"         # True
```

**Common Interview Problems Using Strings:**

```python
# 1. Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Input: "A man a plan a canal Panama"
# Output: True
# Input: "race a car"
# Output: False

# 2. Count character frequency
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 3. First non-repeating character
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1

# Input: "leetcode"
# Output: 0 (first unique char is 'l' at index 0)
# Input: "loveleetcode"
# Output: 2 (first unique char is 'v' at index 2)
# Input: "aabb"
# Output: -1 (no unique character)

# 4. Valid anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Input: "listen", "silent"
# Output: True
# Input: "hello", "world"
# Output: False

# 5. Reverse words in a string
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Input: "the sky is blue"
# Output: "blue is sky the"
# Input: "hello world"
# Output: "world hello"
```

---

#### List - Dynamic Arrays

**Basic Operations:**
```python
# Creation
nums = [1, 2, 3]
mixed = [1, "hello", 3.14, [1, 2]]
empty = []

# Indexing & Slicing
nums = [10, 20, 30, 40, 50]

# Positive indexing
nums[0]           # 10 (first)
nums[4]           # 50 (last)

# Negative indexing (counts from end)
nums[-1]          # 50 (last item)
nums[-2]          # 40 (second from last)
nums[-5]          # 10 (first item)

# Index positions:
# [10,  20,  30,  40,  50]
#   0    1    2    3    4     (positive)
#  -5   -4   -3   -2   -1     (negative)

# Slicing [start:end] - end NOT included
nums[0:3]         # [10, 20, 30]
nums[2:4]         # [30, 40]
nums[:3]          # [10, 20, 30] (from start)
nums[3:]          # [40, 50] (to end)

# Negative slicing
nums[-3:]         # [30, 40, 50] (last 3 elements)
nums[-2:]         # [40, 50] (last 2)
nums[:-2]         # [10, 20, 30] (all except last 2)

# Mixed
nums[1:-1]        # [20, 30, 40] (exclude first and last)
nums[-4:-1]       # [20, 30, 40]

# Edge cases
nums[-2:-3]       # [] (EMPTY! -2 is right of -3)
nums[-3:-2]       # [30] (from -3 to -2)

# Reverse
nums[::-1]        # [50, 40, 30, 20, 10]

# Modification (mutable!) - These modify the original list
nums = [10, 20, 30, 40, 50]

nums.append(60)        # Add to end
print(nums)            # [10, 20, 30, 40, 50, 60]

nums.insert(0, 5)      # Insert value 5 at index 0
print(nums)            # [5, 10, 20, 30, 40, 50, 60]

nums.insert(2, 15)     # Insert value 15 at index 2
print(nums)            # [5, 10, 15, 20, 30, 40, 50, 60]

# Add multiple items (only at END)
nums.extend([70, 80])  # Add multiple items to END
print(nums)            # [5, 10, 15, 20, 30, 40, 50, 60, 70, 80]

# To insert multiple items at specific position, use slicing
nums = [10, 20, 50, 60]
nums[2:2] = [30, 40]   # Insert [30, 40] at index 2
print(nums)            # [10, 20, 30, 40, 50, 60]

nums = [10, 20, 30]
nums[1:1] = [15, 17]   # Insert [15, 17] at index 1
print(nums)            # [10, 15, 17, 20, 30]

# Removing items (modifies original list)
nums = [10, 20, 30, 40, 50]

last = nums.pop()      # Remove and return last item
print(last)            # 50
print(nums)            # [10, 20, 30, 40]

second = nums.pop(1)   # Remove and return item at index 1
print(second)          # 20
print(nums)            # [10, 30, 40]

nums.remove(30)        # Remove first occurrence of value 30
print(nums)            # [10, 40]

del nums[0]            # Delete item at index 0
print(nums)            # [40]

# Common operations
nums = [10, 20, 30, 40]
len(nums)              # 4 (length)
30 in nums             # True (membership check)
50 in nums             # False
nums.sort()            # Sort in place (modifies nums)
sorted(nums)           # Return sorted copy (nums unchanged)
```

**Common Interview Problems Using Lists:**

```python
# 1. Two Sum - Find indices of two numbers that add up to target
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (nums[0] + nums[1] = 2 + 7 = 9)
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2] (nums[1] + nums[2] = 2 + 4 = 6)

# 2. Remove duplicates from sorted array (in-place)
def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

# Input: nums = [1, 1, 2, 2, 3]
# Output: 3 (nums becomes [1, 2, 3, _, _])
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5 (nums becomes [0, 1, 2, 3, 4, _, _, _, _, _])

# 3. Maximum subarray sum (Kadane's algorithm)
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 (subarray [4, -1, 2, 1] has the largest sum)
# Input: [1]
# Output: 1
# Input: [-1, -2, -3]
# Output: -1

# 4. Rotate array k steps
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]
# Input: nums = [-1, -100, 3, 99], k = 2
# Output: [3, 99, -1, -100]

# 5. Merge two sorted arrays
def merge_sorted(nums1, nums2):
    result = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    result.extend(nums1[i:])
    result.extend(nums2[j:])
    return result

# Input: nums1 = [1, 3, 5], nums2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
# Input: nums1 = [1, 2, 3], nums2 = []
# Output: [1, 2, 3]
```

---

#### Tuple - Immutable Sequences

**Basic Operations:**
```python
# Creation
t = (1, 2, 3)
t = 1, 2, 3           # Parentheses optional
single = (1,)         # Single element (comma required!)
empty = ()

# Accessing
t[0]                  # 1
t[-1]                 # 3
t[0:2]                # (1, 2)

# Unpacking
x, y, z = (1, 2, 3)
first, *rest = (1, 2, 3, 4)  # first=1, rest=[2,3,4]

# Immutable - these DON'T work
# t[0] = 5            # TypeError
# t.append(4)         # AttributeError
```

**Common Interview Problems Using Tuples:**

```python
# 1. Return multiple values from function
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns tuple

minimum, maximum = min_max([1, 2, 3, 4, 5])

# Input: [1, 2, 3, 4, 5]
# Output: minimum = 1, maximum = 5

# 2. Swap variables
a, b = 10, 20
a, b = b, a  # Swap using tuple unpacking

# Before: a = 10, b = 20
# After: a = 20, b = 10

# 3. Enumerate with index and value
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):  # Returns tuples
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# 4. Sort list of tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

# Input: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Output: [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 5. Use tuple as dictionary key (lists can't be keys!)
locations = {}
locations[(10, 20)] = "Point A"  # Tuple as key
locations[(30, 40)] = "Point B"

# Result: {(10, 20): 'Point A', (30, 40): 'Point B'}
# Note: locations[[10, 20]] = "Point A" would raise TypeError!
```

---

#### Dictionary (dict) - Hash Maps

**Basic Operations:**
```python
# Creation
person = {'name': 'Alice', 'age': 30}
person = dict(name='Alice', age=30)
empty = {}

# Access
person['name']              # 'Alice'
person.get('email', 'N/A')  # Safe access with default

# Modification
person = {'name': 'Alice', 'age': 30}

person['city'] = 'NYC'      # Add new key-value pair
print(person)               # {'name': 'Alice', 'age': 30, 'city': 'NYC'}

person['age'] = 31          # Update existing key
print(person)               # {'name': 'Alice', 'age': 31, 'city': 'NYC'}

# update() - Update/add multiple key-value pairs at once
person.update({'age': 32, 'country': 'USA'})
# 'age' already exists -> updates 30 to 32
# 'country' doesn't exist -> adds new key
print(person)               # {'name': 'Alice', 'age': 32, 'city': 'NYC', 'country': 'USA'}

person.update({'city': 'Boston', 'job': 'Engineer'})
print(person)               # {'name': 'Alice', 'age': 32, 'city': 'Boston', 'country': 'USA', 'job': 'Engineer'}

# Deleting
del person['age']           # Delete key 'age'
print(person)               # {'name': 'Alice', 'city': 'Boston', 'country': 'USA', 'job': 'Engineer'}

city = person.pop('city')   # Remove and return value
print(city)                 # 'Boston'
print(person)               # {'name': 'Alice', 'country': 'USA', 'job': 'Engineer'}

# Iteration
for key in person.keys():
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():
    print(f"{key}: {value}")

# Common operations
len(person)                 # Number of key-value pairs
'name' in person            # Check key exists
```

**Common Interview Problems Using Dictionaries:**

```python
# 1. Count frequency of elements
def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Input: [1, 2, 2, 3, 3, 3]
# Output: {1: 1, 2: 2, 3: 3}
# Input: ['a', 'b', 'a', 'c', 'b', 'a']
# Output: {'a': 3, 'b': 2, 'c': 1}

# Or using Counter
from collections import Counter
freq = Counter([1, 2, 2, 3, 3, 3])
# Output: Counter({3: 3, 2: 2, 1: 1})

# 2. Group anagrams
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# 3. Longest substring without repeating characters
def length_of_longest_substring(s):
    char_index = {}
    max_length = start = 0
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Input: "abcabcbb"
# Output: 3 (substring "abc")
# Input: "bbbbb"
# Output: 1 (substring "b")
# Input: "pwwkew"
# Output: 3 (substring "wke")

# 4. Check if two strings are isomorphic
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# Input: s = "egg", t = "add"
# Output: True (e->a, g->d)
# Input: s = "foo", t = "bar"
# Output: False (o can't map to both a and r)
# Input: s = "paper", t = "title"
# Output: True (p->t, a->i, e->l, r->e)

# 5. LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.order = []
    
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        
        self.cache[key] = value
        self.order.append(key)

# Example usage:
# cache = LRUCache(2)
# cache.put(1, 1)  # cache: {1: 1}
# cache.put(2, 2)  # cache: {1: 1, 2: 2}
# cache.get(1)     # returns 1
# cache.put(3, 3)  # evicts key 2, cache: {1: 1, 3: 3}
# cache.get(2)     # returns -1 (not found)
```

---

#### Set - Unique Elements

**Basic Operations:**
```python
# Creation
s = {1, 2, 3}
s = set([1, 2, 2, 3])      # {1, 2, 3} (duplicates removed)
empty = set()               # NOT {} (that's a dict)

# Modification
s.add(4)                    # Add element
s.remove(2)                 # Remove (KeyError if not found)
s.discard(2)                # Remove (no error if not found)
s.clear()                   # Remove all

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b                       # Union: {1, 2, 3, 4, 5, 6}
a & b                       # Intersection: {3, 4}
a - b                       # Difference: {1, 2}
a ^ b                       # Symmetric difference: {1, 2, 5, 6}

# Membership (very fast - O(1))
3 in s                      # True
```

**Common Interview Problems Using Sets:**

```python
# 1. Find unique elements / Remove duplicates
def remove_duplicates(arr):
    return list(set(arr))

# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5] (order may vary)

# 2. Check if array contains duplicates
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

# Input: [1, 2, 3, 1]
# Output: True
# Input: [1, 2, 3, 4]
# Output: False

# 3. Intersection of two arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4] (or [4, 9])

# 4. Find missing number (1 to n)
def find_missing(nums, n):
    return sum(set(range(1, n + 1)) - set(nums))
    # Or: sum(range(1, n+1)) - sum(nums)

# Input: nums = [1, 2, 4, 5], n = 5
# Output: 3
# Input: nums = [3, 7, 1, 2, 8, 4, 5], n = 8
# Output: 6

# 5. Longest consecutive sequence
def longest_consecutive(nums):
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if it's the start of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_length = max(max_length, length)
    
    return max_length

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4 (sequence: 1, 2, 3, 4)
# Input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9 (sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8)

# 6. Find all pairs with given difference
def find_pairs_with_diff(arr, k):
    num_set = set(arr)
    pairs = []
    
    for num in num_set:
        if num + k in num_set:
            pairs.append((num, num + k))
    
    return pairs

# Input: arr = [1, 5, 3, 4, 2], k = 2
# Output: [(1, 3), (3, 5), (2, 4)]
# Input: arr = [8, 12, 16, 4, 0, 20], k = 4
# Output: [(8, 12), (12, 16), (4, 8), (0, 4), (16, 20)]

# 7. Check if valid Sudoku (using sets)
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            box_index = (i // 3) * 3 + (j // 3)
            
            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False
            
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)
    
    return True

# Input: Valid partially filled board
# Output: True
# Input: Board with duplicate '5' in same row
# Output: False
```

### Common Constructs Syntax

#### Conditional Statements

```python
# Basic if
x = 10
if x > 5:
    print("x is greater than 5")

# if-else
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator (one-line if-else)
result = "Even" if x % 2 == 0 else "Odd"
```

---

#### For Loops - Different Forms

```python
# 1. Iterate over list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 2. Iterate with range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step by 2)
    print(i)

# 3. Iterate with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# 4. Iterate over dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Keys only
for key in person:
    print(key)

# Keys explicitly
for key in person.keys():
    print(key)

# Values only
for value in person.values():
    print(value)

# Both keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# 5. Iterate over multiple lists with zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 6. Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 7. Iterate backwards
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

for fruit in reversed(fruits):
    print(fruit)
```

---

#### While Loops

```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1

# While with condition
user_input = ""
while user_input != "quit":
    user_input = input("Enter command (quit to exit): ")
    print(f"You entered: {user_input}")

# Infinite loop with break
while True:
    response = input("Continue? (y/n): ")
    if response == 'n':
        break
    print("Continuing...")
```

---

#### Control Flow: pass, break, continue, return

```python
# pass - Do nothing (placeholder)
# Use when you need a statement but don't want to do anything yet

if x > 10:
    pass  # TODO: implement this later

for i in range(5):
    pass  # Empty loop body

def future_function():
    pass  # Function to be implemented later

# break - Exit loop immediately
for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4

# continue - Skip rest of current iteration, continue with next
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
# Output: 0, 1, 3, 4

# return - Exit function and optionally return a value
# Can be used in if/for/while inside a function

def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Exit function immediately with value
    return None  # If no even found

result = find_first_even([1, 3, 4, 7, 8])
print(result)  # 4

# Where you can use them:
# pass: anywhere (if, for, while, function, class)
# break: only in loops (for, while)
# continue: only in loops (for, while)
# return: only in functions
```

---

#### Functions - Understanding Return

**Python vs Java:**
- **Java**: Must declare return type (`int`, `String`, `void`)
- **Python**: No type declaration needed, function can return anything or nothing

```python
# Function that returns a value
def add(a, b):
    return a + b  # Must explicitly return

result = add(5, 3)
print(result)  # 8

# Function that returns nothing (implicitly returns None)
def greet(name):
    print(f"Hello, {name}")
    # No return statement

result = greet("Alice")  # Prints: Hello, Alice
print(result)  # None (Python auto-returns None)

# Multiple return statements
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Return multiple values (as tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

# Early return
def divide(a, b):
    if b == 0:
        return None  # Early exit
    return a / b

# Function with default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!

# How to know what a function returns?
# 1. Read the docstring
# 2. Look at return statements
# 3. Use type hints (Python 3.5+)

def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        int: Sum of a and b
    """
    return a + b
```

---

#### List Comprehensions - Concise List Creation

List comprehensions provide a compact way to create lists.

**Basic Syntax:** `[expression for item in iterable if condition]`

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension (same result, one line)
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
# Traditional
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

# List comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Transform and filter
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# With if-else (ternary)
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ["a", "ab", "abc", "a"]}
print(unique_lengths)  # {1, 2, 3}
```

---

#### Exception Handling - Try-Except

**Common Exception Types:**
- `ValueError` - Invalid value (e.g., `int("abc")`)
- `TypeError` - Wrong type (e.g., `"2" + 2`)
- `KeyError` - Dictionary key not found
- `IndexError` - List index out of range
- `FileNotFoundError` - File doesn't exist
- `ZeroDivisionError` - Division by zero
- `AttributeError` - Attribute doesn't exist
- `ImportError` - Module import failed

```python
# Basic try-except
try:
    number = int("abc")  # This will raise ValueError
except ValueError:
    print("Invalid number!")

# Catch multiple exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")

# Catch exception and get error message
try:
    number = int("abc")
except ValueError as e:
    print(f"Error occurred: {e}")
    # Output: Error occurred: invalid literal for int() with base 10: 'abc'

# Multiple exceptions in one line
try:
    risky_operation()
except (ValueError, TypeError) as e:
    print(f"Value or Type error: {e}")

# Catch all exceptions (not recommended for production)
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Runs if NO exception

# try-except-finally
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    # Always runs, whether exception occurred or not
    print("Cleanup code here")

# Real-world example
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid types")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Division by zero, None
print(safe_divide(10, "2")) # Error: Invalid types, None

# How to know which exception to catch?
# 1. Run the code and see what error occurs
# 2. Read Python documentation
# 3. Use broad Exception and print the type:

try:
    risky_operation()
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Error message: {e}")
```

---

#### Common Patterns Summary

```python
# Iterate with index
for i, item in enumerate(items):
    print(f"Index {i}: {item}")

# Iterate over two lists together
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Filter and transform
result = [x * 2 for x in numbers if x > 0]

# Safe dictionary access
value = my_dict.get('key', 'default')

# Multiple conditions
if x > 0 and y > 0 and z > 0:
    print("All positive")

# Check if in collection
if item in my_list:
    print("Found!")

# Swap variables
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3
```

### Most Used Built-in Functions (Quick Ref)

`print()`, `len()`, `type()`, `range()`, `enumerate()`, `zip()`, `map()`, `filter()`, `sorted()`, `sum()`, `max()`, `min()`, `abs()`, `round()`, `input()`, `open()`, `list()`, `dict()`, `set()`, `str()`, `int()`, `float()`, `bool()`, `all()`, `any()`

### Most Used Standard Library Modules

**Collections**: `collections`, **Itertools**: `itertools`, **Math**: `math`, **Random**: `random`, **Date/Time**: `datetime`, **Files**: `os`, `pathlib`, **JSON**: `json`, **Regex**: `re`, **System**: `sys`

---

## The print() Function - Your Best Friend

The `print()` function is the most important function for beginners. Master it first!

### Basic Usage

```python
# Simple print
print("Hello, World!")

# Multiple arguments (separated by space)
print("Hello", "World")  # Output: Hello World

# Print numbers
print(42)
print(3.14)
```

### Separators and Endings

```python
# Custom separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print(1, 2, 3, 4, sep=" | ")
# Output: 1 | 2 | 3 | 4

# Custom ending (default is newline '\n')
print("Loading", end="...")
print("Done")
# Output: Loading...Done

# No newline
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
```

### Formatted Output

```python
name = "Alice"
age = 30
salary = 75000.50

# f-strings (Python 3.6+, recommended)
print(f"My name is {name}")
print(f"{name} is {age} years old")
print(f"Salary: ${salary:,.2f}")  # Output: Salary: $75,000.50

# format() method
print("My name is {}".format(name))
print("{} is {} years old".format(name, age))

# % formatting (old style)
print("My name is %s" % name)
print("%s is %d years old" % (name, age))
```

### Advanced Formatting

```python
# Number formatting
num = 42
print(f"{num:05}")      # Output: 00042 (pad with zeros)
print(f"{num:>10}")     # Output:        42 (right align)
print(f"{num:<10}")     # Output: 42         (left align)
print(f"{num:^10}")     # Output:     42     (center)

# Float precision
pi = 3.14159265359
print(f"{pi:.2f}")      # Output: 3.14
print(f"{pi:.4f}")      # Output: 3.1416

# Percentage
ratio = 0.75
print(f"{ratio:.1%}")   # Output: 75.0%

# Thousands separator
big_num = 1000000
print(f"{big_num:,}")   # Output: 1,000,000
```

### Printing Data Structures

```python
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Print each item
for fruit in fruits:
    print(fruit)

# Dictionaries
person = {"name": "Bob", "age": 25}
print(person)  # Output: {'name': 'Bob', 'age': 25}

# Pretty print dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

### Debugging with print()

```python
# Variable inspection
x = 10
print(f"x = {x}")
print(f"{x = }")  # Python 3.8+, Output: x = 10

# Multiple variables
a, b, c = 1, 2, 3
print(f"{a = }, {b = }, {c = }")

# Type checking
data = [1, 2, 3]
print(f"Type: {type(data)}, Value: {data}")
```

### Print to File

```python
# Write to file instead of console
with open("output.txt", "w") as f:
    print("This goes to file", file=f)
    print("Another line", file=f)
```

---

## Built-in Functions (Alphabetically)

### abs() - Absolute Value

```python
abs(-5)        # 5
abs(-3.14)     # 3.14
abs(3 + 4j)    # 5.0 (magnitude of complex number)
```

**Use case**: Distance calculations, error margins

---

### all() - Check if All True

```python
all([True, True, True])    # True
all([True, False, True])   # False
all([1, 2, 3])             # True (non-zero = True)
all([1, 0, 3])             # False
all([])                    # True (empty is True)

# Practical use
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True (all even)
```

**Use case**: Validation, checking conditions

---

### any() - Check if Any True

```python
any([False, False, False])  # False
any([False, True, False])   # True
any([0, 0, 1])              # True
any([])                     # False (empty is False)

# Practical use
numbers = [1, 3, 5, 8]
print(any(n % 2 == 0 for n in numbers))  # True (has even number)
```

**Use case**: Finding matches, conditional checks

---

### enumerate() - Index and Value

```python
fruits = ["apple", "banana", "cherry"]

# Get index and value
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start from custom index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# Output:
# 1. apple
# 2. banana
# 3. cherry
```

**Use case**: Iteration with index, numbered lists

---

### filter() - Filter Iterable

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Using function
def is_positive(n):
    return n > 0

nums = [-2, -1, 0, 1, 2]
positives = list(filter(is_positive, nums))
print(positives)  # [1, 2]
```

**Use case**: Data filtering, validation

---

### input() - Get User Input

```python
# Basic input (always returns string)
name = input("Enter your name: ")
print(f"Hello, {name}")

# Convert to number
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

# With validation
while True:
    try:
        age = int(input("Enter age: "))
        if age > 0:
            break
    except ValueError:
        print("Please enter a valid number")
```

**Use case**: Interactive programs, user data

---

### isinstance() - Check Type

```python
isinstance(5, int)              # True
isinstance(5.0, float)          # True
isinstance("hello", str)        # True
isinstance([1, 2], list)        # True

# Multiple types
isinstance(5, (int, float))     # True
isinstance("hi", (int, str))    # True

# Use in functions
def process(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, str):
        return data.upper()
    else:
        return data
```

**Use case**: Type checking, polymorphic functions

---

### len() - Length

```python
len("hello")              # 5
len([1, 2, 3, 4])        # 4
len({"a": 1, "b": 2})    # 2
len((1, 2, 3))           # 3
len({1, 2, 3})           # 3
len(range(10))           # 10
```

**Use case**: Size checking, iteration limits

---

### map() - Apply Function

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Convert to strings
strings = list(map(str, numbers))
print(strings)  # ['1', '2', '3', '4', '5']

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # [11, 22, 33]
```

**Use case**: Transformations, batch operations

---

### max() / min() - Maximum / Minimum

```python
max(1, 5, 3, 9, 2)           # 9
min(1, 5, 3, 9, 2)           # 1

max([1, 5, 3, 9, 2])         # 9
max("hello")                 # 'o'

# With key function
words = ["apple", "pie", "zoo", "a"]
longest = max(words, key=len)
print(longest)  # "apple"

# Dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
best_student = max(scores, key=scores.get)
print(best_student)  # Bob
```

**Use case**: Finding extremes, optimization

---

### open() - File Operations

```python
# Reading
with open("file.txt", "r") as f:
    content = f.read()

# Reading lines
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Writing (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Appending
with open("file.txt", "a") as f:
    f.write("New line\n")

# Reading and writing
with open("data.txt", "r+") as f:
    content = f.read()
    f.write("Appended")
```

**Use case**: File I/O, data persistence

---

### range() - Generate Sequence

```python
# range(stop)
list(range(5))           # [0, 1, 2, 3, 4]

# range(start, stop)
list(range(2, 8))        # [2, 3, 4, 5, 6, 7]

# range(start, stop, step)
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]
list(range(10, 0, -1))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Common uses
for i in range(5):
    print(i)

# Reverse iteration
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])
```

**Use case**: Loops, index generation

---

### round() - Round Numbers

```python
round(3.7)          # 4
round(3.4)          # 3
round(3.5)          # 4 (rounds to nearest even)

# Decimal places
round(3.14159, 2)   # 3.14
round(1234.5678, 1) # 1234.6
round(1234, -1)     # 1230 (round to tens)
round(1234, -2)     # 1200 (round to hundreds)
```

**Use case**: Precision control, display formatting

---

### sorted() - Sort Iterable

```python
sorted([3, 1, 4, 1, 5, 9])              # [1, 1, 3, 4, 5, 9]
sorted([3, 1, 4], reverse=True)         # [4, 3, 1]
sorted("hello")                         # ['e', 'h', 'l', 'l', 'o']

# Sort by key
words = ["apple", "pie", "zoo", "a"]
sorted(words, key=len)                  # ['a', 'pie', 'zoo', 'apple']

# Sort tuples
data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted(data, key=lambda x: x[1])       # [(2, 'a'), (1, 'b'), (3, 'c')]

# Sort dictionary by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted(scores.items(), key=lambda x: x[1], reverse=True)
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

**Use case**: Data organization, ranking

---

### sum() - Sum Iterable

```python
sum([1, 2, 3, 4, 5])              # 15
sum((1, 2, 3))                    # 6
sum(range(10))                    # 45

# With start value
sum([1, 2, 3], 10)                # 16 (10 + 1 + 2 + 3)

# Average calculation
numbers = [85, 90, 78, 92]
average = sum(numbers) / len(numbers)
print(average)  # 86.25
```

**Use case**: Calculations, aggregations

---

### type() - Get Type

```python
type(42)                # <class 'int'>
type(3.14)              # <class 'float'>
type("hello")           # <class 'str'>
type([1, 2, 3])         # <class 'list'>
type({"a": 1})          # <class 'dict'>

# Use in conditionals
x = [1, 2, 3]
if type(x) == list:
    print("It's a list")

# Better: use isinstance()
if isinstance(x, list):
    print("It's a list")
```

**Use case**: Type checking, debugging

---

### zip() - Combine Iterables

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Combine
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Output:
# Alice: 85
# Bob: 92
# Charlie: 78

# Create dictionary
result = dict(zip(names, scores))
print(result)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Multiple iterables
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [10, 20, 30]
for x, y, z in zip(a, b, c):
    print(x, y, z)

# Unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

**Use case**: Parallel iteration, data pairing

---

## String Methods

Strings are immutable - all methods return new strings.

### capitalize() / title() / upper() / lower()

```python
text = "hello world"

text.capitalize()  # "Hello world"
text.title()       # "Hello World"
text.upper()       # "HELLO WORLD"
text.lower()       # "hello world"

# Case conversion
text.swapcase()    # "HELLO WORLD" → "hello world"
```

---

### count() - Count Occurrences

```python
text = "hello world"
text.count('l')      # 3
text.count('o')      # 2
text.count('ll')     # 1
text.count('x')      # 0
```

---

### endswith() / startswith()

```python
filename = "document.pdf"
filename.endswith('.pdf')      # True
filename.endswith(('.pdf', '.doc'))  # True
filename.startswith('doc')     # True

# Case sensitive
"Hello".startswith('h')        # False
"Hello".startswith('H')        # True
```

---

### find() / rfind() / index()

```python
text = "hello world"
text.find('o')        # 4 (first occurrence)
text.rfind('o')       # 7 (last occurrence)
text.find('x')        # -1 (not found)

text.index('o')       # 4
text.index('x')       # ValueError (not found)
```

---

### format() - String Formatting

```python
# Positional
"{} {}".format("hello", "world")  # "hello world"

# Named
"{name} is {age}".format(name="Alice", age=30)

# Indexed
"{0} {1} {0}".format("hello", "world")  # "hello world hello"
```

---

### join() - Join Iterable

```python
# Join list
words = ["apple", "banana", "cherry"]
", ".join(words)           # "apple, banana, cherry"
" ".join(words)            # "apple banana cherry"
"".join(words)             # "applebananacherry"

# Join characters
"".join(['h', 'i'])        # "hi"

# Path joining (use os.path.join for real paths)
"/".join(["home", "user", "docs"])  # "home/user/docs"
```

---

### replace() - Replace Substring

```python
text = "hello world"
text.replace('world', 'Python')  # "hello Python"
text.replace('l', 'L')           # "heLLo worLd"
text.replace('l', 'L', 2)        # "heLLo world" (max 2 replacements)

# Remove characters
text.replace(' ', '')            # "helloworld"
```

---

### split() / rsplit() - Split String

```python
text = "apple,banana,cherry"
text.split(',')                  # ['apple', 'banana', 'cherry']

text = "hello world python"
text.split()                     # ['hello', 'world', 'python'] (whitespace)
text.split(' ', 1)              # ['hello', 'world python'] (max 1 split)

# Multiline text
lines = "line1\nline2\nline3"
lines.split('\n')               # ['line1', 'line2', 'line3']
lines.splitlines()              # ['line1', 'line2', 'line3']
```

---

### strip() / lstrip() / rstrip() - Remove Whitespace

```python
text = "  hello  "
text.strip()      # "hello"
text.lstrip()     # "hello  "
text.rstrip()     # "  hello"

# Remove specific characters
"###hello###".strip('#')   # "hello"
"www.example.com".lstrip('w.')  # "example.com"
```

---

## List Methods

Lists are mutable - methods modify in place (except a few).

### append() - Add Single Item

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Append list (as single item)
fruits.append(["orange", "grape"])
print(fruits)  # ['apple', 'banana', 'cherry', ['orange', 'grape']]
```

---

### extend() - Add Multiple Items

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "orange"])
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Also works with any iterable
fruits.extend("hi")
print(fruits)  # [..., 'h', 'i']
```

---

### insert() - Insert at Index

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # ['apple', 'banana', 'cherry']

fruits.insert(0, "first")   # Insert at beginning
fruits.insert(len(fruits), "last")  # Insert at end
```

---

### remove() - Remove First Match

```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana']

# Remove again
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

# ValueError if not found
fruits.remove("orange")  # ValueError
```

---

### pop() - Remove and Return

```python
fruits = ["apple", "banana", "cherry"]

# Remove last item
last = fruits.pop()
print(last)    # "cherry"
print(fruits)  # ['apple', 'banana']

# Remove by index
first = fruits.pop(0)
print(first)   # "apple"
print(fruits)  # ['banana']
```

---

### clear() - Remove All

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # []
```

---

### index() - Find Index

```python
fruits = ["apple", "banana", "cherry"]
fruits.index("banana")    # 1

# ValueError if not found
fruits.index("orange")    # ValueError

# Start and end positions
fruits.index("banana", 0, 3)  # Search in range
```

---

### count() - Count Occurrences

```python
numbers = [1, 2, 3, 2, 4, 2, 5]
numbers.count(2)     # 3
numbers.count(10)    # 0
```

---

### sort() - Sort In Place

```python
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

# Reverse
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Custom key
words = ["apple", "pie", "zoo", "a"]
words.sort(key=len)
print(words)  # ['a', 'pie', 'zoo', 'apple']
```

---

### reverse() - Reverse In Place

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # ['cherry', 'banana', 'apple']
```

---

### copy() - Shallow Copy

```python
original = [1, 2, 3]
copy = original.copy()
copy.append(4)

print(original)  # [1, 2, 3]
print(copy)      # [1, 2, 3, 4]

# Same as
copy = original[:]
copy = list(original)
```

---

## Dictionary Methods

### get() - Safe Access

```python
person = {"name": "Alice", "age": 30}

person.get("name")         # "Alice"
person.get("email")        # None
person.get("email", "N/A") # "N/A" (default)

# Better than
person["email"]  # KeyError
```

---

### keys() / values() / items()

```python
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Keys
list(person.keys())    # ['name', 'age', 'city']

# Values
list(person.values())  # ['Alice', 30, 'NYC']

# Items (key-value pairs)
list(person.items())   # [('name', 'Alice'), ('age', 30), ('city', 'NYC')]

# Iteration
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

---

### update() - Update Multiple

```python
person = {"name": "Alice", "age": 30}
person.update({"age": 31, "city": "NYC"})
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'NYC'}

# From another dict
defaults = {"country": "USA", "status": "active"}
person.update(defaults)
```

---

### pop() / popitem()

```python
person = {"name": "Alice", "age": 30}

# Remove and return value
age = person.pop("age")
print(age)      # 30
print(person)   # {'name': 'Alice'}

# With default
email = person.pop("email", "none")
print(email)    # "none"

# Remove and return arbitrary item
item = person.popitem()
print(item)     # ('name', 'Alice')
```

---

### setdefault() - Get or Set

```python
person = {"name": "Alice"}

# Get existing
name = person.setdefault("name", "Unknown")
print(name)  # "Alice"

# Set if missing
age = person.setdefault("age", 0)
print(age)      # 0
print(person)   # {'name': 'Alice', 'age': 0}
```

---

## Set Methods

### add() / remove() / discard()

```python
fruits = {"apple", "banana"}

# Add single item
fruits.add("cherry")

# Remove (raises KeyError if missing)
fruits.remove("banana")

# Discard (no error if missing)
fruits.discard("orange")  # No error
```

---

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
a | b              # {1, 2, 3, 4, 5, 6}
a.union(b)

# Intersection
a & b              # {3, 4}
a.intersection(b)

# Difference
a - b              # {1, 2}
a.difference(b)

# Symmetric difference
a ^ b              # {1, 2, 5, 6}
a.symmetric_difference(b)
```

---

## Essential Standard Library Modules

### collections - Specialized Containers

```python
from collections import Counter, defaultdict, deque

# Counter - Count elements
text = "hello world"
counter = Counter(text)
print(counter)  # Counter({'l': 3, 'o': 2, 'h': 1, ...})
print(counter.most_common(2))  # [('l', 3), ('o', 2)]

# defaultdict - Dict with default values
word_count = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_count[word] += 1  # No KeyError

# deque - Double-ended queue
queue = deque([1, 2, 3])
queue.append(4)      # Add right
queue.appendleft(0)  # Add left
queue.pop()          # Remove right
queue.popleft()      # Remove left
```

---

### itertools - Iterator Functions

```python
from itertools import combinations, permutations, product, chain

# Combinations
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# Permutations
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Cartesian product
list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Chain - flatten
list(chain([1, 2], [3, 4], [5, 6]))
# [1, 2, 3, 4, 5, 6]
```

---

### datetime - Date and Time

```python
from datetime import datetime, timedelta, date

# Current time
now = datetime.now()
print(now)  # 2025-11-17 14:30:45.123456

# Create specific datetime
dt = datetime(2025, 12, 31, 23, 59, 59)

# Formatting
now.strftime("%Y-%m-%d")      # "2025-11-17"
now.strftime("%B %d, %Y")     # "November 17, 2025"

# Parsing
date_str = "2025-11-17"
dt = datetime.strptime(date_str, "%Y-%m-%d")

# Arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
```

---

### os - Operating System

```python
import os

# Current directory
os.getcwd()

# Change directory
os.chdir('/path/to/dir')

# List files
os.listdir('.')

# File operations
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.isdir('directory')
os.path.join('dir', 'file.txt')

# Environment variables
os.environ.get('HOME')
os.getenv('PATH')
```

---

### pathlib - Object-Oriented Paths

```python
from pathlib import Path

# Current directory
path = Path.cwd()

# Home directory
home = Path.home()

# Create path
file_path = Path('data/file.txt')

# Check existence
file_path.exists()
file_path.is_file()
file_path.is_dir()

# Read/Write
content = file_path.read_text()
file_path.write_text("Hello")

# List files
for file in Path('.').glob('*.txt'):
    print(file)
```

---

### json - JSON Data

```python
import json

# Python to JSON
data = {"name": "Alice", "age": 30, "active": True}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Alice", "age": 30, "active": true}'

# Pretty print
print(json.dumps(data, indent=2))

# JSON to Python
parsed = json.loads(json_string)

# File operations
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r') as f:
    data = json.load(f)
```

---

### re - Regular Expressions

```python
import re

# Match pattern
pattern = r'\d+'  # One or more digits
text = "I have 2 apples and 5 oranges"

# Find all
numbers = re.findall(pattern, text)
print(numbers)  # ['2', '5']

# Search
match = re.search(r'\d+', text)
if match:
    print(match.group())  # '2'

# Replace
result = re.sub(r'\d+', 'X', text)
print(result)  # 'I have X apples and X oranges'

# Email validation
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
re.match(email_pattern, 'user@example.com')  # Match object
```

---

### random - Random Numbers

```python
import random

# Random float [0.0, 1.0)
random.random()

# Random integer
random.randint(1, 10)      # Includes both endpoints
random.randrange(1, 10)    # Excludes end (like range)

# Random choice
fruits = ['apple', 'banana', 'cherry']
random.choice(fruits)

# Multiple choices (with replacement)
random.choices(fruits, k=3)

# Sample (without replacement)
random.sample(fruits, 2)

# Shuffle in place
random.shuffle(fruits)
```

---

### math - Mathematical Functions

```python
import math

# Constants
math.pi       # 3.141592653589793
math.e        # 2.718281828459045

# Rounding
math.ceil(3.2)    # 4
math.floor(3.8)   # 3

# Power and logs
math.sqrt(16)     # 4.0
math.pow(2, 3)    # 8.0
math.log(10)      # 2.302585092994046 (natural log)
math.log10(100)   # 2.0

# Trigonometry
math.sin(math.pi / 2)  # 1.0
math.cos(0)            # 1.0
```

---

## List Comprehensions (Common Patterns)

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Transform strings
words = ["hello", "world"]
upper = [w.upper() for w in words]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]

# Flatten
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique_lengths = {len(word) for word in ["a", "ab", "abc", "a"]}
```

---

## Lambda Functions (Common Uses)

```python
# Sort by custom key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted(students, key=lambda x: x[1])

# Map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# In dictionary
operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y
}
operations['add'](5, 3)  # 8
```

---

## Common Coding Patterns

### Frequency Counter

```python
# Count occurrences
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Using Counter
from collections import Counter
freq = Counter(text)
```

### Two Pointer Technique

```python
# Check palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Sliding Window

```python
# Max sum of k consecutive elements
def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

---

## Quick Tips for Coding Interviews

### Time Complexity Cheat Sheet

| Operation | List | Dict | Set |
|-----------|------|------|-----|
| Access by index | O(1) | N/A | N/A |
| Access by key | N/A | O(1) | N/A |
| Search | O(n) | O(1) | O(1) |
| Insert | O(n) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |
| Append | O(1) | O(1) | O(1) |

### Must-Know Tricks

```python
# Swap without temp
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Unpacking
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]

# Ternary operator
result = "even" if x % 2 == 0 else "odd"

# Check multiple conditions
if x in [1, 2, 3, 4, 5]:
    pass

# Default dict value
d.get(key, default_value)
d.setdefault(key, default_value)

# List to dict
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))

# Remove duplicates (keep order)
seen = set()
unique = [x for x in items if not (x in seen or seen.add(x))]
```

---

Happy coding! 🐍

