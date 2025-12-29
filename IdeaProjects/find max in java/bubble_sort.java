package com.company;
import java.util.Scanner;
public class bubble_sort
{
        Scanner in=   new Scanner(System.in);
        int c=0,input=0;
        int[]A;
    public void input() {
        System.out.println("How many numbers do you want to input : ");
        input = in.nextInt();
        if (input == 1)
            System.out.println("Enter the number: ");
         else
            System.out.printf("Enter %d number(s) : ", input);

        A =new int[input];
    }
    public void calculate() {
        for (int i = 0; i < A.length; i++) {
            A[i] = in.nextInt();
        }
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length - (i + 1); j++) {
                if (A[j] > A[j + 1]) {
                    c = A[j];
                    A[j] = A[j + 1];
                    A[j + 1] = c;}}}
    }

    void output() {
        System.out.println("Sequence in Ascending order is/are given below : ");
        for (int element : A) {
            System.out.println(element);
        }
    }
    public static void main(String[] args) {
        bubble_sort a=new bubble_sort();
        a.input();
        a.calculate();
        a.output();
    }
}
