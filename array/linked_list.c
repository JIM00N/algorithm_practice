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
    new_node->prev = *end;
    if (*head != NULL){
        (*end)->next = new_node;
    }
    else{
        *head = new_node;
    }
    *end = new_node;
}

void insertMiddle(node** head, int position, int data, node** end){
    node* new_node = (node*)malloc(sizeof(node));
    new_node->value = data;
    node* temp = *head;
    node* cur = *head;
    for (int i=0; i<(position); i++){
        cur = cur->next;
    }

    if (cur->prev == NULL || cur->next == NULL){
        if (cur->prev == NULL){insertFront(head, data, end);}
        else {insertBack(head, data, end);}
    }
    else
    {
        new_node -> prev = cur ->prev;
        new_node -> next = cur;
        cur->prev->next = new_node;
        cur->prev = new_node;
    }
    
}

void removeFront(node** head, node** end){
    if (*head==*end)
    {printf("nothing to delete");}
    else{
    node* temp = *head;
    (*head)->next->prev = NULL;
    (*head) = (*head)->next;
    free(temp);
    }
}

void removeBack(node** head, node** end){
    if (*end == *head){printf("nothing to delete");}
    else{
        node* temp = *end;
        (*end)->prev->next = NULL;
        (*end) = (*end)->prev;
        free(temp);
    }
}

void removeMiddle(node** head, int position, node** end){
    node* cur = *head;
    
    for (int i=0; i<(position-1); i++){
        cur = cur->next;
    }
    if (cur->prev == NULL)
    {
        removeFront(head, end);
    }
    else if (cur->next == NULL)
    {
        removeBack(head, end);
    }
    else
    {
    node* temp = cur->next;
    cur->next = cur->next->next;
    cur->next->prev = cur;
    free(temp);
    }
    
}

void swap1(node** head, int p1, int p2, node** end){
    node* a = *head;
    node* b = *head;
    for (size_t i = 0; i < p1; i++){a = a->next;}
    for (size_t i = 0; i < p2; i++){b = b->next;}
    int gap = p2 - p1;
    int a_val = a->value; // 밑에서 removeM하면 가르키던 값이 free되어버려 엉뚱한 결과가 나온다.
    int b_val = b->value; // 따라서 미리 저장해줘야한다.
    removeMiddle(head, p1, end);
    removeMiddle(head, p2, end);
    insertMiddle(head, p1, b_val, end);
    insertMiddle(head, p1 + gap, a_val, end);
}

void swap2(node** head, int p1, int p2, node** end){
    node* a = *head;
    node* b = *head;
    for (size_t i = 0; i < p1; i++){a = a->next;}
    for (size_t i = 0; i < p2; i++){b = b->next;}
    // step1 gap=1 or not
    node* tempA = (node*)malloc(sizeof(node));
    tempA->next = a->next;
    tempA->prev = a->prev;
    if ((p2-p1)!=1)
    {   
        if (a->prev==NULL)
        {   
            a->next->prev = b;
            b->prev->next = a;
            b->next->prev = a;
            a->prev = b->prev;
            a->next = b->next;
            b->prev = tempA->prev;
            b->next = tempA->next;
            *head = b;
        }
        else{
            a->prev->next = b;
            a->next->prev = b;
            b->prev->next = a;
            b->next->prev = a;

            a->next = b->next;
            a->prev = b->prev;
            b->next = tempA->next;
            b->prev = tempA->prev;
        }
    }
    else{
        if (a->prev==NULL){
            b->next->prev = a;
            b->prev = a->prev;
            a->prev = b;
            a->next = b->next;
            b->next = a;
            *head = b;
        }
        else{
            a->prev->next = b;
            b->next->prev = a;
            b->prev = a->prev;
            a->prev = b;
            a->next = b->next;
            b->next = a;
        }
    }   
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

    printf("Test insertMiddle 888\n");
    int position = 4;
    int value = 888;
    insertMiddle(&head, position, value, &end);
    printf("print insertMiddle result: ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");

    printf("Test removeFront\n");
    removeFront(&head, &end);
    printf("print removeFront : ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");

    printf("Test removeBack\n");
    removeBack(&head, &end);
    printf("print removeBack : ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");

    printf("Test removeMiddle\n");
    int idx = 3;
    removeMiddle(&head, idx,&end);
    printf("print removeMiddle : ");
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");

    printf("Test Swap1\n");
    int s1_idx1, s1_idx2;
    s1_idx1 = 0; s1_idx2 = 2;
    swap1(&head, s1_idx1, s1_idx2, &end);
    for (node* cur = head; cur != NULL; cur = cur->next)
    {
        printf("%d ", cur->value);
    }
    printf("\n");

    printf("Test Swap2\n");
        int s2_idx1, s2_idx2;
        s2_idx1 = 0; s2_idx2 = 2;
        swap2(&head, s2_idx1, s2_idx2, &end);
        for (node* cur = head; cur != NULL; cur = cur->next)
        {
            printf("%d ", cur->value);
        }
        printf("\n");

    return 0;
}
