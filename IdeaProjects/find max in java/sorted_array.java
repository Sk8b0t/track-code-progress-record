package com.company;

public class sorted_array {
    public static void main(String Args[]) {
        int A[] = {87, 89, 54, 65, 42};
        int max=A[0];int t=0;
        for (int i =1; i<A.length; i++) {
            if (max < A[i]) {
                t++;
            }
        }
        if(t==A.length-1)
            System.out.println("sorted array");
        else
            System.out.println("not a sorted array");



    }
}


