package com.company;
import java.util.Scanner;
public class selection_sort {
    Scanner in=new Scanner(System.in);
    int n=0,A[];
    void input(){
        System.out.println("How many terms do you want to enter : ");
        n=in.nextInt();
        A=new int[n];
        System.out.println("Enter the elements :");
        for(int i=0;i<A.length;i++){
            A[i]=in.nextInt();
        }
    }
    int min=0,c=0;
    void calculate(){
        for(int i=0;i<A.length;i++){
            min=i;
            for (int j=i+1;j<A.length;j++) {
                if (A[min] > A[j])
                    min = j;
            }
            c=A[i];
            A[i]=A[min];
            A[min]=c;
            }
        }
        void output(){
        for(int element:A){
            System.out.println(element);
        }
    }

    public static void main(String[] args) {
        selection_sort obj=new selection_sort();
        obj.input();
        obj.calculate();
        obj.output();
    }
}
