#include<stdio.h>
#include<stdlib.h> //malloc()

struct node
{
  int data;
  struct node *next;
}*temp ,*head, *trav, *t, *prev;

struct node * create_node (int d)
{
  temp = malloc(sizeof(struct node));
  temp -> data = d;
  temp -> next = NULL;
  return temp;
}

void insert_at_end(int d)
{ 
  if (head == NULL)
  {
    head = create_node(d);
  }
  else
  {
    trav = head;
    
    while (trav -> next != NULL)
    {
      trav = trav -> next;
    }
    temp = create_node(d);
    trav -> next = temp;
  }
}

void insert_in_middle(int d)
{
  int pos = 2;
  int cnt = 0;

  trav = head;
  prev = trav;
  
  while (cnt != pos)
  {
    prev = trav;
    trav = trav -> next;
    cnt ++;
  }
  
  temp = create_node(d);

  if (pos == 0)
  {
    temp ->next = head;
    head = temp;
    return 0;
  }

  if (trav -> next != NULL)
  {
    prev -> next = temp;
    temp -> next = trav;
  }
  else
  {
    trav -> next = temp;
  }
}

void remove_node(int d)
{
  trav = head;
  prev = head;
  while (trav -> data != d)
  {
    prev = trav;
    trav = trav -> next;
  }
  if (trav == head)
  {
    head = head -> next;
    return (0);
  }
  if (trav -> next != NULL)
  {
    prev -> next = trav -> next;
  }
  else
  {
    prev -> next = NULL;
  }
}
  

void traverse()
{
  trav = head;
  
  while (trav != NULL)
  {
    printf(" %d",trav->data);
    trav = trav -> next;
  }
}
      
    
int main() {
  
  insert_at_end(10);
  insert_at_end(12);
  insert_at_end(13);
  insert_in_middle(14);
  remove_node(13);
  remove_node(10);
  traverse();

  return 0;
}
