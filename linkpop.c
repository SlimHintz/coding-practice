#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


typedef struct node
{
	int data;
	struct node *next;
}
node;

int length(void);
int* createarr(int n);
node* linkarr(int *arr, int length);
void printarr(int *arr, int length);
void printlink(node *head);
void selsortarr(int *arr, int length);
//TODO


int main(void)
{
	//declare variables
	int *arr = NULL;
	node *head, *tmp;
	int n;
	//prompt user for the number of entries into the list
	n = length();
	//use prompt the user to enter values into the list n times
	arr = createarr(n);
	//create a singly linked list with head pointing to its start
	head = linkarr(arr, n);
	//print out the array
	printarr(arr, n);
	//print out the linked list
	printlink(head);
	//allocated memory
	free(arr);
	return 0;
}





//create a function prompt user for the number of user input
int length(void)
{
	int n;
	printf("# of entries to be added to the list: ");
	scanf("%i", &n);
	return n;
}
//create a function to a generate an array from user input
int* createarr(int n)
{
	int i;
	int *a = NULL;
	a = malloc(n * sizeof(int));
	if (a == NULL)
	{
		return NULL;
	}
	for (int i = 0; i < n; i++)
	{
		printf("Element %i of the array is: ", (i+1));
		scanf("%i", &a[i]);
	}
	return a;
}

//program to print the contents of an array

void printarr(int *arr, int length)
{
	//print out arr using a for loop
	//declare variables
	int i;
	for (int i = 0; i < length; i++)
	{
		printf("%i\n", arr[i]);
	}
}

//program to take an array and convert it to a singly linked list and return a pointer to head
node* linkarr(int *arr, int length)
{
	//declare variables
	node *head = malloc(sizeof(node));
	node *current = NULL;
	node *tmp = NULL;
	
	int i, j, k;
 	for (i = 0; i < length; i++)
	{
		//create node containing the current array index's data value
		current = malloc(sizeof(node));
		current->data = arr[i];
		current->next = NULL;
		//use a temporary node to find the end of the list
		for (node *tmp = head; tmp->next!= NULL; tmp = tmp->next)
		{
			//point the tmp to the final item on the liat and point it to the current node 
			if (tmp->next ==  NULL)
			{
				tmp->next = current;
			}

		}
	}
	head = current;
	free(current);
	return head;
}

//program to print out a linked list

void printlink(node *head)
{
	//declare variables
	printf("printlink is invoked\n");
	node *tmp = head;
	int i = 1;
	//print out each link in the list
	while (tmp->next != NULL)
	{
		printf("Element %i of the linked list is %i\n", i, tmp->data);
		tmp = tmp->next;
		i++;
	}
}

