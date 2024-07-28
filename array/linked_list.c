#include <stdio.h>
#include <stdlib.h>

// structure to define a node of the doubly linked list
typedef struct node{
    node* prev;
    int value;
    node* next;
}node;

// // function to insert a new node with given data in the front of the doubly linked list
void insertFront(node** head, int data, node** end){
    // 1. new node 
    node* new_node = (node*) malloc(sizeof(node));
    new_node-> value = data;
    // 2. set previous to Null
    new_node->prev = NULL;
    // 3. set next to point to head node
    new_node->next = *head;
    // 4. set previous of crrent head to new node
    if (*head != NULL)
    {
        (*head)->prev = new_node;
    }
    else
    {
        *end = new_node;
    }
    
    // 5. set head node reference to new node
    *head = new_node;
}

int main() {
    
    node *head = NULL;
    
    // create a pointer to end node
    node *end = NULL;
    
    // call the insert_at_front function four times
    insertFront(&head, 1, &end);
    insertFront(&head, 2, &end);
    insertFront(&head, 3, &end);
    insertFront(&head, 4, &end);
    
    // // print the list in forward direction
    
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d\n", cur->value);
    }
    
    
    return 0;
}