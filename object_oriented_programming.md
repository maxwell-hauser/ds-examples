# Object-Oriented Programming in Java

## Exercise 1: Cylinder Class Structure

Consider the following class definition:

```java
public class Cylinder {
    private String color;
    private int xCenterBase;
    private int yCenterBase;
    private int radius;
    private int height;

    public Cylinder(String c, int x, int y, int r, int h) {
        color = c;
        xCenterBase = x;
        yCenterBase = y;
        radius = r;
        height = h;
    }
}
```

### Object Creation

What is the structure and content of object `c` created as follows:

```java
Cylinder c = new Cylinder("Blue", 100, 100, 200, 200);
```

| Variable Name | Type     | Size (Bytes)              | Content |
|---------------|----------|---------------------------|---------|
| color         | String   | 8 (reference) + 2*length  | "Blue"  |
| xCenterBase   | int      | 4                         | 100     |
| yCenterBase   | int      | 4                         | 100     |
| radius        | int      | 4                         | 200     |
| height        | int      | 4                         | 200     |

## Exercise 2: Array Search Method

Method `searchArray` takes a 1D array of integers `A` and an integer key `k`, returning an array where:
- Index 0: Number of elements smaller than `k`
- Index 1: Number of elements larger than `k`

```java
public static int[] searchArray(int[] s, int k) {
    int[] result = new int[2];
    int countSmaller = 0;
    int countLarger = 0;

    for (int i = 0; i < s.length; i++) {
        if (s[i] < k) {
            countSmaller++;
        }
        if (s[i] > k) {
            countLarger++;
        }
    }
    
    result[0] = countSmaller;
    result[1] = countLarger;
    return result;
}
```

## Exercise 3: 2D Array Equality Check

Method `equal` takes two 2D int arrays `a` and `b`, returning `true` if all corresponding elements are equal, `false` otherwise.

```java
public static boolean equal(int[][] a, int[][] b) {
    // Check if dimensions match
    if (a.length != b.length) {
        return false;
    }
    
    boolean isEqual = true;
    
    for (int row = 0; row < a.length; row++) {
        // Check row lengths
        if (a[row].length != b[row].length) {
            return false;
        }
        
        for (int col = 0; col < a[row].length; col++) {
            if (a[row][col] != b[row][col]) {
                isEqual = false;
            }
        }
    }
    
    return isEqual;
}
```

## Exercise 4: Graphics - Centered Circle

Paint method that draws a circle in the middle of the screen, leaving 20 pixels from borders and accounting for 40-pixel title/menu bar.

```java
public void paint(Graphics g) {
    int w = getWidth();
    int h = getHeight();
    
    g.setColor(Color.BLUE);
    
    // Calculate centered circle position and size
    int x = 20;
    int y = 60;  // 40 for title bar + 20 for margin
    int diameter = Math.min(w - 40, h - 80);
    
    g.fillOval(x, y, diameter, diameter);
}
```

## Exercise 5: Student Class

Track student personal information and enrollment status.

### UML Diagram

```
+------------------------+
|        Student         |
+------------------------+
| - firstName: String    |
| - lastName: String     |
| - address: String      |
| - telephone: String    |
| - major: String        |
| - minor: String        |
| - credits: int         |
| - gpa: double          |
+------------------------+
| + Student()            |
| + Student(fn, ln, a, t, ma, mi, c, g) |
| + getFirst(): String   |
| + getLast(): String    |
| + getAddress(): String |
| + getTelephone(): String |
| + getMajor(): String   |
| + getMinor(): String   |
| + getCredits(): int    |
| + getGPA(): double     |
+------------------------+
```

### Implementation

```java
public class Student {    
    // Data Members
    private String firstName;
    private String lastName;
    private String address;
    private String telephone;
    private String major;
    private String minor;
    private int credits;
    private double gpa;

    // No-argument constructor
    public Student() {
        firstName = "John";
        lastName = "Smith";
        address = "123 Filbert St.";
        telephone = "(555) 123-4567";
        major = "Computer Science";
        minor = "None";
        credits = 80;
        gpa = 3.5;
    }
    
    // Argument constructor
    public Student(String fn, String ln, String a, String t, 
                   String ma, String mi, int c, double g) {
        firstName = fn;
        lastName = ln;
        address = a;
        telephone = t;
        major = ma;
        minor = mi;
        credits = c;
        gpa = g;
    }
    
    // Accessors
    public String getFirst() { return firstName; }
    public String getLast() { return lastName; }
    public String getAddress() { return address; }
    public String getTelephone() { return telephone; }
    public String getMajor() { return major; }
    public String getMinor() { return minor; }
    public int getCredits() { return credits; }
    public double getGPA() { return gpa; }
}
```

## Exercise 6: Inheritance Example

Given class definitions:

```java
public class A {
    private int[] a;
    public double b;
    public String c;
}

public class XYZ extends A {
    private int d;
    private boolean f;
    String g;
}
```

### Object Structure with Default Constructor

```java
XYZ p = new XYZ();
```

| Variable | Type     | Size (Bytes)       | Content      |
|----------|----------|-------------------|--------------|
| d        | int      | 4                 | 0            |
| f        | boolean  | 1                 | false        |
| g        | String   | 4 (reference)     | null         |
| a        | int[]    | 4 (reference)     | null         |
| b        | double   | 8                 | 0.0          |
| c        | String   | 4 (reference)     | null         |

### Access Rights

All references in class XYZ are acceptable because:
- Class XYZ inherits all non-private members from class A
- Private member `a` is inherited but not directly accessible in XYZ methods
- Public members `b` and `c` are fully accessible

## Key Concepts

### Inheritance
- Subclasses inherit non-private members from superclasses
- Private members are inherited but not directly accessible
- Use constructors to properly initialize inherited members

### Encapsulation
- Keep data members private
- Provide public accessor methods
- Protect object state from invalid modifications

### Memory Layout
- Objects contain all instance variables from their class and superclasses
- References (objects, arrays) typically use 4 or 8 bytes depending on JVM
- Primitive types have fixed sizes
