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
- `ds_1.md` .. `ds_6.md`: Existing notes/reference materials
- `.github/workflows/`: CI and Release automation
- `scripts/verify.ps1`: PowerShell script to install and test

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

## Notes
- This repo is intentionally scoped to the `ds_examples` folder; the root workspace is not pushed to GitHub.
- After pushing to GitHub, the local folder name will be renamed to `ds_examples_gh` per project requirements. The GitHub repo will not include `_gh`.
