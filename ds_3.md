### Data Structures 3
---

Consider the following class definition:

```java
public class Cylinder {
    private String color;
    private int xCenterBase;
    private int yCenterBase;
	private int radius;
	private int height;

    public Cylinder(String c, int x, int y, int r, int h)
    {
        color = c;
        xCenterBase = x;
        yCenterBase = y;
        radius = r;
        height = h;
    }
}
```

What is the structure and content of object c created as follows:

```java
Cylinder c = new Cylinder("Blue", 100, 100, 200, 200);
```

| Var Name | Type | Size (B) | Content |
|-------------|----------|-----------|---------|
| color| String | 8 (reference) + 2*length | "Blue" | Blue |
| xCenterBase | int | 4 | 100 | 100 |
| yCenterBase | int | 4 | 100 | 100 |
| radius | int | 4 | 200 | 200 |
| height | int | 4 | 200 | 200 |

---

Below is a method, $searchArray$, that takes a 1D array of integers, $A$, and an integer key, $k$.

The method returns another 1D array: index zero is the number of elements in $A$ that are smaller than $k$, index one is the number of elements in $A$ that are larger than $k$:

```java
public static int[] searchArray(int[] s, int k) 
    {
        int[] result = new int[2];
        int countSmaller = 0;
        int countLarger = 0;

        for (int i = 0; i < s.length; i++) 
        {
            if (s[i] < k)
            {
                countSmaller++;
            }
            if (s[i] > k)
            {
                countLarger++;
            }
        }
        result[0] = countSmaller;
        result[1] = countLarger;
        return result;
    }
```
---

Below is a method $equal$ that takes two 2D int arrays, $a$ and $b$, as the input arguments and returns:

`true` if `a[i][j] = b[i][j]` for all elements of the two arrays,

`false` otherwise:

```java
public static boolean equal(int[][] a, int[][] b)
	{
		boolean isEqual = true;
		for (int row = 0; row < a.length; row++)
		{
			for (int col = 0; col < a[row].length; col++)
			{
				if (a[row][col] != b[row][col])
					isEqual = false;
			}
		}
		return isEqual;
	}
```
---

Below is a paint method that draws a circle in the middle of the screen based on the current width and height of the screen (it leaves 20 pixels from the borders and assumes that the title bar + menu bar is 40 pixels high)

```java
public void paint(Graphics g)
    {
        int w = getWidth();
        int h = getHeight();
        g.setColor(Color.BLUE);
        g.fillRect(20, 20, w - 40, h - 60);
        g.setColor(Color.WHITE);
        g.fillOval(20, 20, w - 40, h - 60);
    }
```
---

Below is a class called Student. We need to keep track of every student’s personal information (first and last name, address and telephone number) and their enrollment status (major, minor, credits completed and GPA).

UML diagram for the class:

```
+----------------+---------+-----------+----------------+
|    Student     |         |           |                |
+----------------+---------+-----------+----------------+
| - firstName    | String  |           |                |
| - lastName     | String  |           |                |
| - address      | String  |           |                |
| - telephone    | String  |           |                |
| - major        | String  |           |                |
| - minor        | String  |           |                |
| - credits      | int     |           |                |
| - gpa          | double  |           |                |
+----------------+---------+-----------+----------------+
| + Student()   |         |           |                |
| + Student(fn, ln, a, t, ma, mi, c, g)                |
| + getFirst()  | String  |           |                |
| + getLast()   | String  |           |                |
| + getAddress()| String  |           |                |
| + getTelephone()| String|           |                |
| + getMajor()  | String  |           |                |
| + getMinor()  | String  |           |                |
| + getCredits()| int     |           |                |
| + getGPA()    | double  |           |                |
+----------------+---------+-----------+----------------+
```
Below is the code to implement the class:

```java
public class Student 
{	
	//Data Members
	private String firstName;
	private String lastName;
	private String address;
	private String telephone;
	private String major;
	private String minor;
	private int credits;
	private double gpa;

	//No arg constructor
	public Student()
	{
		firstName = "John";
		lastName = "Smith";
		address = "123 Filbert St.";
		telephone = "(555) 123-4567";
		major = "Computer Science";
		minor = "None";
		credits = 80;
		gpa = 3.5;
	}
	
	//Arg constructor
	public Student(String fn, String ln, String a, String t, String ma, String mi, int c, double g)
	{
		firstName = fn;
		lastName = ln;
		address = a;
		telephone = t;
		major = ma;
		minor = mi;
		credits = c;
		gpa = g;
	}
	
	//Accessors
	public String getFirst() {return firstName;}
	public String getLast() {return lastName;}
	public String getAddress() {return address;}
	public String getTelephone() {return telephone;}
	public String getMajor() {return major;}
	public String getMinor() {return minor;}
	public int getCredits() {return credits;}
	public double getGPA() {return gpa;}
}
```
---

Given the following definitions of classes A and XYZ:

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

What is the structure and content of object p created as follows using java default constructor:

```java
XYZ p = new XYZ();
```

| Var Name | Type | Size (B) | Content |
|-------------|----------|---------------|---------|
| d | int | 4 | 0 |
| f | boolean | 1 bit | false |
| g | String | 2 bytes/char | "" |
| a | int[] | 4 bytes * length of array | {0,0,0,...} |
| b | double | 8 | 0.0 |
| c | String | 2 bytes/char | "" |
---

What are the unacceptable references made in methods of class XYZ?

None. All references are acceptable because class XYZ inherits from class A.