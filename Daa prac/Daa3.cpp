#include<iostream>
using namespace std;

struct Item
{
	int profit,weight;
	Item(int profit,int weight)
	{
		this->profit=profit;
		this->weight=weight;
	}	
};

void swapItems(Item *a, Item* b)
{
	Item temp=*a;
	*a=*b;
	*b=temp;

}

double fractionalKnapsack(int w,Item arr[],int N)
{
	for(int i=0;i<N-1;i++)
	{
		int maxIndex=i;
		for(int j=i+1;j<N;j++)
		{
			double ratio1=(double)arr[j].profit/arr[j].weight;
			double ratio2=(double)arr[maxIndex].profit/arr[maxIndex].weight;
			if(ratio1>ratio2)
			{
				maxIndex=j;
			}
		}
		
		swapItems(&arr[maxIndex],&arr[i]);
	}
	
	double finalvalue=0.0;
	
	for(int i=0;i<N;i++)
	{
		if(arr[i].weight<=w)
		{
			w-=arr[i].weight;
			finalvalue+=arr[i].profit;
		}
		else
		{
			finalvalue+=arr[i].profit*((double)w/(double)arr[i].weight);
			break;
		}
	}
	
	return finalvalue;
}

int main()
{
	int w=60;
	Item arr[]={{60,10},{100,20},{120,30}};
	int N=sizeof(arr)/sizeof(arr[0]);
	
	cout<<fractionalKnapsack(w,arr,N);
	
	return 0;
}
