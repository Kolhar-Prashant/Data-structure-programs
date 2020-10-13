#include<stdio.h>
#include<stdlib.h>

struct node
{
  int data;
  struct node * next;
}*head=NULL,*t,*temp,*prev;

struct node * create_node(int d)
{
    temp = malloc(sizeof(struct node));
    temp->data = d;
    temp->next = NULL;
    return temp;
}
void insert(int d)
{
    if (head == NULL)
    {
        head=create_node(d);
    }
    else
    {
        t=head;
        while (t->next != NULL)
        {
            t=t->next;
        }
        t->next=create_node(d);
    }
}
void remove_node(int d)
{
  t=head;
  if (t->data == d)
  {
    if (t->next != NULL)
    {
      head = t->next;
    }
    else
    {
      head=NULL;
    }
    return (0);
  }
  while (t->data != d)
  {
    prev = t;
    t=t->next;
  }
  prev ->next = t-> next;
}
void traverse()
{
    t=head;
    if (head == NULL)
    {
      printf("Linked list is empty !");
    }
    while (t != NULL)
    {
        printf("%d ",t->data);
        t=t->next;
    }
    printf("\n");
}
 
           
int main() {

  insert(11);
  insert(12);
  insert(13);  
  traverse();
  remove_node(13);
  traverse();
  insert(14);
  traverse();
  remove_node(12);
  traverse();
  insert(10);
  traverse();
  remove_node(11);
  traverse();
  return (0);
}            