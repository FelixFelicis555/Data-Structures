class prog2{ 

 public static void main(String args[]){

	try
	{  
		try
			{  
		 		System.out.println("division by 0");  
		 		int a=10/0;  
			}
		catch(ArithmeticException e)
			{
				System.out.println("Number cant be divide by Zero.Please Look to it!");
			}  
	 try
	 		{  
				int a[]=new int[5];  
				a[5]=4;  
			}
		catch(ArrayIndexOutOfBoundsException e)
			{
				System.out.println(e);
			}  
		 
		System.out.println("Try Executed!!");  
	}
	catch(Exception e)
	{
		System.out.println("Exception handeled");
	}  
	
	System.out.println("normal flow..");  
 }  
}  