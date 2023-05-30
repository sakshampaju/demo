#include<iostream>
#include<queue>
#define MAX 5

class Graph
{
	public:
	int m[5][5];
	char node[5]={'A','B','C','D','E'};
	int que[MAX];
	int stack[MAX];
	int top=0;
	Graph()
	{
		for(int i=0;i<MAX;i++)
		{
			for(int j=0;j<5;j++)
			{
				m[i][j]=0;
				
			}
		}
		
		for(int j=0;j<MAX;j++)
		{
			stack[j]=0;
		}
	}
	void create();
	void display();
	void dfs();
	void bfs();
};



void Graph::create()
{
	// A B C D E
	int p,q;
	char ch;
	do{
		std::cout<<"Enter source ";
		std::cin>>p;
		int R=p;
		
		std::cout<<"Enter destination ";
		std::cin>>q;
		int C=q;
		
		m[R][C]=1;
		m[C][R]=1;
	
	std::cout<<"Do you want to continue y or n ? "<<std::endl;
	std::cin>>ch;
	
	}while(ch=='y');
		
}


void Graph::dfs()
{
    std::cout << " =====  Program to demonstrate the DFS Traversal on a Graph, in CPP  ===== \n\n";
    int i, j, k,v;
    int visited[5]={0};
    int visit[5]={0};
    std::cout << "\nEnter the initial vertex to start the DFS traversal with: ";
    std::cin >> v;
    std::cout << "\nThe DFS traversal on the given graph is : \n";
    std::cout << v << " ";

    visited[v] = 1;

    k = 1;

    while (k < MAX)
    {
        for (j = MAX-1; j >= 0; j--)
        {
            if (m[v][j] != 0 && visited[j] != 1 && visit[j] != 1)
            {
                visit[j] = 1;
                stack[top] = j;
                top++;
            }
        }
        v = stack[--top];
        std::cout << v << " ";
        k++;
        visit[v] = 0;
        visited[v] = 1;
    }
        std::cout << "\n\n\n";

}

void Graph::bfs()
{
    std::cout << " =====  Program to demonstrate the BFS Traversal on a Graph, in CPP  ===== \n\n";
    std::queue<int>quearr;
    int i, j, k,v;
    int visited[5]={0};
    
    std::cout << "\nEnter the initial vertex to start the BFS traversal with: ";
    std::cin >> v;
    std::cout << "\nThe BFS traversal on the given graph is : \n";
    
    visited[v] = 1;
    quearr.push(v);
    
    k = 1;

    while(!quearr.empty())
    {
    	int currentNode=quearr.front();
    	std::cout<<currentNode<<"  ";
    	quearr.pop();
    	
    	for(int i=0 ;i<MAX ;i++)
    	{
    		if(m[currentNode][i]!=0 && visited[i]!=1)
    		{
    			visited[i]=1;
    			quearr.push(i);
    		}
    		
    	}
    }
    
        std::cout << "\n\n\n";

}


void Graph::display()
{
	for(int i=0;i<5;i++)
	{
		std::cout<<node[i]<<"\t";
		for(int j=0;j<5;j++)
		{
			std::cout<<m[i][j]<<"\t";
		}
		std::cout<<std::endl;
	}
	std::cout<<std::endl<<std::endl;
	
}

int main()
{
	Graph t;
	int ch;
	char p;
	while(1)
	{
		std::cout<<"1.Create "<<std::endl;
		std::cout<<"2.Display "<<std::endl;
		std::cout<<"3.DFS "<<std::endl;
		std::cout<<"4.BFS "<<std::endl;
		std::cout<<"5.Exit "<<std::endl;
		std::cout<<"Enter your choice: ";
		std::cin>>ch;
		std::cout<<std::endl<<std::endl;
		switch(ch)
		{
			
			case 1:
				t.create();
				break;
			case 2:
				t.display();
				break;
			case 3:
				t.dfs();
				break;
			case 4:
				t.bfs();
				break;
			case 5:
				exit(0);
		}
		
		
	
	}
	
	return 0; 
}
