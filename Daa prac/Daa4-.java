import java.util.Scanner;

class Knapsack
{
	int maxProfit(int weight[],int profit[],int currentindex,int capacity,int n)
	{
		if(currentindex==n)
			return 0;
			
		int ciw=weight[currentindex];
		int cip=profit[currentindex];
		int consider=0;
		int notconsider=0;
		if(ciw<=capacity)
		{	
			consider=cip+maxProfit(weight,profit,currentindex+1,capacity-ciw,n);
			notconsider=maxProfit(weight,profit,currentindex+1,ciw,n);
		}
		
		return Math.max(consider,notconsider);
	}
	
	public int knapsack(int weight[],int profit[],int capacity,int n)
	{
		return maxProfit(weight,profit,0,capacity,n);
	}
	
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		Knapsack k=new Knapsack();
		int weight[]=new int[10];
		int profit[]=new int[10];
		int n,capacity;
		
		System.out.println("Enter n : ");
		n=sc.nextInt();
		
		System.out.println("Enter capacity : ");
		capacity=sc.nextInt();
		
		System.out.println("Enter weight array : ");
		for(int i=0;i<n;i++)
		{
			weight[i]=sc.nextInt();
		}
		
		System.out.println("Enter profit array : ");
		for(int i=0;i<n;i++)
		{
			profit[i]=sc.nextInt();
		}
		
		int maxprofit=k.knapsack(weight,profit,capacity,n);
		System.out.println("Maximum profit is : "+maxprofit);
		
	}
}
