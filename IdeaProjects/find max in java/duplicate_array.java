package com.company;
import java.util.Scanner;
public class duplicate_array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an array of 10 elements: ");
        int[] A = new int[6];
        for (int i = 0; i < A.length; i++) {
            A[i] = sc.nextInt();
        }
        System.out.println("the duplicated element is : ");

        for (int i = 0; i < A.length; i++) {
            for (int j = i+1; j < A.length; j++) {
                if(A[j] == A[i]) {
                    System.out.print(A[j]+ "\t");
                    } }
        }

    }
}

