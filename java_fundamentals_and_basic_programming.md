# Java Fundamentals and Basic Programming

## JOptionPane Dialog Methods

### Input Dialog

```java
String input;
input = JOptionPane.showInputDialog(null, 
                "Enter a Positive Integer Number",
                "Grade (Project 1)",
                JOptionPane.QUESTION_MESSAGE);

// Convert string input to integer 
int p1 = Integer.parseInt(input);
```

### Output Dialog

```java
JOptionPane.showMessageDialog(null,
                           "CSC 229 – Test 1\n" +
                           "_____________________________\n",
                           "Question 1", 
                           JOptionPane.INFORMATION_MESSAGE);
```

## Computer Hardware Components

| Hardware Component | Function                                           |
|--------------------|-----------------------------------------------------|
| Control Unit       | Fetches, decodes, and executes instruction cycles   |
| Processor (CPU)    | Handles arithmetic and logic operations             |
| RAM                | Holds instructions and data for active programs     |
| Disk               | Provides long-term storage for data                 |
| Cache              | Fast temporary storage between CPU and RAM          |

## Basic Programming Language Functions

### Arithmetic Operations in Java

1. **Addition**
   ```java
   int sum = 6 + 2;  // Result: 8
   ```

2. **Multiplication**
   ```java
   int product = 3 * 19;  // Result: 57
   ```

3. **Modulus**
   ```java
   int remainder = 21 % 4;  // Result: 1
   ```

## Programming Errors

| Error Type       | Cause                                                | Example                                                                 |
|------------------|------------------------------------------------------|-------------------------------------------------------------------------|
| Syntax Error     | Missing semicolons, parentheses, or incorrect syntax | Missing closing parenthesis in switch statement                         |
| Run-Time Error   | Errors occurring during program execution            | Division by zero, infinite loops, null pointer exceptions               |

### Syntax Error Example

```java
int number = 0;
switch (number)  // Missing closing parenthesis
{
    case 0:      // Missing colon
        break;
    case 1:
        break;
}
```

## Java Development Environment

### Java Runtime Environment (JRE)

The JRE is required to run Java applications and includes:

- Java Virtual Machine (JVM)
- Core classes
- Supporting libraries

### Project Directory Structure

| Directory | Contents                                |
|-----------|-----------------------------------------|
| `src/`    | Java source files (`.java`)             |
| `bin/`    | Compiled bytecode files (`.class`)      |

## Data Type Selection

| Constant         | Best Data Type | Reasoning                                      |
|------------------|----------------|------------------------------------------------|
| Anthony Blake    | `String`       | Text data                                      |
| -25              | `int`          | Small negative integer                         |
| -256.1999283565  | `double`       | Decimal number requiring precision             |
| 34675            | `int`          | Integer within standard range                  |
| 1450891667       | `int`          | Large integer within int range                 |
| A                | `char`         | Single character                               |
| 789302367100     | `long`         | Exceeds int range (> 2,147,483,647)            |
| true             | `boolean`      | Boolean value                                  |
| -71657           | `int`          | Negative integer                               |
| 203-555-7890     | `String`       | Phone number (contains non-numeric characters) |

## Program: Find Minimum, Maximum, and Average

```java
import javax.swing.JOptionPane;

public class MinMaxAverage {

    public static void main(String[] args) {
        String input;
        int p1, p2, p3;
        int min, max;
        double avg;
        
        // Get first number
        input = JOptionPane.showInputDialog(null, 
                        "Enter first integer",
                        "Number 1",
                        JOptionPane.QUESTION_MESSAGE);
        p1 = Integer.parseInt(input);
        
        // Get second number
        input = JOptionPane.showInputDialog(null, 
                        "Enter second integer",
                        "Number 2",
                        JOptionPane.QUESTION_MESSAGE);
        p2 = Integer.parseInt(input);
        
        // Get third number
        input = JOptionPane.showInputDialog(null, 
                        "Enter third integer",
                        "Number 3",
                        JOptionPane.QUESTION_MESSAGE);
        p3 = Integer.parseInt(input);
        
        // Calculate average
        avg = (p1 + p2 + p3) / 3.0;
        
        // Determine min and max
        if (p1 > p2) {
            max = p1;
            min = p2;
        } else {
            max = p2;
            min = p1;
        }
        
        if (p3 < min) {
            min = p3;
        }
        if (p3 > max) {
            max = p3;
        }
        
        // Display results
        JOptionPane.showMessageDialog(null,
                     "Results\n" +
                     "_____________________________\n" +
                     "Min: " + min + " | Max: " + max + " | Average: " + avg,
                     "Statistics", 
                     JOptionPane.INFORMATION_MESSAGE);
    }
}
```

