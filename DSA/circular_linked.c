#include <stdio.h>
#include<stdlib.h>
struct node{
    int item;
    struct node* nxt;
};
void dis(struct node* head){
    struct node *ptr=head;
    printf("The elements are:\n");
    do{
        printf(" %d\n",ptr->item);
        ptr=ptr->nxt;
        
    }while(ptr!=head);

}
struct node* InsertAtFirst(struct node* head, int item){
    struct node* ptr=(struct node*)malloc(sizeof(struct node));
    struct node* p=head->nxt;
    ptr->item=item;
    while(p->nxt!=head){
        p=p->nxt;
    }
    p->nxt=ptr;
    ptr->nxt=head;
    return ptr;

}


 int main() {
    //memory allocation
    struct node *head =(struct node *)malloc(sizeof(struct node));
    struct node *first =(struct node *)malloc(sizeof(struct node));
    struct node *sec =(struct node *)malloc(sizeof(struct node));
    struct node *thrd =(struct node *)malloc(sizeof(struct node));

    //starting of a linked list
    head->item=12;
    head->nxt=first;
    first->item=13;
    first->nxt=sec;
    sec->item=14;
    sec->nxt=thrd;
    thrd->item=15;
    thrd->nxt=head;
    printf("before\n");
    dis(head);
    printf("After:\n");
    head=InsertAtFirst(head,69);
    dis(head);


    return 0;
}