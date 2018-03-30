import java.util.Scanner;
interface Mystack
{
public void pop();
public void push();
public void peek();
public void display();
}
class Stackimp implements Mystack
{
int stack[]=new int[5];
int top=-1;
public void push()
{
if(top==(4))
{
System.out.println("overflow");
return;
}
else
{
int ele;
System.out.println("enter element");
Scanner s=new Scanner(System.in);
ele=s.nextInt();
stack[++top]=ele;
}
}
public void pop()
{
if(top<0)
{
System.out.println("underflow");
return;
}
else
{
int popper=stack[top];
top--;
System.out.println("popped element" +popper);
}
}
public void peek()
{
if(top<0)
{
System.out.println("underflow");
}
else
{
int popper=stack[top];
System.out.println("peek element" +popper);
}
}
public void display()
{
if(top<0)
{
System.out.println("empty");
return;
}
else
{
System.out.println("elements are");
for(int i=0;i<=top;i++){
	System.out.println(stack[i]);
}
}
}
}
class prog7
{
public static void main(String arg[])
{
Stackimp stk=new Stackimp();
int ch=0;
do{
	Scanner in=new Scanner(System.in);
	System.out.println("enter ur choice  \n1.push \n2.pop \n3.peek \n4.display \n10.exit");
	ch=in.nextInt();
	switch(ch){
	case 1:stk.push();
		break;
	case 2:stk.pop();
		break;
	case 3:stk.peek();
		break;
	case 4:stk.display();
		break;
	default:System.exit(0);
	}
}while(ch!=10);
}
}