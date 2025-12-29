package com.company;

import java.util.Scanner;

public class secondMax {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        System.out.println("How many terms do you wanna input :");
        int input=in.nextInt();
        int[]A=new int[input];
        System.out.printf("Enter %d numbers : ",input);
        for (int i=0;i<A.length;i++){
            A[i]=in.nextInt();
        }
        int max=A[0],smax=A[0];
        for (int i=0;i<A.length;i++){
            if(A[i]>max){
                max=A[i];
            }
        }
        for(int i=0;i<A.length;i++){
            if(A[i]==max){
                continue;
            }
            else if(A[i]>smax){
               smax=A[i];
            }
        }
        System.out.println("Second max= "+smax);
    }
}
