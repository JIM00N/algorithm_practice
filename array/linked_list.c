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
    if (*end != NULL)
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

void insertBack(node** head, int data, node** end){
    node* new_node = (node*)malloc(sizeof(node));
    new_node->value = data;
    new_node->next = NULL;
    if (*head != NULL){
        (*end)->next = new_node;
    }
    else{
        *head = new_node;
    }
    *end = new_node;
}

int main() {
    
    node *head = NULL;
    
    // create a pointer to end node
    node *end = NULL;
    
    // call the insert_at_front function four times
    printf("Test insertFront 1->2->3->4\n");
    insertFront(&head, 1, &end);
    insertFront(&head, 2, &end);
    insertFront(&head, 3, &end);
    insertFront(&head, 4, &end);
    
    // // print the list in forward direction
    printf("print insertFront result: ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");
    
    printf("Test insertBack 1->2->3->4\n");
    insertBack(&head, 1, &end);
    insertBack(&head, 2, &end);
    insertBack(&head, 3, &end);
    insertBack(&head, 4, &end);
    printf("print insertBack result: ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");
    return 0;
}