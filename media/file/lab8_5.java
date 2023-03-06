package lab8_programs;

import java.util.TreeMap;

class random 
{
	String name;
	int age;
	public random(String name,int age)
	{
		this.name=name;
		this.age=age;
	}
	 String tostring()
			{
			return ("name= "+name +"\nage="+age); 
			}

}

public class sortbyname implements Comparartor<random>
{
	public int compare()
	
}

public class lab8_5 {
public static void main(String[] args)
{
	
	TreeMap<random,String> m=new TreeMap<random,String>();
	m.put(new random("Bhairavi",22),"Singing");
	m.put(new random("Dhara",23), "Sketching");
	m.put(new random("Anmol",23), "Reading");
	m.put(new random("Megh",21), "Singing");
	m.put(new random("Raag",22), "Sketching");
	System.out.println("Tree_map=" +m);
	
}

	
	

}
