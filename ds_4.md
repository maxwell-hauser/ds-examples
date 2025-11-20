### Data Structures 4
---			   

What is a Java Class?

A Java class is a blueprint from which individual objects are created. A class can contain fields (data members) and methods to define the behavior of the objects created from the class.

What is a Java Object?

An object is an instance of a class. It contains state (attributes or data members) and behavior (methods or functions) defined by its class. Objects are created using constructors.

What is Java inheritance?

Inheritance is a mechanism in Java where one class (the subclass or child class) can inherit fields and methods from another class (the superclass or parent class). This promotes code reusability and establishes a hierarchical relationship between classes.

What is Polymorphism (in the context of Java programming language)?

Polymorphism is the ability of a single function or method to operate in different ways based on the object that it is acting upon. In Java, polymorphism is primarily achieved through method overriding (runtime polymorphism) and method overloading (compile-time polymorphism). This allows methods to behave differently based on the object type or the parameters passed to them.

---

Below is a method that, given a one-dimensional array of integers with values between zero and nine, $A$, returns the number of occurrences of each digit in the array.

The method creates an array of 10 elements, $B$, each holding the number of occurrences of a digit. B[0] holds the number of zeros in A.

```java
public static int[] numberOccurrences(int[] a) {
    int[] b = new int[10];
    for (int l = 0; l < a.length; l++) {
        switch (a[l]) {
            case 0:
                b[0] += 1;
                break;	
            case 1:
                b[1] += 1;
                break;
            case 2:
                b[2] += 1;
                break;
            case 3:
                b[3] += 1;
                break;
            case 4:
                b[4] += 1;
                break;
            case 5:
                b[5] += 1;
                break;
            case 6:
                b[6] += 1;
                break;
            case 7:
                b[7] += 1;
                break;
            case 8:
                b[8] += 1;
                break;
            case 9:
                b[9] += 1;
                break;
        }
    }
    return b;
}
```
---

Below is a method called set2DArray that, given an integer number, $N$, creates and returns a 2D array with $N$ rows and $N$ columns initialized as follows:

A[i][j] = 1 if i and j are both even

A[i][j] = -1 if i and j are both odd

A[i][j] = 0 otherwise

```java
public static int[][] set2DArray(int n) {
    int[][] a = new int[n][n];
    for (int row = 0; row < a.length; row++) {
        for (int col = 0; col < a[row].length; col++) {
            if (row % 2 == 0 && col % 2 == 0)
                a[row][col] = 1;
            
            else if (row % 2 != 0 && col % 2 != 0)
                a[row][col] = -1;
            
            else
                a[row][col] = 0;
        }
    }
    return a;
}
```
---

Below is a paint method that draws a shape based on the current width and height of the visible screen. Title bar is 40 pixels in height, leave 20 pixels between outer rectangle and frame borders. 

```java
public void paint(Graphics g) {
    int ww = (int) this.getWidth();
    int wh = (int) this.getHeight();

    g.drawRect (20, 60, ww-40, wh-80);
    g.drawLine(20, 30 + (wh-50), ww-700, 30 + (wh-810));
    g.drawLine(ww-700, 30 + (wh-810), 500, 30 + (wh-50));
    g.drawLine(500, 30 + (wh-50), (ww-680) * 2, 30 + (wh-810));
    g.drawLine((ww-680) * 2, 30 + (wh-810), 980, 30 + (wh-50));
}
```
---

What is method overloading?

When two methods share the same name but have different implementations based on different parameter lists (different type, number, or both of parameters).

What is method overriding?

When you write your own method to replace one already defined in the java library or in a superclass. The method in the subclass has the same name, return type, and parameters as the one in the superclass.

What is an abstract method?

An abstract method is a method that is declared without an implementation (without a body) in an abstract class. It serves as a placeholder for methods that must be implemented by subclasses.

Why would you use an abstract method?

To force the subclasses to provide an implementation for the method.

What is an abstract class?

An abstract class is a class that cannot be instantiated on its own and may contain abstract methods that must be implemented by subclasses.

Why would you use an abstract class?

To provide a common base class with shared code and to enforce a contract for subclasses through abstract methods.

