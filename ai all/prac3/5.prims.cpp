#include<iostream>
using namespace std;

class Graph
{
    int m[10][10], nodes;
public:
    void create();
    void prims();
};

void Graph::create()
{
    int i, j;
    cout << "Enter Total Offices: ";
    cin >> nodes;
    cout << "\nEnter Adjacency Matrix: \n";
    for (i = 0; i < nodes; i++)
    {
        for (j = i; j < nodes; j++) 
        {
            cout << "Enter distance between " << i+1 << " and " << j+1 << endl;
            cin >> m[i][j];
            m[j][i] = m[i][j];
        }
    }

    for (i = 0; i < nodes; i++) 
    {
        for (j = 0; j < nodes; j++) 
        {
            if (m[i][j] == 0)
                m[i][j] = 999;    //fill infinity where path is not present
        }
    }
}

void Graph::prims() 
{
    int visited[10], i, j;
    int count=0;
    int min = 0, u, v;
    int cost = 0;
    for (i = 0; i < nodes; i++)
        visited[i] = 0;

    visited[0] = 1;        //starting vertex is always node-0

    while (count < nodes - 1) 
    {
        min = 999;

        for (i = 0; i < nodes; i++) 
        {
            if (visited[i] == 1) 
            {
                for (j = 0; j < nodes; j++) 
                {
                    if (visited[j] == 0) 
                    {
                        if (min > m[i][j]) 
                        {
                            min = m[i][j];
                            u= i;
                            v = j;
                        }
                    }
                }
            }
        }
        visited[v] = 1;
        cout << "\n" << u+1 << " --> " << v+1;
        cost += m[u][v];
        count++;
    }
    cout << "\nOptimal cost is: " << cost << endl;
}

int main() 
{
    Graph s;
    cout << "\nPrims Algorithm to connect several offices\n";
    s.create();
    s.prims();
}
