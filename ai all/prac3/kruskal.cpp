#include <iostream>
#include <algorithm>

using namespace std;

// Structure to represent an edge
struct Edge {
    int src, dest, weight;
};

// Function to find the set of an element
int find(int parent[], int i) {
    while (parent[i] != i)
        i = parent[i];
    return i;
}

// Function to perform union of two sets
void Union(int parent[], int rank[], int x, int y) {
    int xroot = find(parent, x);
    int yroot = find(parent, y);

    if (rank[xroot] < rank[yroot])
        parent[xroot] = yroot;
    else if (rank[xroot] > rank[yroot])
        parent[yroot] = xroot;
    else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}

// Function to compare two edges based on their weight
bool compareEdges(const Edge& edge1, const Edge& edge2) {
    return edge1.weight < edge2.weight;
}

// Function to find the MST using Kruskal's algorithm
void KruskalMST(Edge edges[], int numVertices, int numEdges) {
    Edge MST[numVertices];  // Array to store the MST edges

    // Sort the edges in non-decreasing order of weight
    sort(edges, edges + numEdges, compareEdges);

    int parent[numVertices];
    int rank[numVertices];
    for (int v = 0; v < numVertices; v++) {
        parent[v] = v;
        rank[v] = 0;
    }

    int MSTSize = 0;
    int edgeIndex = 0;

    while (MSTSize < numVertices - 1) {
        Edge nextEdge = edges[edgeIndex++];

        int srcParent = find(parent, nextEdge.src);
        int destParent = find(parent, nextEdge.dest);

        if (srcParent != destParent) {
            MST[MSTSize++] = nextEdge;
            Union(parent, rank, srcParent, destParent);
        }
    }

    cout << "Minimum Spanning Tree:\n";
    for (int i = 0; i < MSTSize; i++) {
        cout << MST[i].src << " - " << MST[i].dest << " : " << MST[i].weight << endl;
    }
}

int main() {
    int numVertices, numEdges;
    cout << "Enter the number of vertices: ";
    cin >> numVertices;
    cout << "Enter the number of edges: ";
    cin >> numEdges;

    Edge edges[numEdges];

    cout << "Enter source, destination, and weight of each edge:\n";
    for (int i = 0; i < numEdges; i++) {
        cin >> edges[i].src >> edges[i].dest >> edges[i].weight;
    }

    KruskalMST(edges, numVertices, numEdges);

    return 0;
}
