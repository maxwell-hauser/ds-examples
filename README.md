# Data Structures Examples (Python)

Data Structures Examples is a curated set of concise, runnable Python implementations and notes to learn fundamental data structures (stacks, queues, linked lists, and trees). It pairs readable code with step-by-step tests and markdown guides to reinforce concepts. Ideal for self-study, teaching, and quick refreshers.

## Features
- Minimal, well-documented Python implementations
- Pytest tests for fast feedback and learning-by-doing
- Simple CLI demo to see structures in action
- GitHub Actions CI + Release workflow

## Repository Layout
- `src/ds_examples/`: Python package with implementations and a CLI demo
- `tests/`: Pytest-based tests for core structures
- `scripts/`: Utility scripts including `verify.ps1` (setup/test) and `benchmark.py` (performance testing)
- `.github/workflows/`: CI and Release automation
- Reference materials:
  - `java_fundamentals_and_basic_programming.md`: Java basics, JOptionPane, hardware, errors
  - `java_methods_and_classes.md`: Method design, class implementation, Sphere example
  - `object_oriented_programming.md`: Inheritance, encapsulation, Student class
  - `oop_concepts_and_advanced_topics.md`: Polymorphism, abstract classes, access modifiers
  - `advanced_java_programming_techniques.md`: Arrays, recursion, file I/O, exceptions
  - `data_structures_exercises_and_analysis.md`: Complexity analysis, postfix evaluation, tree structures

## Quick Start (Windows PowerShell)
```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -U pip
pip install -e .
pip install pytest
pytest -q

# Run the CLI demo
python -m ds_examples.cli
```

## CLI Demo
```powershell
python -m ds_examples.cli
```
Outputs example usage of Stack, Queue, LinkedList, and BinaryTree.

## Use Cases
- Teaching/learning core data structures with runnable examples
- Quick reference for interviews or coding exercises
- Lightweight starting point for experimenting with ADTs

## Test Cases
Tests live under `tests/`. Example checks include:
- LIFO behavior for `Stack`
- FIFO behavior for `Queue`
- Insert/search/remove for `LinkedList`
- Insert/find/traversals for `BinaryTree`

Run all tests:
```powershell
pytest -q
```

## CI/CD and Releases
- CI runs on pushes/PRs to validate code and tests across Python versions
- Tagging a version like `v0.1.0` triggers the Release workflow, generating GitHub release notes

## Complexity Reference

### Stack

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| push      | O(1)            | O(1)             |
| pop       | O(1)            | O(1)             |
| peek      | O(1)            | O(1)             |
| is_empty  | O(1)            | O(1)             |
| size      | O(1)            | O(1)             |

### Queue

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| enqueue   | O(1)            | O(1)             |
| dequeue   | O(1)            | O(1)             |
| peek      | O(1)            | O(1)             |
| is_empty  | O(1)            | O(1)             |
| size      | O(1)            | O(1)             |

### LinkedList

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| append    | O(n)            | O(1)             |
| find      | O(n)            | O(1)             |
| remove    | O(n)            | O(1)             |
| to_list   | O(n)            | O(n)             |

### BinaryTree (BST)

| Operation    | Average Case | Worst Case | Space Complexity |
|--------------|--------------|------------|------------------|
| insert       | O(log n)     | O(n)       | O(1)             |
| find         | O(log n)     | O(n)       | O(1)             |
| inorder      | O(n)         | O(n)       | O(n)             |
| preorder     | O(n)         | O(n)       | O(n)             |
| postorder    | O(n)         | O(n)       | O(n)             |

## Performance Benchmarking

Run the included benchmarking script to measure performance on your system:

```powershell
python scripts/benchmark.py
```

This will test operations across multiple input sizes and display timing results.

## Authorship
Authored 20 November, 2025 by Maxwell Hauser

## License
This project is licensed under the MIT License. See `LICENSE`.

## Project Structure Notes
- This repository contains only the data structures examples project; the parent workspace is not included.
- The local folder is named `py_ds_examples_gh` to distinguish it from the workspace root, while the GitHub repository is named `ds-examples`.
