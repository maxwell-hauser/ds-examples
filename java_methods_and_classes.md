# Java Methods and Classes

## Exercise 1: Series Summation

Develop a method `sum` that, given an integer `n`, returns the value of the following series:

$$S = 1 + \frac{1}{2} + \frac{1}{4} + \ldots + \frac{1}{2^n}$$

```java
public static double sum(int n) {
    double number = 1.0;
    
    if (n == 0) {
        return 0;
    }
    
    if (n == 1) {
        return 1;
    }
    
    for (int i = 1; i < n; i++) {
        number += (1.0 / Math.pow(2, i));
    }
    
    return number;
}
```

## Exercise 2: Counting Divisible Numbers

Develop a method called `count` that, given two integers `k1` and `k2`, returns the number of integers between `k1` and `k2` that are divisible by either 7 or 11 but not both.

```java
public static int count(int k1, int k2) {
    int counter = 0;
    
    for (int i = k1 + 1; i < k2; i++) {
        // Skip numbers divisible by both 7 and 11
        if (i % 7 == 0 && i % 11 == 0) {
            continue;
        }
        
        // Count numbers divisible by 7 or 11 (but not both)
        if (i % 7 == 0 || i % 11 == 0) {
            counter++;
        }
    }
    
    return counter;
}
```

## Exercise 3: Maximum Value in 2D Array

Develop a method called `maxArray` that, given a two-dimensional array `t` of integers, returns the maximum of the elements stored in the array.

```java
public static int maxArray(int[][] t) {
    int maxValue = Integer.MIN_VALUE;
    
    for (int row = 0; row < t.length; row++) {
        for (int col = 0; col < t[row].length; col++) {
            if (t[row][col] > maxValue) {
                maxValue = t[row][col];
            }
        }
    }
    
    return maxValue;
}
```

## Exercise 4: Faculty Summer Pay Calculator

Develop a method `summerPay` that, given the rank of a teaching faculty (a String) and the number of credit hours taught during summer (an integer), returns the total summer earnings for that faculty.

### Wages for 1 Credit Hour (Year 2020)

| Rank                | Rate per Credit Hour |
|---------------------|----------------------|
| Professor           | $2,146               |
| Associate Professor | $1,977               |
| Assistant Professor | $1,825               |
| Instructor          | $1,672               |

```java
public static int summerPay(String rank, int creditHours) {
    int pay = 0;
    
    switch (rank) {
        case "Professor":
            pay = 2146 * creditHours;
            break;
        case "Associate Professor":
            pay = 1977 * creditHours;
            break;
        case "Assistant Professor":
            pay = 1825 * creditHours;
            break;
        case "Instructor":
            pay = 1672 * creditHours;
            break;
        default:
            pay = -1;  // Invalid rank
    }
    
    return pay;
}
```

## Exercise 5: Sphere Class Design

Design a class named `Sphere` to represent a geometric sphere defined by the coordinates of its center `(xc, yc)` and its radius `r`.

**Formulas:**
- Surface Area = $4\pi r^2$
- Volume = $\frac{4}{3}\pi r^3$

### UML Diagram

```
+-----------------+
|     Sphere      |
+-----------------+
| - xc: int       |
| - yc: int       |
| - r: int        |
+-----------------+
| + Sphere()      |
| + Sphere(int xc, int yc, int r) |
| + getX(): int   |
| + getY(): int   |
| + getR(): int   |
| + getSurface(): double |
| + getVolume(): double  |
+-----------------+
```

### Java Implementation

```java
public class Sphere {
    // Data members
    private int xc, yc, r;
    
    // No-argument constructor
    public Sphere() {
        xc = 0;
        yc = 0;
        r = 10;
    }
    
    // Argument constructor
    public Sphere(int xc1, int yc1, int r1) {
        xc = xc1;
        yc = yc1;
        r = r1;
    }
    
    // Accessors
    public int getR() {
        return r;
    }
    
    public int getX() {
        return xc;
    }
    
    public int getY() {
        return yc;
    }
    
    // Other methods
    public double getSurface() {
        return 4 * Math.PI * r * r;
    }
    
    public double getVolume() {
        return (4.0 / 3.0) * Math.PI * r * r * r;
    }
}
```

## Key Concepts

### Method Design Principles

1. **Clear Purpose**: Each method should have a single, well-defined purpose
2. **Appropriate Return Types**: Choose return types that accurately represent the result
3. **Meaningful Parameters**: Use descriptive parameter names and appropriate data types
4. **Error Handling**: Consider edge cases and invalid inputs

### Class Design Best Practices

1. **Encapsulation**: Use private data members with public accessors
2. **Constructors**: Provide both no-argument and parameterized constructors
3. **Documentation**: Include clear comments explaining purpose and formulas
4. **Validation**: Consider validating input parameters in constructors and methods
