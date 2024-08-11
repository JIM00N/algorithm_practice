#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node{
    node* prev;
    int value;
    node* next;
}node;

void enqueue(node** head, int data, node** end){
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

int dequeue(node** head, node** end){
    node* temp = *head;
    int val;
    if (*head==*end && *head==NULL) {printf("This queque is empty.");}

    else if (*head==*end && *head!=NULL)
    {
        val = (*head)->value;
        *head = NULL;
        *end = NULL;
        free(temp);
    }
    
    else{
        val = (*head)->value;
        (*head)->next->prev = NULL;
        (*head) = (*head)->next;
        free(temp);
    }

    return val;
}

void showAll(node** head, node** end){
    node* cur = *head;
    printf("all remaining elements in this queue : \n");
    
    while (cur!=NULL)
    {   
        printf("%d ", cur->value);
        cur = cur->next;
    }
    printf("\n");
}

int size(node** head, node** end){
    int size_count = 0;
    node* cur = NULL;
    while (cur!=*end)
    {
        if (cur==NULL){cur = *head;}
        else {cur = cur->next;}
        size_count += 1;
    }
    return size_count;
}

int isEmpty(node** head, node** end){
    if (*head==*end && *head==NULL)
    {return true;}
    else
    {return false;}
}

int main(){
    node* head = NULL;
    node* end = NULL;
    
    printf("Enqueue : 1~5\n");
    for (int i = 1; i < 6; i++)
    {enqueue(&head, i, &end);}

    printf("Dequeue : Three Values\n");
    for (int i = 1; i < 4; i++)
    {
        int deq = dequeue(&head, &end);
        printf("dequeue %d\n", deq);
    }

    printf("the size of this queue is %d\n", size(&head, &end));

    printf("This queue is empty: %d (0:False, 1:True)\n", isEmpty(&head, &end));
    
    showAll(&head, &end);

    printf("Dequeue : Last Two Values\n");
    printf("dequeue %d\n", dequeue(&head, &end));
    printf("dequeue %d\n", dequeue(&head, &end));

    printf("the size of this queue is %d\n", size(&head, &end));
    printf("This queue is empty: %d (0:False, 1:True)\n", isEmpty(&head, &end));
    return 0;
}
