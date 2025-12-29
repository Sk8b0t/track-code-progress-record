
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int item;
    struct Node *next;
};

void show(struct Node *ptr) {
    printf("The elements of the linked list are:\n");
    while (ptr != NULL) {
        printf("%d\n",ptr->item);
        ptr=ptr->next;
    }
}
struct Node *addAtStart(struct Node *head,int data) {
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->item = data;
    ptr->next = head;
    head=ptr;
    return head;

}
void addAtIndex(struct Node *head,int data,int ind) {
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = (struct Node *)malloc(sizeof(struct Node));
    p=head;
    ptr->item = data;
    int i=0;
    while (i!=ind-1) {
        p=p->next;
        i++;
    }
    ptr->next=p->next;
    p->next=ptr;


}
void addAfterNode(struct Node *prev,int data) {
    struct Node *newnode = (struct Node *)malloc(sizeof(struct Node));
    newnode->item=data;
    newnode->next=prev->next;
    prev->next=newnode;

}
void addAtEnd(struct Node *head,int data) {
    struct Node* ptr=(struct Node *)malloc(sizeof(struct Node));
    struct Node* p=(struct Node *)malloc(sizeof(struct Node));
    ptr->item=data;
    p=head;
    while (p->next != NULL) {
        p=p->next;
    }
    p->next=ptr;
    ptr->next=NULL;


}
int main() {
    //memory allocation
    struct Node *head =(struct Node *)malloc(sizeof(struct Node));
    struct Node *first =(struct Node *)malloc(sizeof(struct Node));
    struct Node *sec =(struct Node *)malloc(sizeof(struct Node));
    struct Node *thrd =(struct Node *)malloc(sizeof(struct Node));

    //starting of a linked list
    head->item=12;
    head->next=first;
    first->item=13;
    first->next=sec;
    sec->item=14;
    sec->next=thrd;
    thrd->item=15;
    thrd->next=NULL;

    //operations
    printf("before:");
    show(head);

    // //adding after a node
    printf("after:");
    addAfterNode(sec,69);
    show(head);

    //adding at start
    printf("after:\nsuccessfully added at start:\n");
    head=addAtStart(head,69);
    show(head);

    //adding at a given index
    printf("after:\nsuccessfully added at start:\n");
    addAtIndex(head,69,1);
    show(head);

    //adding index at the end of the node
    printf("after:\nsuccessfully added at end:\n");
    addAtEnd(head,69);
    show(head);






    //freeing all the allocated memory
    free(head);
    free(first);
    free(sec);
    free(thrd);

    return 0;
}
