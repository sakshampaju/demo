#include<iostream>
#include<algorithm>
using namespace std;

class Edge
{
	public:
	int source;
	int dest;
	int weight;
};

bool compare(Edge e1,Edge e2)
{
	return e1.weight<e2.weight;
}

int findParent(int v,int *parent)
{
	if(parent[v]==v)
	{
		return v;
	}
	return findParent(parent[v],parent);
}

void kruskal(Edge* input,int n,int E)
{
	//sort the input array ascending order on basis of weights
	sort(input,input+E,compare);
	
	Edge *output=new Edge[n-1];
	
	int *parent=new int[n];  //to store parent of each vertex
	
	for(int i=0;i<n;i++)
	{
		parent[i]=i;
	}
	
	int count=0; //tells currently how many edges are added
	int i=0;     //tells current working edge
	
	while(count!=n-1)
	{
		Edge currentEdge=input[i];    
		
		//Check if we can add the currentEdge in MS or not
		int sourceParent=findParent(currentEdge.source,parent);
		int destParent=findParent(currentEdge.dest,parent);
		
		if(sourceParent!=destParent)
		{
			output[count]=currentEdge;
			count++;
			parent[sourceParent]=destParent;
		}
		i++;
	}
	
	for(int i=0;i<n-1;i++)
	{	
		if(output[i].source<output[i].dest)
		{
			cout<<output[i].source<<"  "<<output[i].dest<<"  "<<output[i].weight<<endl;
		}
		else
		{
			cout<<output[i].dest<<"  "<<output[i].source<<"  "<<output[i].weight<<endl;
		}
		
	}
}

int main()
{
	int n,E;  //n-no.of vertices, E=No.of edges
	cin>>n>>E;
	Edge *input=new Edge[E];
	
	for(int i=0;i<E;i++)
	{
		int s,d,w;
		cin>>s>>d>>w;
		input[i].source=s;
		input[i].dest=d;
		input[i].weight=w;
	}
	
	kruskal(input,n,E);
	
}

