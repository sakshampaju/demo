#include <iostream>
using namespace std;

struct Item {
    int weight;
    int value;
};

int maxProfit = 0;

bool compare(Item a, Item b) {
    return (double)a.value / a.weight > (double)b.value / b.weight;
}

void bubbleSort(Item* items,int n)
{
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<n-i-1;j++)
		{
			if(!compare(items[j],items[j+1]))
			{
				swap(items[j],items[j+1]);
			}
		}
	}
}

void knapsackBranchAndBound(int capacity, Item* items, int level, int profit, int weight, int n) 
{
    if (weight > capacity) 
    	return;

    if (level == n) 
    {
        maxProfit = max(maxProfit, profit);
        return;
    }

    int bound = profit;

    while (level < n && weight + items[level].weight <= capacity) {
        bound += items[level].value;
        weight += items[level].weight;
        level++;
    }

    if (level < n) {
        bound += (capacity - weight) * (double)items[level].value / items[level].weight;
    }

    if (bound <= maxProfit) return;

    // Consider taking the item
    if (weight + items[level].weight <= capacity) {
        knapsackBranchAndBound(capacity, items, level + 1, profit + items[level].value, weight + items[level].weight, n);
    }

    // Consider not taking the item
    knapsackBranchAndBound(capacity, items, level + 1, profit, weight, n);
}

int knapsack(int capacity, Item* items, int n) {
   bubbleSort(items,n);

    int level = 0;
    int profit = 0;
    int weight = 0;

    knapsackBranchAndBound(capacity, items, level, profit, weight, n);

    return maxProfit;
}

int main() {
    int capacity = 50;
    Item items[] = { {10, 60}, {20, 100}, {30, 120} };
    int n = sizeof(items) / sizeof(items[0]);

    int maxProfit = knapsack(capacity, items, n);
    cout << "Maximum profit: " << maxProfit << endl;

    return 0;
}

