#include<stdio.h>

void selectionsort(int b[],int n)
{
    
    int i,j,temp;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(b[i]>b[j])
            {
                temp=b[i];
                b[i]=b[j];
                b[j]=temp;
            }
        }
    }
}

int main()
{
    int a[10];
    int i,j,n;
    printf("\n enter number of array elements. ");
    scanf("%d",&n);
    printf("\n enter array elements");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("\n Unsorted  array=  ");
    printf("[");
    for(i=0;i<n;i++)
    {
        printf(" %d ",a[i]);
    }
    printf("]");
    selectionsort(a,n);
    printf("\n  Sorted array=    ");
    printf("[");
    for(i=0;i<n;i++)
    {
        printf(" %d ",a[i]);
    }
    printf("]");
}
