package com.company;
public class merge_sort {
    public static void main(String[] args) {
       int A[]={1,2,5,6};
       int B[]={3,4,7};
       int []C=new int[A.length+B.length];
       int i=0,j=0,k=0;
       while(i<A.length&&j<A.length){
           if(A[i]<B[j]){
               C[k]=A[i];
               i++;k++;
           }
           else{
               C[k]=B[j];
               j++;k++;
           }
       }
       while (i<A.length){
           C[k]=A[i];
           i++;k++;
       }
       while(j<B.length){
           C[k]=B[j];
           j++;k++;
       }
       for(int item:C){
           System.out.print(item+" ");
       }

    }
}