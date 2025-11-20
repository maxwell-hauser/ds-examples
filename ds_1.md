JOptionPane Methods for dialog input/output are as follows:
Input Dialog:
/ input  grade
String input;
input = JOptionPane.showInputDialog(null, 
                "Enter a Positive Integer Number",
                "Grade (Project 1)",
                JOptionPane.QUESTION_MESSAGE);
		
// convert string input to integer 
p1 = Integer.parseInt(input);

Output Dialog:
 JOptionPane.showMessageDialog(" null,
                           “                 CSC 229 – Test 1"+”\n”+
                           “ _____________________________”+”\n”,
                           “Question 1”, JOptionPane.INFORMATION_MESSAGE);
(10)	1. Briefly explain the function of the following computer hardware components in program execution:
Hardware Component

Function
Control Unit
Processor
Handles arithmetic and logic

Fetches, decodes, and executes run cycles

RAM
Holds instructions and data

Disk
Holds long term information

Cache
Like RAM but faster



(10)	2. List the basic functions every programming language should support and give an example of each function in Java:
	
	1. +
	int sum = 6 + 2; //needs to not be part of a string
	2. *
	int product = 3 * 19;
	3. %
	int remainder = 21 % 4;


(10)	3. In the context of a programming language what is:

Error Type

What causes the error

Give an example

Syntax Error
Something like missing semicolons or parentheses at the end of a line

int number = 0;
switch (number
{
case “0”
break;
case “1”
break;
}
Won’t run because I didn’t put a closing parenthesis


Run-Time Error
A run-time error is an error that occurs at anytime during a program’s execution
Dividing by zero
Infinite loops


(10)	4. What is Java runtime Environment? What is stored in “src” directory of a Java project? What is stored in the “bin” directory.
	•	What is Java runtime Environment?
		You need a JRE to use java
		Includes java virtual machine, core classes, and supported libraries

	•	What is stored in “src” directory of a Java project?
		The .java files relating to a certain project

	•	What is stored in the “bin” directory.
			Stores compiled project/java files

(10)	5. Select the best data type in java for the following constants by placing an X in the corresponding cell.
Constant
char
byte
short
int
long
float
double
String
Anthony Blake
string







-25
int







-256.1999283565
double







34675
(assuming this is signed) int







1450891667
int







A
char







789302367100
long







true
Would be a boolean, but since that option is not available, I believe this is a string







-71657
int







203-555-7890
string









(10)	6. Develop a complete Java program that prompts the user to three integer numbers using input dialogues. Report minimum, maximum and average of the three numbers using an output dialogue.

import javax.swing.JOptionPane;

public class inClass {

	public static void main(String[] args)
	{
		String input;
		int p1, p2;
		int min, max, p3;
		double avg;
		
		input = JOptionPane.showInputDialog(null, 
		                "Enter a Positive Integer Number",
		                "Number",
		                JOptionPane.QUESTION_MESSAGE);
		p1 = Integer.parseInt(input);
		
		input = JOptionPane.showInputDialog(null, 
		                "Enter a Positive Integer Number",
		                "Number",
		                JOptionPane.QUESTION_MESSAGE);
		p2 = Integer.parseInt(input);
 
		input = JOptionPane.showInputDialog(null, 
		                "Enter a Positive Integer Number",
		                "Grade (Project 1)",
		                JOptionPane.QUESTION_MESSAGE);
		p3 = Integer.parseInt(input);
		
		avg = (p1 + p2 + p3)/3.0;
		
		if (p1 > p2)
		{
			max = p1;
			min = p2;
		}
		else
		{
			max = p2;
			min = p1;
		}
		
		if (p3 < min)
		{
			min = p3;
		}
		else if (p3 > max);
		{
			max = p3;
		}
	
		 JOptionPane.showMessageDialog(null,
                 "                 CSC 229 – Test 1\n" +
                 "_____________________________\n" +
                 "Min: " + min + " | Max: " + max + " | Average: " + avg,
                 "Question 1", JOptionPane.INFORMATION_MESSAGE);

		
	}
}



 (20)	7. Develop a Java program to prompt the user for the coordinates of the center of a circle on the cartesian coordinate system (x,y) and its radius (all integer numbers. Report circle’s properties, perimeter and area using an output dialogue.
Perimeter = 2  X radius            Area =   X  radius2                Where   = 3.14
import javax.swing.JOptionPane;

public class inClass {

	public static void main(String[] args)
	{
		String input;
		int x, y, r;
		int p, a;
		double pi = 3.14;
		
		input = JOptionPane.showInputDialog(null, 
		                "Enter x value",
		                "Number",
		                JOptionPane.QUESTION_MESSAGE);
		x = Integer.parseInt(input);
		
		input = JOptionPane.showInputDialog(null, 
		                "Enter y value",
		                "Number",
		                JOptionPane.QUESTION_MESSAGE);
		y = Integer.parseInt(input);
 
		input = JOptionPane.showInputDialog(null, 
		                "Enter radius",
		                "Number",
		                JOptionPane.QUESTION_MESSAGE);
		r = Integer.parseInt(input);
		
}
	p = 2 * pi * r;
	
	a = pi * r * r;
	
		 JOptionPane.showMessageDialog(null,
                 "                 CSC 229 – Test 1\n" +
                 "_____________________________\n" +
                 "x: " + x + " | y: " + y + " | r: " + r + " | Perimeter: " + p + " | Area: " + a,
                 "Question 1", JOptionPane.INFORMATION_MESSAGE);

		
	}
}




(20)	8. Develop a Java program that prompts the user for State code  ( the number next to the state name, 1,2, …) and income. Report the state name, income, tax rate and state tax owed based on the following table:

State code/State Name

Tax rate

	•	Connecticut 
% 6.35
	•	Massachusetts 
% 6.6
	•	New York
% 8.75
	•	Rhode Island
%6.75

