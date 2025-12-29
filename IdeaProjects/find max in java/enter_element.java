package com.company;
import java.util.Scanner;
public class enter_element {
    int[] A;
    Scanner sayan = new Scanner(System.in);

    void getInput() {
        System.out.println("Enter the number of elements of the array :");
        int input = sayan.nextInt();
        A = new int[input+1];
        for (int i = 0; i < A.length-1; i++) {
            System.out.printf("Enter the element no. %d : ", i + 1);
            A[i] = sayan.nextInt();
        }
    }

    int element = 0, index = 0;

    void askDetails() {
        System.out.print("\nEnter the element to be inserted : ");
        element = sayan.nextInt();
        System.out.println("Enter the index no. :");
        index = sayan.nextInt();
    }
    int c=0;
    void calculate() {
        for (int i = A.length - 2; i >= 0; i--) {
            if (i >= index) {
                c = A[i];
                A[i] = A[i+1];
                A[i+1] = c;

            }
        }
        A[index] = element;
    }
    void newArray() {
        System.out.println("The new array is : ");
        for (int item : A) {
            System.out.println(item);
        }
    }

    public static void main(String[] args) {
        enter_element s = new enter_element();
        s.getInput();
        s.askDetails();
        s.calculate();
        s.newArray();
    }
}




