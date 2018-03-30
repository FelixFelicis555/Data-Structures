
interface MyInterface
 {
  public void get();

  public void show();
}

abstract class partial implements MyInterface {
   public void get()
   {

   }
   public void show() 
  {
    System.out.println("Hi,Welcome!!");
  }


 }
 class prog5 extends partial{
 	public static void main(String[] args)
 	{
 		prog5 A = new prog5();
 		A.show();
 	}
 }


