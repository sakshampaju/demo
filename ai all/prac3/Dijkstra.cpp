#include <iostream>
#include <limits.h>
#define V 5
#define INF INT_MAX

// Function to find the vertex with the minimum distance value
int minDistance(int dist[], bool visited[])
{
    int minDist = INF;
    int minIndex = -1;

    for (int v = 0; v < V; v++)
    {
        if (!visited[v] && dist[v] <= minDist)
        {
            minDist = dist[v];
            minIndex = v;
        }
    }

    return minIndex;
}

// Function to print the shortest path from source to destination
void printPath(int parent[], int j)
{
    if (parent[j] == -1)
        return;

    printPath(parent, parent[j]);
    std::cout << " -> " << j;
}

// Function to print the distance array
void printDistance(int dist[])
{
    std::cout << "Vertex \t Distance from Source\n";
    for (int i = 0; i < V; i++)
        std::cout << i << "\t\t" << dist[i] << '\n';
}

// Dijkstra's algorithm to find the shortest path from source vertex
void dijkstra(int graph[V][V], int src)
{
    int dist[V];     // Array to store the shortest distance from source
    bool visited[V]; // Array to keep track of visited vertices
    int parent[V];   // Array to store the parent of each vertex in the shortest path

    for (int i = 0; i < V; i++)
    {
        dist[i] = INF;
        visited[i] = false;
        parent[i] = -1;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++)
    {
        int u = minDistance(dist, visited);
        visited[u] = true;

        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && graph[u][v] && dist[u] != INF && dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    printDistance(dist);

    for (int i = 0; i < V; i++)
    {
        if (i != src)
        {
            std::cout << "\nShortest path from " << src << " to " << i << ": ";
            printPath(parent, i);
        }
        std::cout << '\n';
    }
}

int main()
{
    //int V;
   // std::cout << "Enter the number of vertices: ";
    //std::cin >> V;

    int graph[V][V];
    std::cout << "Enter the adjacency matrix:\n";
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            std::cin >> graph[i][j];
        }
    }

    int source;
    std::cout << "Enter the source vertex: ";
    std::cin >> source;

    dijkstra(graph, source);

    return 0;
}
