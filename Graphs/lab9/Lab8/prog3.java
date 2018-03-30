import java.util.Scanner;
import pack.*;

class attendance extends pack.Student{
	int att;
	Scanner sc=new Scanner(System.in);
	void getatt()
		{
		System.out.println("Enter attendance percentage");
		att=sc.nextInt();
	}
}

class prog3{
	public static void main(String args[])
	{	
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the number of students");
		int n=sc.nextInt();
		attendance[] a=new attendance[n];
		int i;
		for(i=0;i<n;i++)
		{
			a[i]=new attendance();
			a[i].getid();
			a[i].getatt();
		}
		for(i=0;i<n;i++)
		{
			if (a[i].att<75)
			{
				System.out.println(a[i].id+" has attendance shortage");
			}
			else
			{
				System.out.println(a[i].id+" doesnt have attendance shortage");
			}
		}
	}
}