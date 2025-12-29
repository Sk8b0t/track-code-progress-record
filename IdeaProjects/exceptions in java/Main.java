package com.company;

import java.util.InputMismatchException;

public class Main {

    public static void main(String[] args) {


	java.util.Scanner in=new java.util.Scanner(System.in);

        int arr[]={1,4,5,7,8,5,4,3334,55,4};
        boolean k=true;
        while(k=true) {
            try {
                  System.out.println("Enter the array index : ");
                int index = in.nextInt();
                System.out.printf("Array index %d : %d\n", index, arr[index]);
                k=false;
                break;
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Array index not found");
            }
             catch (InputMismatchException e) {
                System.out.println("Wrong input");
            }
            in.nextLine(); //<- clears the buffer
        }
    }
}
