### DS 5

Internal representation of some data types:

| Data Type | Number of bytes | Internal Representation |
|-----------|-----------------|-------------------------|
| long      | 8               | 2’s complement          |
| double    | 8               | IEEE 754 (exp, mantissa)|
| boolean   | 1               | System dependent        |
---

Below is a method that, given a 2D integer array, $A$, returns the median.

```java 
public static double median(int[][] A) {
    int totalElements = 0;
    for (int row = 0; row < A.length; row++) {
        totalElements += A[row].length;
    }

    int[] flatArray = new int[totalElements];
    int index = 0;
    for (int row = 0; row < A.length; row++) {
        for (int col = 0; col < A[row].length; col++) {
            flatArray[index++] = A[row][col];
        }
    }

    Arrays.sort(flatArray);

    if (totalElements % 2 == 1) {
        return flatArray[totalElements / 2];
    } else {
        int mid1 = flatArray[(totalElements / 2) - 1];
        int mid2 = flatArray[totalElements / 2];
        return (mid1 + mid2) / 2.0;
    }
}
```
---

Below is a paint method that draws concentric ellipses separated by 20 pixels based on current width and height of the visible screen:

```java
public void paint(Graphics g) {
    int ww = (int) this.getWidth();
    int wh = (int) this.getHeight();
    int x = 0;
    int y = 40;
    int w = ww;
    int h = wh - 40;
    while (w > 40 && h > 40) {
        g.drawOval(x, y, w, h);
        x = x + 20;
        y = y + 20;
        w = w - 40;
        h = h - 40;
    }
}
```
---
Below is a method called $set2DArray$ that creates a 2D array with the same number of rows and columns as the input argument and sets the array elements to:

B[i][j] = 1 for all elements above the diagonal
B[i][j] = 0 for all elements on the diagonal
B[i][j] = -1 for all elements below the diagonal

Returns the created 2D array.

```java
public static int[][] set2DArray(int n) {
    int[][] b = new int[n][n];
    for (int row = 0; row < b.length; row++) {
        for (int col = 0; col < b[row].length; col++) {
            if (row < col)
                b[row][col] = 1;
            else if (row == col)
                b[row][col] = 0;
            else
                b[row][col] = -1;
        }
    }
    return b;
}
```
---

Below is a method to calculate the $nth$ Fibonacci number in the Fibonacci sequence. It assumes that the first 1 is fibonacci(1):

S = 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + ...

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
Recursive approach:
```java
public int fib(int n)
{
	if (n == 1 || n == 2)
		return 1;
	else
		return (fib(n-1) + fib(n-2));
}
```
---
Below is a method $normalized$ that receives a 2D integer array $A[N][N]$ and returns a 2D array $B[N][N]$ of integers that is created using the following formulas:

B[i][j] = A[i][j] - integer average of neighbors of A[i][j] (cells immediately next to A[i][j] including A[i][j]) 

B[i][j] = 0 for all border cells

```java
public static int[][] normalized(int[][] A) {
    int n = A.length;
    int[][] B = new int[n][n];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || j == 0 || i == n - 1 || j == n - 1) {
                B[i][j] = 0;
            } else {
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
---

Below is a method, $sumRow$, that receives a 2D array of integers, $A$, and returns the sum of each row of the array stored in a 1D array.
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
---

Below is a class $3DArray$ that contains:

A three dimensional array of integers.

An integer to represent the first dimension (rows).

An integer to represent the second dimension (columns)

An integer to represent the third dimension (depth)

A default constructor that creates a 3D array with 10 rows, 10 columns and 10 depth.

Constructor that receives the three dimensions, low and high and creates the array and initializes the array with random values between low and high.

Class also has methods to calculate and return minimum, average and maximum of the elements stored in the array 

```java
import java.util.Random;

public class 3DArray {
    private int[][][] array;
    private int rows;
    private int columns;
    private int depth;

    public 3DArray() {
        this(10, 10, 10, 0, 100);
    }

    public 3DArray(int rows, int columns, int depth, int low, int high) {
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
        int sum = 0;
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
---
Consider a text file containing 1000 integer numbers between 1,000,000 and 2,000,000.

What is the size of the text file in bytes? Why?

The size of the text file will be approximately 8000 bytes.
Each integer number can have up to 7 digits (from 1,000,000 to 2,000,000), plus a newline character (or space) to separate the numbers. Therefore, each number can take up to 8 bytes (7 for the digits and 1 for the separator). For 1000 integers, the total size would be approximately 1000 * 8 = 8000 bytes.

What size will the file have if you copy it to a binary file of integers? Why?

The size of the binary file will be 4000 bytes, because each integer in Java is stored in 4 bytes. Since there are 1000 integers, the total size will be 1000 * 4 = 4000 bytes.

Is a binary file's I/O faster or slower than a text file's? Why?

Faster. Binary file I/O is generally faster because it involves reading and writing raw bytes directly, without the need for conversion to and from text format. This reduces processing overhead and results in quicker data access.

---
Package vs Import in Java:
A package in Java is a namespace that organizes a set of related classes and interfaces. It helps to avoid name conflicts and to control access to classes. For example, `java.util` is a package that contains utility classes like `ArrayList` and `HashMap`.

An import statement allows you to use classes from other packages without needing to specify their full package name each time. For example, `import java.util.ArrayList;` lets you use `ArrayList` directly instead of `java.util.ArrayList`.

---
Below is a class hierarchy for vehicles, which includes cars and trucks. It identifies data members and methods (abstract and concrete) for each class in the hierarchy.

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

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }
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
---
What is an abstract method?

An abstract method is a method that is declared without an implementation. It only has a method signature and must be implemented by subclasses.

Why would you use an abstract method?

To enforce that subclasses provide specific implementations for the method, ensuring a consistent interface across different subclasses.

What is an abstract class?

An abstract class is a class that cannot be instantiated on its own and may contain abstract methods that must be implemented by subclasses.

Why would you use an abstract class?

To provide a common base class with shared code and to enforce a contract for subclasses through abstract methods.

What is an interface?

An interface is a reference type in Java that defines a contract of methods that implementing classes must provide. It can contain abstract methods (without implementation) and default methods (with implementation).

Why would you use an interface?

To define a contract that multiple classes can implement, allowing for polymorphism and decoupling of code.

What is a checked exception?

A checked exception is an exception that is checked at compile-time. The Java compiler requires that methods that can throw checked exceptions either handle them with a try-catch block or declare them in the method signature using the throws keyword.

What is an unchecked exception?

An unchecked exception is an exception that is not checked at compile-time. These are usually runtime exceptions that indicate programming errors, such as logic mistakes or improper use of an API.

What can you do about checked and unchecked exceptions?

For checked exceptions, you must either catch them using a try-catch block or declare them in the method signature with the throws keyword. For unchecked exceptions, you can choose to handle them, but it is not mandatory.

---