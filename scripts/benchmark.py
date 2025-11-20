"""Benchmark script for data structure operations.

Measures the performance of Stack, Queue, LinkedList, and BinaryTree
operations with varying input sizes.
"""

import sys
import time
import random
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ds_examples import Stack, Queue, LinkedList, BinaryTree


def benchmark_stack(size: int) -> dict:
    """Benchmark Stack operations."""
    s = Stack()
    
    # Push operations
    start = time.perf_counter()
    for i in range(size):
        s.push(i)
    push_time = time.perf_counter() - start
    
    # Peek operations
    start = time.perf_counter()
    for _ in range(min(1000, size)):
        s.peek()
    peek_time = time.perf_counter() - start
    
    # Pop operations
    start = time.perf_counter()
    for _ in range(size):
        s.pop()
    pop_time = time.perf_counter() - start
    
    return {
        "push": push_time,
        "peek": peek_time,
        "pop": pop_time,
    }


def benchmark_queue(size: int) -> dict:
    """Benchmark Queue operations."""
    q = Queue()
    
    # Enqueue operations
    start = time.perf_counter()
    for i in range(size):
        q.enqueue(i)
    enqueue_time = time.perf_counter() - start
    
    # Peek operations
    start = time.perf_counter()
    for _ in range(min(1000, size)):
        q.peek()
    peek_time = time.perf_counter() - start
    
    # Dequeue operations
    start = time.perf_counter()
    for _ in range(size):
        q.dequeue()
    dequeue_time = time.perf_counter() - start
    
    return {
        "enqueue": enqueue_time,
        "peek": peek_time,
        "dequeue": dequeue_time,
    }


def benchmark_linked_list(size: int) -> dict:
    """Benchmark LinkedList operations."""
    ll = LinkedList()
    
    # Append operations
    start = time.perf_counter()
    for i in range(size):
        ll.append(i)
    append_time = time.perf_counter() - start
    
    # Find operations (search for middle element)
    mid = size // 2
    start = time.perf_counter()
    for _ in range(100):
        ll.find(lambda v: v == mid)
    find_time = time.perf_counter() - start
    
    # Remove operations (remove first 100 elements)
    start = time.perf_counter()
    for i in range(min(100, size)):
        ll.remove(i)
    remove_time = time.perf_counter() - start
    
    return {
        "append": append_time,
        "find": find_time,
        "remove": remove_time,
    }


def benchmark_binary_tree(size: int) -> dict:
    """Benchmark BinaryTree operations."""
    bt = BinaryTree()
    
    # Generate random values to avoid degenerate tree
    values = list(range(size))
    random.shuffle(values)
    
    # Insert operations
    start = time.perf_counter()
    for val in values:
        bt.insert(val)
    insert_time = time.perf_counter() - start
    
    # Find operations
    mid = size // 2
    start = time.perf_counter()
    for _ in range(min(1000, size)):
        bt.find(mid)
    find_time = time.perf_counter() - start
    
    # Traversal operations
    start = time.perf_counter()
    bt.inorder()
    traversal_time = time.perf_counter() - start
    
    return {
        "insert": insert_time,
        "find": find_time,
        "inorder": traversal_time,
    }


def format_time(seconds: float) -> str:
    """Format time in appropriate units."""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} µs"
    elif seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    else:
        return f"{seconds:.3f} s"


def main():
    """Run all benchmarks and display results."""
    sizes = [100, 1000, 5000, 10000]
    
    print("=" * 70)
    print("Data Structures Performance Benchmark")
    print("=" * 70)
    print()
    
    for size in sizes:
        print(f"Input size: {size:,}")
        print("-" * 70)
        
        # Stack
        print("Stack:")
        results = benchmark_stack(size)
        for op, t in results.items():
            print(f"  {op:12s}: {format_time(t):>12s}")
        print()
        
        # Queue
        print("Queue:")
        results = benchmark_queue(size)
        for op, t in results.items():
            print(f"  {op:12s}: {format_time(t):>12s}")
        print()
        
        # LinkedList
        print("LinkedList:")
        results = benchmark_linked_list(size)
        for op, t in results.items():
            print(f"  {op:12s}: {format_time(t):>12s}")
        print()
        
        # BinaryTree
        print("BinaryTree:")
        results = benchmark_binary_tree(size)
        for op, t in results.items():
            print(f"  {op:12s}: {format_time(t):>12s}")
        print()
        print("=" * 70)
        print()


if __name__ == "__main__":
    main()
