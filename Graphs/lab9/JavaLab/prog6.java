import java.util.*;
public class prog6
{  

   void check(int age)
   {  
     if(age<18)  
      throw new ArithmeticException("not eligible to vote!!");  
     else  
      System.out.println("welcome to vote");  
   }  
   public static void main(String args[]){  
      System.out.println("Enter Your Age:");  
      Scanner in = new Scanner(System.in);
      int age=in.nextInt();
      prog6 A=new prog6();
      A.check(age);
  }  
}  
