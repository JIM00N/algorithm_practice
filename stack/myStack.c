#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    node* prev;
    int value;
    node* next;
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

void pop(node** head, node** end){
    node* temp = *end;
    if (*head==*end && *end==NULL) {printf("This queque is empty.");}

    else if (*head==*end && *end!=NULL)
    {
        printf("%d\n", (*end)->value);
        *head = NULL;
        *end = NULL;
        free(temp);
    }

    else{
        printf("%d\n", (*end)->value);
        (*end)->prev->next = NULL;
        (*end) = (*end)->prev;
        free(temp);
    }
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

void size(node** head, node** end){
    int size_count = 0;
    node* cur = NULL;
    while (cur!=*end)
    {
        if (cur==NULL){cur = *head;}
        else {cur = cur->next;}
        size_count += 1;
    }
    printf("the size of this stack is %d\n", size_count);
}

void isEmpty(node** head, node** end){
    if (*head==*end && *head==NULL)
    {printf("This stack is empty = true\n");}
    else
    {printf("This stack is empty = false\n");}
}

int main(){
    node* head = NULL;
    node* end = NULL;

    printf("Push : 1~5\n");
    for (int i = 1; i < 6; i++)
    {push(&head, i, &end);}

    printf("Pop : Three Values\n");
    for (int i = 1; i < 4; i++)
    {pop(&head, &end);}

    size(&head, &end);

    isEmpty(&head, &end);

    showAll(&head, &end);

    printf("Pop : Last Two Values\n");
    pop(&head, &end);
    pop(&head, &end);

    size(&head, &end);

    isEmpty(&head, &end);
    return 0;
}