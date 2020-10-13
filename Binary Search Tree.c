#include<stdio.h>
#include<stdlib.h>

struct node 
{
  int data;
  struct node * left;
  struct node * right;
}*root,*sroot,*temp,*t;

struct node * create_node(int d)
{
  temp = malloc(sizeof(struct node));
  temp -> data = d;
  temp -> left = NULL;
  temp -> right = NULL;
  return temp;
}
void insert_node(int d)
{
  if (root == NULL)
  {
    root = create_node(d);
    sroot = root;
    return(0);
  }
  else
  {
    t=root;
    if (d < t->data)
    {
      if (t->left == NULL)
      {
        t->left = create_node(d);
        return (0);
      }
      root=t->left;
      insert_node(d);
    }
    else
    {
      if (t->right == NULL)
      {
        t->right = create_node(d);
        return(0);
      }
      root = t->right;
      insert_node(d);
    }
  root = sroot;
  }
}
void traverse(struct node * t)
{
  if (t != NULL)
  {    
    traverse(t->left);
    printf("%d ",t->data);    
    traverse(t->right);
  }
}
int main() 
{
  insert_node(12);
  insert_node(5);
  insert_node(14);
  insert_node(7);
  insert_node(6);
  insert_node(4);
  traverse(root);
  return 0;
}
18:11 10/13/202018:11 10/13/2020