class prog1{
	public static void main(String args[]){  
   try
   {  
    	int[] arr=new int[5];  
    	arr[10]=30/0;  
   }
  
   catch(ArrayIndexOutOfBoundsException e)
   {
   System.out.println("Array Index Out of Bound");
   }  
    catch(ArithmeticException e)
   {
   System.out.println("Divided by Zero");
   }  
}
}