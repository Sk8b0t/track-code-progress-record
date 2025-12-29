
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

struct Node* delAtStart(struct Node * head){
    struct Node* ptr=head;
    ptr=head->next;
    free(head);
    return ptr;

}

void delAtIndex(struct Node* head, int idx){
  struct Node * a=head;     
  struct Node * b=head->next;
  for (int i = 0; i < idx-1; i++)
  {
    a=a->next;
    b=b->next;
  }
a->next=b->next;
free(b);
  
    
}
void delAtNode(struct Node* head, struct Node* toDel){
    struct Node* a=head;
    struct Node* b=head->next;
    while(b!=toDel){
        a=a->next;
        b=b->next;
    }
         a->next=b->next;
         free(b);
        
}
 void delAtEnd(struct Node* head){
    struct Node* a= head;
    struct Node* b=head->next;
    while(b->next!=NULL){
        a=a->next;
        b=b->next;
    }
    a->next=NULL;
    free(b);

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
    


    //deleting the start of the linked list
    // printf("\nafter deleting head node:");
    // head=delAtStart(head);
    // show(head)
    printf("before:");
    show(head);

    //deleting at an index
    // printf("After deleting from the index:");
    // delAtIndex(head,2);
    // show(head);

    //deleting at the end
    // delAtEnd(head);
    // show(head);
  
    //deleting from a specific node 
    delAtNode(head,sec);
    show(head);

    // //operations
    // printf("before:");
    // show(head);

    // // //adding after a node
    // printf("after:");
    // addAfterNode(sec,69);
    // show(head);

    // //adding at start
    // printf("after:\nsuccessfully added at start:\n");
    // head=addAtStart(head,69);
    // show(head);

    // //adding at a given index
    // printf("after:\nsuccessfully added at start:\n");
    // addAtIndex(head,69,1);
    // show(head);

    // //adding index at the end of the node
    // printf("after:\nsuccessfully added at end:\n");
    // addAtEnd(head,69);
    // show(head);






    //freeing all the allocated memory
    free(head);
    free(first);
    free(sec);
    free(thrd);

    return 0;
}