---

Below are class definitions $A$ and $B$ within the same package $S$, and class definitions $C$ and $D$ within another package $T$.

```java
Package S
public class A {
    private int[] x;
    protected int y;
    String c;
}

public class B extends A {
    private int d;
    boolean f;
    protected float[] g;
}
```
```java
Package T
public class C extends A {
    private int p;
    public String t;
}

public class D extends B {
    private int h;
    boolean r;
}
```
What is the structure and content of object term created as follows using java default constructor:

```java
B term = new B ();
```
| Var Name | Type | Bytes | Content |
|----------|------|-------|---------|
| d        | int  | 4     | 0       |
| f        | boolean | 1  | false   |
| g        | float[] | 4x length of array | null |
| x        | int[] | 4x length of array | null |
| y        | int  | 4     | 0       |
| c        | String | 4x length of array | null |

What are the acceptable and unacceptable references made across all classes?

Acceptable references: 
- Class B can access protected member y and default member c from class A.
- Class D can access protected member y from class A and protected member g from class B.

Unacceptable references:
- Class C cannot access private member x from class A.
- Class D cannot access private member d from class B.
---

Below is the design and implementation of class $Point$. It represents a point on 2D Cartesian coordinate planes. $Point$ has two integer numbers as data members, no-arg and argument constructors, accessor methods, a method to calculate and return the distance of the point from the origin, and a method to determine and return the quadrant the point is located at as an integer (1 for quadrant I, 2 for quadrant II, etc.).

```java
public class Point
{
	private static int x, y, q;
	
	public Point()
	{
		x = 10;
		y = 10;
	}
	
	public Point(int x1, int y1)
	{
		x = x1;
		y = y1;
	}

	public int getX() {return x;}
	public void setX(int x1) {x = x1;}
	public int getY() {return y;}
	public void setY(int y1) {y = y1;}
			
	
	public double getDistance(int x1, int y1)
	{
		return Math.sqrt(Math.pow(x1 - 0, 2)
				 	   + Math.pow(y1 - 0, 2));
	}
	
	public int getQuadrant(int x1, int y1)
	{
		if (x1 > 0 && y1 > 0)
			q = 1;
		else if (x1 < 0 && y1 > 0)
			q = 2;
		else if (x1 < 0 && y1 < 0)
			q = 3;
		else (x1 > 0 && y1 < 0)
			q = 4;
		return q;
	}
}
```
---
Java supports text and binary files.

What is a file? A file is a way to store collections of data/information/numbers on a computer. They can be both read and written.

A text file is made of ASCII characters, and can be opened and edited with text editors. A binary file is made of bytes, and is not human-readable.

Given a text file with one million integers between 4,000,000,000 and 9,000,000,000, how many bytes of the disk will the file occupy?

Each integer in that range requires 8 bytes (since they exceed the range of a 4-byte integer). Therefore, for one million integers:
1,000,000 integers * 8 bytes/integer = 8,000,000 bytes.

---

Below is the design and implementation for a class hierarchy for two-dimensional shapes. All shapes have a color and name. Subclasses define their own specific data members. All subclasses implement the following methods:

getAttributes: obtains attributes of a shape by interacting with the user.

getPerimeter: calculates and returns the perimeter of the particular shape.

getArea: calculates and returns the area of the particular shape.

UMLs for TwoDShape class (Super Class) and subclasses Ellipse and Parallelogram:

```
TwoDShape
-color: String
-name: String
+TwoDShape(color: String, name: String)
+TwoDShape() 
+getColor(): String
+setColor(color: String): void
+getName(): String
+setName(name: String): void
+getAttributes(): void
+getPerimeter(): double
+getArea(): double
```
```
Parallelogram extends TwoDShape
+Parallelogram()
+Parallelogram(width: double, height: double)
+Parallelogram(width: double, height: double, color: String, name: String)
+getWidth(): double
+getHeight(): double
+getPerimeter(): double
+getArea(): double
```
```
Ellipse extends TwoDShape
+Ellipse()
+Ellipse(radius: double)
+getPerimeter(): double
+getArea(): double
+getRadius(): double
```