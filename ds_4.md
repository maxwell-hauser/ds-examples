# Java OOP Concepts and Advanced Topics

## Core OOP Concepts

### What is a Java Class?

A Java class is a blueprint from which individual objects are created. A class can contain:
- **Fields** (data members): Variables that hold the state
- **Methods**: Functions that define behavior
- **Constructors**: Special methods for object initialization

### What is a Java Object?

An object is an instance of a class. It contains:
- **State**: Attributes or data members with specific values
- **Behavior**: Methods or functions that operate on the object's data

Objects are created using constructors and the `new` keyword.

### What is Java Inheritance?

Inheritance is a mechanism where one class (subclass/child) inherits fields and methods from another class (superclass/parent). Benefits include:
- Code reusability
- Hierarchical class relationships
- Polymorphic behavior

### What is Polymorphism?

Polymorphism allows a single function or method to operate in different ways based on the object or parameters. Types include:
- **Runtime Polymorphism**: Method overriding
- **Compile-time Polymorphism**: Method overloading

## Exercise 1: Counting Digit Occurrences

Given a 1D array of integers with values between 0-9, return the number of occurrences of each digit.

```java
public static int[] numberOccurrences(int[] a) {
    int[] b = new int[10];
    
    for (int i = 0; i < a.length; i++) {
        if (a[i] >= 0 && a[i] <= 9) {
            b[a[i]]++;
        }
    }
    
    return b;
}
```

**Improved version using simplified logic:**

```java
public static int[] numberOccurrences(int[] a) {
    int[] count = new int[10];
    
    for (int value : a) {
        if (value >= 0 && value <= 9) {
            count[value]++;
        }
    }
    
    return count;
}
```

## Exercise 2: Initialize 2D Array with Pattern

Create and return a 2D array with N rows and N columns initialized as:
- `A[i][j] = 1` if both i and j are even
- `A[i][j] = -1` if both i and j are odd
- `A[i][j] = 0` otherwise

```java
public static int[][] set2DArray(int n) {
    int[][] a = new int[n][n];
    
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row % 2 == 0 && col % 2 == 0) {
                a[row][col] = 1;
            } else if (row % 2 != 0 && col % 2 != 0) {
                a[row][col] = -1;
            } else {
                a[row][col] = 0;
            }
        }
    }
    
    return a;
}
```

## Exercise 3: Graphics - Nested Rectangles

Draw a shape based on current window dimensions, leaving 20 pixels margin and accounting for 40-pixel title bar.

```java
public void paint(Graphics g) {
    int ww = getWidth();
    int wh = getHeight();
    
    // Draw outer rectangle
    g.drawRect(20, 60, ww - 40, wh - 80);
    
    // Draw diagonal lines
    int x1 = 20;
    int y1 = 60 + (wh - 80);
    int x2 = ww - 20;
    int y2 = 60;
    
    g.drawLine(x1, y1, x2, y2);
}
```

## Advanced OOP Concepts

### Method Overloading

Two or more methods share the same name but have different parameter lists (different type, number, or both).

```java
public int add(int a, int b) {
    return a + b;
}

public double add(double a, double b) {
    return a + b;
}

public int add(int a, int b, int c) {
    return a + b + c;
}
```

### Method Overriding

A subclass provides a specific implementation of a method already defined in its superclass. The method must have:
- Same name
- Same return type
- Same parameters

```java
class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}
```

### Abstract Methods

An abstract method is declared without an implementation (no method body) in an abstract class.

```java
public abstract class Shape {
    public abstract double getArea();
    public abstract double getPerimeter();
}
```

**Why use abstract methods?**
- Force subclasses to provide specific implementations
- Define a contract that subclasses must follow
- Enable polymorphic behavior

### Abstract Classes

An abstract class cannot be instantiated and may contain abstract methods that must be implemented by subclasses.

```java
public abstract class Vehicle {
    protected String make;
    protected String model;
    
    public abstract void startEngine();
    
    public void displayInfo() {
        System.out.println(make + " " + model);
    }
}
```

**Why use abstract classes?**
- Provide a common base with shared code
- Enforce implementation contracts through abstract methods
- Share state and behavior among related classes

## Package Access Modifiers

### Example: Cross-Package Inheritance

```java
// Package S
public class A {
    private int[] x;
    protected int y;
    String c;  // Default (package-private)
}

public class B extends A {
    private int d;
    boolean f;
    protected float[] g;
}
```

```java
// Package T
public class C extends A {
    private int p;
    public String t;
}

public class D extends B {
    private int h;
    boolean r;
}
```

### Object Structure: Class B

```java
B term = new B();
```

| Variable | Type    | Bytes              | Content |
|----------|---------|--------------------| --------|
| d        | int     | 4                  | 0       |
| f        | boolean | 1                  | false   |
| g        | float[] | 4 (reference)      | null    |
| x        | int[]   | 4 (reference)      | null    |
| y        | int     | 4                  | 0       |
| c        | String  | 4 (reference)      | null    |

### Access Rules

**Acceptable references:**
- Class B can access protected `y` and default `c` from class A (same package)
- Class D can access protected `y` from class A (through inheritance)
- Class D can access protected `g` from class B (through inheritance)

**Unacceptable references:**
- Class C cannot access private `x` from class A
- Class C cannot access default member `c` from class A (different package)
- Class D cannot access private `d` from class B

## Key Principles

### Encapsulation
- Private data members
- Public accessors/mutators
- Protected access for inheritance

### Inheritance Hierarchy
- `extends` keyword for class inheritance
- `super` to access parent class members
- Constructor chaining with `super()`

### Polymorphism
- Method overriding for runtime polymorphism
- Abstract classes and interfaces for contracts
- Type substitution (subclass objects as superclass references)
