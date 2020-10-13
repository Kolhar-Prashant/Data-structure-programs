#include<stdio.h>
#include<stdlib.h>

struct node 
{
  int data;
  struct node *next;
}*start=NULL,*temp,*t,*prev;

struct node * create_node(int d)
{
  temp = malloc (sizeof(struct node));
  temp -> data = d;
  temp -> next = NULL;
  return temp;
}

void insert(int d)
{
  if (start == NULL)
  {
    start = create_node(d);
  }
  else
  {
    t=start;
    prev = t;
    if (d < t->data)
    {
      t=create_node(d);
      t->next=prev;    
      start=t;
      return (0);
    }
      
    while (t->data < d)
    {
      prev = t;
      if (t->next != NULL)
      {
        t=t->next;      
      }
      else
      {
        t->next=create_node(d);
        return(0);
      }
    }
    t = prev;
    prev = t->next;
    t->next = create_node(d);
    t=t->next;
    t->next = prev;
  }
}

void traverse()
{
  t=start;
  while (t != NULL)
  {
    printf("%d ",t->data);
    t=t->next;
  }
}

int main() {

  insert(10);
  insert(14);
  insert(12);
  insert(8);
  insert(15);
  insert(55);
  insert(3);
  insert(13);
  insert(-1);
  insert(100);
  traverse();
  
  return 0;
}