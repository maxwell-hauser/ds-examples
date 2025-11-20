Name: Maxwell Hauser
CSC 229 				   Test #2 			          	100 Points
Complete the exam, save the file as a Microsoft Word file labeled as “your last name-your first name ”, submit through BB and via email with a subject line that reads as “CSC 229-70 – Test 2 – your last name-your first name” 
on or before 3:10 PM
Late submissions are subject to 20% penalty per 5 minutes
(20)	1. Develop a method sum that given an integer n, return the value of the following series. 
    	S = 1 + 12+14+… + 12n

public static double sum(int n)
	{
		double number = 1;
		if (n == 0)
		{
			return 0;
		}
		
		else if (n == 1)
		{
			return 1;
		}
		
		else
		{
			for (int i = 1; i < n; i++)
			{
				number += (1/(double)(Math.pow(2, i)));
			}
		}
		
		return number;
	}


(20)	2. Develop a method called count that given two integers k1 and k2 returns the number of integers between k1 and k2 that are divisible by either 7 or 11 but not both, return the count.

	public static int count(int k1, int k2)
	{
		int counter = 0;
		for (int i = k1+1; i < k2; i++)
		{
			if (i % 7 == 0 && i % 11 == 0) {continue;}
		
			else if (i % 7 == 0 || i % 11 == 0) {counter++; continue;}
		}
		
		return counter;	
	}


(20) 	3. Develop a method called maxArray that given a two-dimensional array t of integers, returns the maximum of the elements stored in the array.

public static int maxArray(int[][] t)
	{
		int maxValue = Integer.MIN_VALUE;
		for (int row = 0; row < t.length; row++)
		{
			for (int col = 0; col < t[row].length; col++)
			{
				if (t[row][col] > maxValue)
				{
					maxValue = t[row][col];
				}
			}
		}
		return maxValue;
	}

(20)	4. Develop a method summerPay that given the rank of a teaching faculty (a String) and number of credit hours she/he taught during summer (an integer) returns the total summer earnings for that faculty. Use the following table:

      Wages for 1 credit of teaching for full-time faculty members
Rank
Year 2020
Professor
$ 2,146
Associate Professor
$ 1,977
Assistant Professor
$ 1,825
Instructor
$ 1,672

public static int summerPay(String s, int i)
	{
		int pay = 0;
		switch (s)
		{
		case "Professor":
			pay = 2146*i;
			
		case "Associate Professor":
			pay = 1977*i;
		
		case "Assistant Professor":
			pay = 1825*i;

		case "Instructor":
			pay = 1672*i;
			
		default:
			pay = -1;
		}		
		return pay;
	}

(20)	5. Design a class named Sphere to represent a Geometric shape Sphere represented by the coordinates of the center of sphere ( xc, yc ) and its radius ( r )	


sphere surface  = ( 4 π r2 )    
sphere  volume = ( 4/3 π r3  )

(5)	Draw the UML diagram for the class 
I had no idea how to use those boxes so I’m just going to type it.

Class header first
then data members
then constructors
then accessors
then other methods

 (5)	Develop Java code to define data members and constructors
public class Sphere {
	// data members
	private int xc, yc, r;
	// constructors
	public Sphere()
	// no-argument constructor
	{
		xc = 0;
		yc = 0;
		r = 10;
	}
	
	public Sphere(int xc1, int yc1, int r1)
	//yes-argument constructor
	{
		xc = xc1;
		yc = yc1;
		r = r1;
	}
	
	// accessors
	public int getR() {return r;}
	public int getX() {return xc;}
	public int getY() {return yc;}
	
	// other methods
	public double getSurface()
	{
		return 4 * Math.PI * r * r;
	}
	
	public double getVolume()
	{
		return (4 /(double)3) * Math.PI * r * r * r;
	}
}

(10)	Develop Java code to define accessors and other methods

See above :)
