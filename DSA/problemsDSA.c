#include <stdio.h>
#include <stdlib.h>

struct node{
    int item;
    struct node * nxt;
};

void countNodes(struct node * head ){
    struct node* a=head;
    int i=0;
    while(a->nxt!=NULL){
        a=a->nxt;
        i++;
    }
    printf("total nodes in this linked list are: %d\n",i+1);
}

int searchItem(struct node * head, int data){
    struct node* a=head;
    int cnt=0;
    while(a->nxt!=NULL){
        if (a->item==data){
            cnt=1;
            return 1; //indicates the data is found in the linked list
        }
        a=a->nxt;
    }
    if (cnt==0){
        return 0; //indicates the data is not found in the linked list
    }
 return 0;
}


int main()
{
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
    thrd->nxt=NULL;
    countNodes(head);
    if (searchItem(head,18) ==0){
        printf("item not found ");

    }
    else{
        printf("Item found");
    }



   return 0; 
}
