interface i1
{
	public void method1();
	public void method2();
	public void method3();
}

class c1 implements i1
{
	public void method1()
	{

	}

	public void method2()
	{
		System.out.println("This is method 2");
	}

	public void method3()
	{

	}

	interface i2
	{
		public void method4();
		public void method5();
	}
}

class c2 implements c1.i2
{
	public void method4()
	{
		System.out.println("This is method 4");
	}

	public void method5()
	{
		System.out.println("This is method 5");
	}
}

interface i3 extends i1
{
	public void method6();
}

class c3 implements i3
{
	public void method3()
	{

	}

	public void method6()
	{
		System.out.println("This is method 6");
	}

	public void method2()
	{

	}

	public void method1()
	{
		System.out.println("This is method 1");
	}
}

class prog2
{
	public static void main(String[] args)
	{
		c1 ob1 = new c1();
		c2 ob2 = new c2();
		c3 ob3 = new c3();
		ob1.method2();
		ob2.method4();
		ob2.method5();
		ob3.method1();
	}
}