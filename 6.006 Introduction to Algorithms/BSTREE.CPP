#include<iostream.h>
#include<conio.h>
#include<process.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *left;
	struct node *right;
};
struct node *create_node(int a)
{
	struct node *temp=(struct node *)malloc(sizeof(struct node));
	temp->data = a;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}
struct node* insert(struct node* node, int a)
{
	if(node == NULL)
	{
		return create_node(a);
	}
	if(a < node->data)
	{
		node->left = insert(node->left, a);
	}
	else if(a > node->right)
	{
		node->right = insert(node->right, a);
	}
	return node;
}
struct node* delet(struct node* node, int a)
{
	if(node == NULL)
	{

	}
}
void traverse(struct node* node)
{
	char ch;
	printf("\nSelect a traversal type:\na.In\nb.Pre\nc.Post\n");
	scanf("%c", &ch);
	switch(ch)
	{
		case 'a':inorder(node);
			break;
		case 'b':preorder(node);
			break;
		case 'c':postorder(node);
			break;
	}
}
void inorder(struct node* node)
{
	if(node != NULL)
	{
		inorder(node->left);
		printf("%d\t", node->data);
		inorder(node->right);
	}
}
void preorder(struct node* node)
{
	if(node != NULL)
	{
		printf("%d\t", node->data);
		preorder(node->left);
		preorder(node->right);
	}
}
void postorder(struct node* node)
{
	if(node != NULL)
	{
		postorder(node->left);
		postorder(node->right);
		printf("%d\n", node->data);
	}
}
void main()
{
	char ch;
	int a;
	clrscr();
	struct node *root = NULL;
	printf("Enter the value of the root node:");
	scanf("%d", &a);
	root = insert(root, a);
	do
	{
	printf("Select choice:\na.Insertion\nb.Deletion\nc.Display\nd.Exit\n");
	scanf("%c",&ch);
	switch(ch)
	{
		case 'a':printf("\nINSERTION\n");
			printf("Enter value to insert into tree:");
			scanf("%d", &a);
			insert(root, a);
			break;
		case 'b':printf("\nDELETION\n");
			printf("Enter value to delete from the tree:");
			scanf("%d", &a);
			delet(root, a);
			break;
		case 'c':printf("\nDISPLAY\n");
			traverse(root);
			break;
		case 'd':printf("\nEXIT\n");
			exit();
		default :
			printf("\nINVALID CHOICE\n");
	}
	printf("Want to continue?(y/n)\n");
	scanf("%c",&ch);
	}while(ch=='y' || ch=='Y');
	getch();
}