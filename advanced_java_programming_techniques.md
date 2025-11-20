# Advanced Java Programming Techniques

## Data Type Internal Representation

| Data Type | Bytes | Internal Representation                        |
|-----------|-------|------------------------------------------------|
| long      | 8     | 2's complement                                 |
| double    | 8     | IEEE 754 (exponent + mantissa)                 |
| boolean   | 1     | System dependent (typically 1 byte in memory)  |

## Exercise 1: 2D Array Median Calculation

Calculate the median of all elements in a 2D integer array.

```java
public static double median(int[][] A) {
    // Count total elements
    int totalElements = 0;
    for (int row = 0; row < A.length; row++) {
        totalElements += A[row].length;
    }

    // Flatten 2D array into 1D array
    int[] flatArray = new int[totalElements];
    int index = 0;
    for (int row = 0; row < A.length; row++) {
        for (int col = 0; col < A[row].length; col++) {
            flatArray[index++] = A[row][col];
        }
    }

    // Sort the flattened array
    Arrays.sort(flatArray);

    // Calculate median
    if (totalElements % 2 == 1) {
        // Odd number of elements: return middle element
        return flatArray[totalElements / 2];
    } else {
        // Even number of elements: return average of two middle elements
        int mid1 = flatArray[(totalElements / 2) - 1];
        int mid2 = flatArray[totalElements / 2];
        return (mid1 + mid2) / 2.0;
    }
}
```

## Exercise 2: Graphics - Concentric Ellipses

Draw concentric ellipses separated by 20 pixels based on current window dimensions.

```java
public void paint(Graphics g) {
    int ww = getWidth();
    int wh = getHeight();
    int x = 0;
    int y = 40;  // Account for title bar
    int w = ww;
    int h = wh - 40;
    
    while (w > 40 && h > 40) {
        g.drawOval(x, y, w, h);
        x += 20;
        y += 20;
        w -= 40;
        h -= 40;
    }
}
```

## Exercise 3: Diagonal Pattern in 2D Array

Create a 2D array with N×N dimensions and initialize as:
- `B[i][j] = 1` for elements above the diagonal (i < j)
- `B[i][j] = 0` for elements on the diagonal (i == j)
- `B[i][j] = -1` for elements below the diagonal (i > j)

```java
public static int[][] set2DArray(int n) {
    int[][] b = new int[n][n];
    
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row < col) {
                b[row][col] = 1;
            } else if (row == col) {
                b[row][col] = 0;
            } else {
                b[row][col] = -1;
            }
        }
    }
    
    return b;
}
```

## Exercise 4: Fibonacci Sequence

Calculate the nth Fibonacci number in the sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...

### Iterative Approach

```java
public static int fibonacci(int n) {
    if (n <= 0) {
        throw new IllegalArgumentException("Input must be a positive integer.");
    }
    
    if (n == 1 || n == 2) {
        return 1;
    }
    
    int a = 1, b = 1, c = 0;
    for (int i = 3; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    
    return c;
}
```

### Recursive Approach

```java
public static int fibonacci(int n) {
    if (n <= 0) {
        throw new IllegalArgumentException("Input must be a positive integer.");
    }
    
    if (n == 1 || n == 2) {
        return 1;
    }
    
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

**Time Complexity:**
- Iterative: O(n)
- Recursive (naive): O(2ⁿ)

## Exercise 5: Normalized 2D Array

Create a normalized version of a 2D array where each element equals the original value minus the integer average of its neighbors (including itself). Border cells are set to 0.

```java
public static int[][] normalized(int[][] A) {
    int n = A.length;
    int[][] B = new int[n][n];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // Set border cells to 0
            if (i == 0 || j == 0 || i == n - 1 || j == n - 1) {
                B[i][j] = 0;
            } else {
                // Calculate average of neighbors (including current cell)
                int sum = 0;
                int count = 0;
                
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        sum += A[i + di][j + dj];
                        count++;
                    }
                }
                
                int average = sum / count;
                B[i][j] = A[i][j] - average;
            }
        }
    }
    
    return B;
}
```

## Exercise 6: Row Sum Calculator

Calculate the sum of each row in a 2D array and return as a 1D array.

```java
public static int[] sumRow(int[][] A) {
    int[] s = new int[A.length];
    
    for (int row = 0; row < A.length; row++) {
        int sum = 0;
        for (int col = 0; col < A[row].length; col++) {
            sum += A[row][col];
        }
        s[row] = sum;
    }
    
    return s;
}
```

## Exercise 7: 3D Array Class

A class to manage a 3D array of integers with initialization and statistical methods.

```java
import java.util.Random;

