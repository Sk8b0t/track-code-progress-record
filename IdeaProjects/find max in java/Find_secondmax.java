package com.company;

import java.util.Scanner;

public class Find_secondmax {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("How many terms do you wanna input :");
        int input = in.nextInt();
        int[] A = new int[input];
        System.out.printf("Enter %d numbers : ", input);
        for (int i = 0; i < A.length; i++) {
            A[i] = in.nextInt();
        }
        int c = 0;
        int min=0;
                for (int i = 0; i < A.length; i++) {
                    min = i;
                    for (int j =i+1; j < A.length; j++) {
                        if (A[min] > A[j])
                            min = j;
                    }
                    c = A[i];
                    A[i] = A[min];
                    A[min] =c;
                }
        int max=A[0],smax=A[0];
        for (int i=0;i<A.length;i++){
            if(A[i]>max){
                max=A[i]; }
        }

        for(int i=0;i<A.length;i++) {
            if(A[i]>smax&&A[i]<max)
                smax=A[i];
        }
        System.out.println("Second max= "+smax);
        System.out.print("Numbers in descending orders : \n");
        for(int i:A)
        System.out.print(i+ "\n");
    }
}
