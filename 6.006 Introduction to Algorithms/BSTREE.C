#include<stdio.h>
#include<conio.h>
#include<process.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *left;
	struct node *right;
};
void inorder(struct node* node);
void preorder(struct node* node);
void postorder(struct node* node);
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
	else if(a > node->data)
	{
		node->right = insert(node->right, a);
	}
	return node;
}
struct node* maxi(struct node* node)
{
	if(node == NULL || node->right == NULL)
		return node;
	else
		return maxi(node->right);
}
struct node* mini(struct node* node)
{
	if(node == NULL || node->left == NULL)
		return node;
	else
		return mini(node->left);
}
struct node* find_pre_or_suc(struct node* node, int a, char ch)
{
	if(node == NULL)
		return node;
	else if(node->data == a)
	{
		if(ch == 'p')
			return maxi(node->left);
		else if(ch == 's')
			return mini(node->right);
	}
	else if(node->data < a)
		return find_pre_or_suc(node->right, a, ch);
	else
		return find_pre_or_suc(node->left, a, ch);
}
struct node* deletenode(struct node* node, int a)
{
	struct node* suc;
	struct node* temp;
	char ch = 's';
	if(node == NULL)
		return node;
	else if(node->data < a)
		node->right = deletenode(node->right, a);
	else if(node->data > a)
		node->left = deletenode(node->left, a);
	else
	{
		if(node->left == NULL)
		{
			temp = node->right;
			free(node);
			return temp;
		}
		else if(node->right == NULL)
		{
			temp = node->left;
			free(node);
			return temp;
		}
		suc = find_pre_or_suc(node, a, ch);
		node->data = suc->data;
		node->right = deletenode(node->right, suc->data);
	}
	return node;
}
void traverse(struct node* node)
{
	char ch;
	printf("\nSelect a traversal type:\na.In\nb.Pre\nc.Post\n>>");
	scanf(" %c", &ch);
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
	//Code Submitted By : SunnyVikasMalviya
	char ch2;
	int a,ch,n,i;
	struct node *root = NULL;
	struct node *suc;
	struct node *pre;
	clrscr();
	printf("Enter the value of the root node:");
	scanf("%d", &a);
	root = insert(root, a);
	do
	{
	printf("Select choice:\n1.Insertion\n2.Deletion\n3.Display\n4.Successor\n5.Predecessor\n6.Exit\nPress 7 for hidden operation ;)\n>>");
	scanf("%d", &ch);
	switch(ch)
	{
		case 1:printf("\nINSERTION\n");
			printf("Enter value to insert into tree:");
			scanf("%d", &a);
			insert(root, a);
			break;
		case 2:printf("\nDELETION\n");
			printf("Enter value to delete from the tree:");
			scanf("%d", &a);
			deletenode(root, a);
			break;
		case 3:printf("\nDISPLAY\n");
			traverse(root);
			break;
		case 4:printf("\nSUCCESSOR\n");
			printf("Successor of which node is required?:");
			scanf("%d", &a);
			suc = find_pre_or_suc(root, a, 's');
			printf("%d", suc->data);
			break;
		case 5:printf("\nPREDECESSOR\n");
			printf("Predecessor of which node is required?:");
			scanf("%d", &a);
			pre = find_pre_or_suc(root, a, 'p');
			printf("%d", pre->data);
			break;
		case 7:printf("\nINSERT MULTIPLE\n");
			printf("Enter number of nodes to insert:");
			scanf("%d", &n);
			printf("Enter %d numbers:(Press enter after every number)", n);
			for(i=0;i<n;i++)
			{
				scanf("%d", &a);
				insert(root, a);
			}
			break;
		case 6:printf("\nEXIT\n");
			exit(0);
		default :
			printf("\nINVALID CHOICE\n");
	}
	printf("Want to continue?(y/n)\n>>");
	scanf(" %c", &ch2);
	}while(ch2=='y' || ch2=='Y');
	getch();
}