public class Array3D {
    private int[][][] array;
    private int rows;
    private int columns;
    private int depth;

    // Default constructor: 10×10×10 array with random values 0-100
    public Array3D() {
        this(10, 10, 10, 0, 100);
    }

    // Parameterized constructor
    public Array3D(int rows, int columns, int depth, int low, int high) {
        this.rows = rows;
        this.columns = columns;
        this.depth = depth;
        array = new int[rows][columns][depth];
        
        Random rand = new Random();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                for (int k = 0; k < depth; k++) {
                    array[i][j][k] = rand.nextInt(high - low + 1) + low;
                }
            }
        }
    }

    public int getMin() {
        int min = array[0][0][0];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                for (int k = 0; k < depth; k++) {
                    if (array[i][j][k] < min) {
                        min = array[i][j][k];
                    }
                }
            }
        }
        
        return min;
    }

    public int getMax() {
        int max = array[0][0][0];
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                for (int k = 0; k < depth; k++) {
                    if (array[i][j][k] > max) {
                        max = array[i][j][k];
                    }
                }
            }
        }
        
        return max;
    }

    public double getAverage() {
        long sum = 0;
        int count = rows * columns * depth;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                for (int k = 0; k < depth; k++) {
                    sum += array[i][j][k];
                }
            }
        }
        
        return (double) sum / count;
    }
}
```

## File I/O Concepts

### Text File vs Binary File Size

**Scenario:** 1000 integers between 1,000,000 and 2,000,000

**Text File Size:**
- Each integer: up to 7 digits + separator (space/newline) = ~8 bytes
- Total: 1000 × 8 = **~8,000 bytes**

**Binary File Size:**
- Each integer: 4 bytes (Java `int`)
- Total: 1000 × 4 = **4,000 bytes**

**Performance:**
Binary file I/O is **faster** because:
- No conversion between text and binary representation
- Direct byte-level reading/writing
- Less processing overhead

## Java Packages and Imports

### Package

A namespace that organizes related classes and interfaces:
- Avoids name conflicts
- Controls access
- Example: `java.util`, `java.io`

### Import

Allows using classes without full package qualification:
- `import java.util.ArrayList;` → use `ArrayList` directly
- `import java.util.*;` → import all classes from package

## Abstract Class Hierarchy Example

```java
abstract class Vehicle {
    protected String make;
    protected String model;
    protected int year;

    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public abstract void startEngine();
    public abstract void stopEngine();

    public String getMake() { return make; }
    public String getModel() { return model; }
    public int getYear() { return year; }
}

class Car extends Vehicle {
    private int numberOfDoors;

    public Car(String make, String model, int year, int numberOfDoors) {
        super(make, model, year);
        this.numberOfDoors = numberOfDoors;
    }

    @Override
    public void startEngine() {
        System.out.println("Car engine started.");
    }

    @Override
    public void stopEngine() {
        System.out.println("Car engine stopped.");
    }

    public int getNumberOfDoors() {
        return numberOfDoors;
    }
}

class Truck extends Vehicle {
    private double loadCapacity;

    public Truck(String make, String model, int year, double loadCapacity) {
        super(make, model, year);
        this.loadCapacity = loadCapacity;
    }

    @Override
    public void startEngine() {
        System.out.println("Truck engine started.");
    }

    @Override
    public void stopEngine() {
        System.out.println("Truck engine stopped.");
    }

    public double getLoadCapacity() {
        return loadCapacity;
    }
}
```

## Exception Handling

### Checked Exceptions

Checked at compile-time; must be handled or declared:
- `IOException`
- `SQLException`
- `ClassNotFoundException`

```java
public void readFile(String path) throws IOException {
    // Method must declare exception or handle with try-catch
}
```

### Unchecked Exceptions

Not checked at compile-time (runtime exceptions):
- `NullPointerException`
- `ArrayIndexOutOfBoundsException`
- `ArithmeticException`

```java
public int divide(int a, int b) {
    return a / b;  // May throw ArithmeticException
}
```

### Handling Strategies

```java
// Try-catch block
try {
    riskyOperation();
} catch (IOException e) {
    System.err.println("Error: " + e.getMessage());
} finally {
    cleanup();
}

// Declare with throws
public void method() throws IOException, SQLException {
    // May throw these exceptions
}
```
