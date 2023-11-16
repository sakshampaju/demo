//Iterative Program

#include<iostream>
using namespace std;

int main()
{
	int n1=0,n2=1,n3,i,n;
	cout<<"Enter number of elements : ";
	cin>>n;
	cout<<endl;
	cout<<n1<<"   "<<n2<<"  ";
	for(i=2;i<n;i++)
	{
		n3=n1+n2;
		cout<<n3<<"  ";
		n1=n2;
		n2=n3;
	}
	cout<<endl;
	return 0;
}

/*

OUTPUT: 

Enter number of elements : 20  

0   1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597  2584  4181  

*/

//Recursive Program

#include<iostream>
using namespace std;


int fibonacci(int n)
{
	if(n<=1)
	{
		return n;
	}
	else
	{
		return fibonacci(n-1)+fibonacci(n-2);	
	}
}

int main()
{
	int n,i;
	cout<<"Enter number of elements : ";
	cin>>n;
	cout<<endl;
	
	for(i=0;i<n;i++)
	{
		cout<<fibonacci(i)<<"  ";
	}
	cout<<endl;
}

/*

OUTPUT:

Enter number of elements : 10

0  1  1  2  3  5  8  13  21  34  

*/


