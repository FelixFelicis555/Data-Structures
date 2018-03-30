package pack;
import java.util.Scanner;

public class Student{
	public int id;
	Scanner sc=new Scanner(System.in);
	public void getid()
	{
		System.out.println("Enter ID");
		id=sc.nextInt();
	}

}