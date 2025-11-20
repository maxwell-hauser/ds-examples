# Data Structures Exercises## More Exercise Questions!



## Exercise 1: Time Complexity Analysis### 1. How many question marks does the code segment below output?

```python

### Questionfor i in range(3 * n):

  for j in range(2 * n):

How many question marks does the code segment below output?    print(“?”)

```

```python

for i in range(3 * n):#### Solution

    for j in range(2 * n):The outer loop iterates 3n times.

        print("?")For each iteration of the outer loop, the inner loop iterates 2n times.

```In total, the print statement executes 3n x 2n times = 6n^2

 

### Solution### 2. What does the postfix expression 4 1 + 8 4 2 */ - evaluate to?

a. 9

The outer loop iterates `3n` times.b. 10

c. 3

For each iteration of the outer loop, the inner loop iterates `2n` times.d. 4

e. None of the above

In total, the print statement executes `3n × 2n = 6n²` times.

#### Solution:

**Answer:** The code outputs `6n²` question marks.d. 4



## Exercise 2: Postfix Expression Evaluation### 3. What’s the big-O running time of the following code segment?

```python

### Questioni = 1

while i < n:

What does the postfix expression `4 1 + 8 4 2 * / -` evaluate to?  i = i * 2

```

a. 9

b. 10a. O(1)

c. 3b. O(n)

d. 4c. O(log n)

e. None of the aboved. O(nlog n)

e. O(n2)

### Solutionf. O(2n)



Step-by-step evaluation using a stack:#### Solution:

c.

1. Push 4 → Stack: `[4]`Since i doubles at every iteration, it takes log2n iterations for i to exceed n. Therefore, the big-O efficiency is O(log n)

2. Push 1 → Stack: `[4, 1]`

3. `+` → Pop 1 and 4, push 5 → Stack: `[5]`### 4. Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?

4. Push 8 → Stack: `[5, 8]````python

5. Push 4 → Stack: `[5, 8, 4]`m = Stack()

6. Push 2 → Stack: `[5, 8, 4, 2]`m.push(‘x’)

7. `*` → Pop 2 and 4, push 8 → Stack: `[5, 8, 8]`m.push(‘y’)

8. `/` → Pop 8 and 8, push 1 → Stack: `[5, 1]`m.push(‘z’)

9. `-` → Pop 1 and 5, push 4 → Stack: `[4]`while not m.is_empty():

  m.pop()

**Answer:** d. 4  m.pop()

```

## Exercise 3: Loop Time Complexity

#### Solution

### QuestionAn error will occur.

The while loop attempts to pop an empty stack which causes an error.

What's the big-O running time of the following code segment?

### 5. What’s the minimum number of nodes that a complete tree of height 3 can have?

```pythonRecall that a tree with a single node has height 0. 

i = 1

while i < n:#### Solution

    i = i * 2The smallest complete tree of height three has a single leaf node at level 3. The number of nodes, starting with level 0 = 1 + 2 + 4 + 1 = 8

```



a. O(1)### 6. Consider the linked list implementation provided in unordered_list.py

b. O(n)Add the following method to the UnorderedList class:

c. O(log n)```py

d. O(n log n)def no_repeating(self):

e. O(n²)```

f. O(2ⁿ)

Returns

### Solution```py

 True 

Since `i` doubles at every iteration, it takes `log₂(n)` iterations for `i` to exceed `n`.```

if the list contains no consecutively repeating numbers.

**Answer:** c. O(log n)

Returns

## Exercise 4: Stack Operations```py

 False

### Question```

otherwise.

Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?

For instance, if list aList had the elements 3, 4, 5, 10, 8, 5, 9, the call aList.no_repeating() would return True.

```python

m = Stack()A list with elements 3, 5, 5, 2, 1 would return False.

m.push('x')

m.push('y')#### Solution

m.push('z')Implemented as part of class UnorderedList.

while not m.is_empty():

    m.pop()```py

    m.pop()def no_repeating(self):

```# keep track of previous and current elements

prev = self.head()

### Solutioncurrent = self.head.get_next()



Step-by-step execution:# if the list has one element, it’s non-repeating

if not current:

1. Push 'x', 'y', 'z' → Stack: `['x', 'y', 'z']` (z on top)  return True

2. First iteration: Pop 'z', then pop 'y' → Stack: `['x']`

3. Second iteration: Pop 'x', then attempt to pop from empty stack → **Error!**# while not at the end of the list, compare previous 

# and current

**Answer:** An error will occur. The while loop attempts to pop an empty stack, which causes an exception.while current:

  

## Exercise 5: Complete Tree Structure  # if there’s a match, we have repeating #*consecutive*values. Return False. 

  if current.get_data() == prev.get_data():

### Question    return False

  

What's the minimum number of nodes that a complete tree of height 3 can have?  # advance previous and current

  prev = current

(Recall that a tree with a single node has height 0.)  current = current.get_next()



### Solution# if we’ve reached the end of the list, it must be 

#the case that there were no repeating consecutive #values. 

A complete tree must have all levels fully filled except possibly the last level, which must be filled from left to right.return True

```

For height 3:

- Level 0: 1 node (root)
- Level 1: 2 nodes
- Level 2: 4 nodes
- Level 3: At least 1 node (leftmost position)

**Total:** 1 + 2 + 4 + 1 = **8 nodes**

## Exercise 6: Linked List Method

### Question

Consider the linked list implementation provided in `unordered_list.py`. Add the following method to the `UnorderedList` class:

```python
def no_repeating(self):
```

Returns `True` if the list contains no consecutively repeating numbers, `False` otherwise.

For instance:

- A list with elements `[3, 4, 5, 10, 8, 5, 9]` would return `True`.
- A list with elements `[3, 5, 5, 2, 1]` would return `False`.

### Solution

```python
def no_repeating(self):
    """Check if list has no consecutively repeating elements.

    Returns:
        True if no consecutive duplicates exist, False otherwise.
    """
    # Keep track of previous and current elements
    prev = self.head
    current = self.head.get_next()

    # If the list has one element, it's non-repeating
    if not current:
        return True

    # While not at the end of the list, compare previous and current
    while current:
        # If there's a match, we have repeating consecutive values
        if current.get_data() == prev.get_data():
            return False

        # Advance previous and current
        prev = current
        current = current.get_next()

    # If we've reached the end of the list, there were no
    # repeating consecutive values
    return True
```
