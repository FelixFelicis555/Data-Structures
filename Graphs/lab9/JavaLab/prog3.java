package pack2;  
import pack1.A;  
 class B{
 	public void msg(){
 	System.out.println("Hello,I am Same Class");}
 }
class prog3
{  
  public static void main(String args[]){  
   A obj = new A();  
   obj.msg(); 
   B obj1 = new B();
   obj1.msg();

  }  
}  