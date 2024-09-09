#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node{
    struct node* prev;
    int value;
    struct node* next;
}node;

void push(node** head, int element, node** end){
    node* new_node = (node*)malloc(sizeof(node));
    new_node->value = element;
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

int pop(node** head, node** end){
    node* temp = *end;
    int val;
    if (*head==*end && *end==NULL) {printf("This queque is empty.");}

    else if (*head==*end && *end!=NULL)
    {
        val = (*end)->value;
        *head = NULL;
        *end = NULL;
        free(temp);
    }

    else{
        val = (*end)->value;
        (*end)->prev->next = NULL;
        (*end) = (*end)->prev;
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

    printf("Push : 1~5\n");
    for (int i = 1; i < 6; i++)
    {push(&head, i, &end);}

    printf("Pop : Three Values\n");
    for (int i = 1; i < 4; i++)
    {int poop = pop(&head, &end);
        printf("pop %d\n", poop);}

    printf("the size of this stack : %d\n", size(&head, &end));

    printf("This stack is empty: %d (0:False, 1:True)\n", isEmpty(&head, &end));
    showAll(&head, &end);

    printf("Pop : Last Two Values\n");
    printf("pop : %d\n", pop(&head, &end));
    printf("pop : %d\n", pop(&head, &end));

    printf("the size of this stack : %d\n", size(&head, &end));

    printf("This stack is empty: %d (0:False, 1:True)\n", isEmpty(&head, &end));
    return 0;
}