## Program: Circle Properties Calculator

Calculate the perimeter and area of a circle given its center coordinates and radius.

**Formulas:**
- Perimeter = 2π × radius
- Area = π × radius²
- π ≈ 3.14

```java
import javax.swing.JOptionPane;

public class CircleProperties {

    public static void main(String[] args) {
        String input;
        int x, y, r;
        double pi = 3.14;
        double perimeter, area;
        
        // Get x coordinate
        input = JOptionPane.showInputDialog(null, 
                        "Enter x coordinate",
                        "X Value",
                        JOptionPane.QUESTION_MESSAGE);
        x = Integer.parseInt(input);
        
        // Get y coordinate
        input = JOptionPane.showInputDialog(null, 
                        "Enter y coordinate",
                        "Y Value",
                        JOptionPane.QUESTION_MESSAGE);
        y = Integer.parseInt(input);
        
        // Get radius
        input = JOptionPane.showInputDialog(null, 
                        "Enter radius",
                        "Radius",
                        JOptionPane.QUESTION_MESSAGE);
        r = Integer.parseInt(input);
        
        // Calculate perimeter and area
        perimeter = 2 * pi * r;
        area = pi * r * r;
        
        // Display results
        JOptionPane.showMessageDialog(null,
                     "Circle Properties\n" +
                     "_____________________________\n" +
                     "Center: (" + x + ", " + y + ")\n" +
                     "Radius: " + r + "\n" +
                     "Perimeter: " + perimeter + "\n" +
                     "Area: " + area,
                     "Results", 
                     JOptionPane.INFORMATION_MESSAGE);
    }
}
```

## Program: State Tax Calculator

Calculate state tax based on state code and income.

### State Tax Rates

| State Code | State Name    | Tax Rate |
|------------|---------------|----------|
| 1          | Connecticut   | 6.35%    |
| 2          | Massachusetts | 6.60%    |
| 3          | New York      | 8.75%    |
| 4          | Rhode Island  | 6.75%    |

```java
import javax.swing.JOptionPane;

public class StateTaxCalculator {

    public static void main(String[] args) {
        String input;
        int stateCode;
        double income, taxRate = 0, taxOwed;
        String stateName = "";
        
        // Get state code
        input = JOptionPane.showInputDialog(null, 
                        "Enter state code:\n" +
                        "1 - Connecticut\n" +
                        "2 - Massachusetts\n" +
                        "3 - New York\n" +
                        "4 - Rhode Island",
                        "State Code",
                        JOptionPane.QUESTION_MESSAGE);
        stateCode = Integer.parseInt(input);
        
        // Get income
        input = JOptionPane.showInputDialog(null, 
                        "Enter income",
                        "Income",
                        JOptionPane.QUESTION_MESSAGE);
        income = Double.parseDouble(input);
        
        // Determine tax rate and state name
        switch (stateCode) {
            case 1:
                stateName = "Connecticut";
                taxRate = 0.0635;
                break;
            case 2:
                stateName = "Massachusetts";
                taxRate = 0.0660;
                break;
            case 3:
                stateName = "New York";
                taxRate = 0.0875;
                break;
            case 4:
                stateName = "Rhode Island";
                taxRate = 0.0675;
                break;
            default:
                JOptionPane.showMessageDialog(null,
                             "Invalid state code",
                             "Error",
                             JOptionPane.ERROR_MESSAGE);
                return;
        }
        
        // Calculate tax owed
        taxOwed = income * taxRate;
        
        // Display results
        JOptionPane.showMessageDialog(null,
                     "Tax Calculation\n" +
                     "_____________________________\n" +
                     "State: " + stateName + "\n" +
                     "Income: $" + income + "\n" +
                     "Tax Rate: " + (taxRate * 100) + "%\n" +
                     "Tax Owed: $" + taxOwed,
                     "Results", 
                     JOptionPane.INFORMATION_MESSAGE);
    }
}
```

