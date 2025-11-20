# Data Structures Exercises and Analysis

## Exercise 1: Time Complexity Analysis

### Question

How many question marks does the following code segment output?

```python
for i in range(3 * n):
    for j in range(2 * n):
        print("?")
```

### Solution

**Analysis:**
- The outer loop iterates `3n` times
- For each iteration of the outer loop, the inner loop iterates `2n` times
- Total executions: `3n × 2n = 6n²`

**Answer:** The code outputs **6n²** question marks.

**Time Complexity:** O(n²)

---

## Exercise 2: Postfix Expression Evaluation

### Question

What does the postfix expression `4 1 + 8 4 2 * / -` evaluate to?

a. 9  
b. 10  
c. 3  
d. 4  
e. None of the above

### Solution

**Step-by-step evaluation using a stack:**

1. Push 4 → Stack: `[4]`
2. Push 1 → Stack: `[4, 1]`
3. `+` → Pop 1 and 4, compute 4+1=5, push 5 → Stack: `[5]`
4. Push 8 → Stack: `[5, 8]`
5. Push 4 → Stack: `[5, 8, 4]`
6. Push 2 → Stack: `[5, 8, 4, 2]`
7. `*` → Pop 2 and 4, compute 4×2=8, push 8 → Stack: `[5, 8, 8]`
8. `/` → Pop 8 and 8, compute 8÷8=1, push 1 → Stack: `[5, 1]`
9. `-` → Pop 1 and 5, compute 5-1=4, push 4 → Stack: `[4]`

**Answer:** d. **4**

---

## Exercise 3: Loop Time Complexity

### Question

What's the big-O running time of the following code segment?

```python
i = 1
while i < n:
    i = i * 2
```

a. O(1)  
b. O(n)  
c. O(log n)  
d. O(n log n)  
e. O(n²)  
f. O(2ⁿ)

### Solution

**Analysis:**
- `i` starts at 1
- Each iteration: `i` is multiplied by 2
- Sequence: 1, 2, 4, 8, 16, ..., 2^k
- Loop terminates when `2^k >= n`
- Therefore: `k = log₂(n)` iterations

**Answer:** c. **O(log n)**

---

## Exercise 4: Stack Operations

### Question

Given the following sequence of stack operations, what is the top item on the stack when the sequence is complete?

```python
m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    m.pop()
    m.pop()
```

### Solution

**Step-by-step execution:**

1. Push 'x', 'y', 'z' → Stack: `['x', 'y', 'z']` (z on top)
2. **First iteration:**
   - `m.is_empty()` is False
   - First `m.pop()` removes 'z' → Stack: `['x', 'y']`
   - Second `m.pop()` removes 'y' → Stack: `['x']`
3. **Second iteration:**
   - `m.is_empty()` is False
   - First `m.pop()` removes 'x' → Stack: `[]`
   - Second `m.pop()` attempts to pop from empty stack → **Error!**

**Answer:** An error occurs. The while loop attempts to pop from an empty stack, which raises an exception.

---

## Exercise 5: Complete Tree Structure

### Question

What's the minimum number of nodes that a complete tree of height 3 can have?

(Recall that a tree with a single node has height 0.)

### Solution

**Analysis:**

A complete binary tree must have all levels fully filled except possibly the last level, which is filled from left to right.

For height 3:
- **Level 0:** 1 node (root)
- **Level 1:** 2 nodes
- **Level 2:** 4 nodes
- **Level 3:** At least 1 node (leftmost position)

**Total:** 1 + 2 + 4 + 1 = **8 nodes**

**Formula:** Minimum nodes for complete tree of height h = 2^h + 1 (when only leftmost node exists at bottom level)

---

## Exercise 6: Linked List Method Implementation

### Question

Consider the linked list implementation provided in `unordered_list.py`. Add the following method to the `UnorderedList` class:

```python
def no_repeating(self):
```

Returns `True` if the list contains no consecutively repeating numbers, `False` otherwise.

**Examples:**
- List `[3, 4, 5, 10, 8, 5, 9]` → returns `True`
- List `[3, 5, 5, 2, 1]` → returns `False`

### Solution

```python
def no_repeating(self):
    """Check if list has no consecutively repeating elements.

    Returns:
        bool: True if no consecutive duplicates exist, False otherwise.
    """
    # Handle empty list or single element
    if self.head is None or self.head.get_next() is None:
        return True

    # Keep track of previous and current elements
    prev = self.head
    current = self.head.get_next()

    # Traverse the list comparing consecutive elements
    while current is not None:
        # If there's a match, we have repeating consecutive values
        if current.get_data() == prev.get_data():
            return False

        # Advance to next pair
        prev = current
        current = current.get_next()

    # No repeating consecutive values found
    return True
```

**Time Complexity:** O(n) - single pass through the list  
**Space Complexity:** O(1) - constant extra space

---

## Complexity Summary Table

| Algorithm/Operation        | Time Complexity | Space Complexity |
|---------------------------|-----------------|------------------|
| Nested loops (3n × 2n)    | O(n²)           | O(1)             |
| Postfix evaluation        | O(n)            | O(n)             |
| Doubling loop (i *= 2)    | O(log n)        | O(1)             |
| Stack operations          | O(1) per op     | O(n) for n items |
| Complete tree traversal   | O(n)            | O(h) for height  |
| Linked list traversal     | O(n)            | O(1)             |

---

## Key Concepts

### Stack Applications
- Expression evaluation (postfix, prefix, infix)
- Function call management (call stack)
- Undo mechanisms
- Backtracking algorithms

### Time Complexity Patterns
- **O(1):** Direct access, basic arithmetic
- **O(log n):** Binary search, divide-and-conquer
- **O(n):** Single loop, linear traversal
- **O(n log n):** Efficient sorting (merge sort, heap sort)
- **O(n²):** Nested loops, bubble sort
- **O(2ⁿ):** Naive recursive algorithms (Fibonacci)

### Tree Properties
- **Complete Binary Tree:** All levels filled except possibly last (filled left-to-right)
- **Height:** Longest path from root to leaf
- **Minimum nodes at height h:** 2^h + 1
- **Maximum nodes at height h:** 2^(h+1) - 1

### Linked List Operations
- **Traversal:** O(n) time, O(1) space
- **Search:** O(n) average and worst case
- **Insertion at head:** O(1)
- **Insertion at tail:** O(n) without tail pointer
- **Deletion:** O(n) to find element, O(1) to remove

---

## Practice Tips

1. **Big-O Analysis:** Focus on the dominant term and drop constants
2. **Stack Evaluation:** Use paper/whiteboard to track stack state
3. **Tree Properties:** Memorize formulas for common structures
4. **Linked Lists:** Draw diagrams to visualize pointer operations
5. **Testing:** Always consider edge cases (empty, single element, duplicates)
