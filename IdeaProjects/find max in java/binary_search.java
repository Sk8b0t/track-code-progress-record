package com.company;
import java.util.Locale;
import java.util.Scanner;
public class binary_search {

        double m = 0.0d, len = 0.0d;
        static int i = 0, a = 0,n;
       static int[] A;
        boolean k = false;

   static void getInput() {

       Scanner in = new Scanner(System.in);
       System.out.println("How many numbers do you want to input : ");
      int input = in.nextInt();
        A= new int[input];
       for (int i = 0; i < A.length; i++) {
           System.out.printf("Enter the element %d ", i + 1);
           A[i] = in.nextInt();
       }
       System.out.println("Enter the number to be found : ");
        n = in.nextInt();
   }


 static void cal() {
     int low = 0, high = A.length - 1, mid = A.length / 2;
     boolean k = false;
     while (!k) {
         if (A[mid] == n) {
             System.out.println("Found");
             k = true;
             break;
         }
       else if (A[mid] < n) {
             low = mid+1;
             mid = (high + low) / 2;
         } else if (A[mid] > n) {
             high = mid-1;
             mid = (high + low) / 2;
         }
     }
 }


    public static void main(String[] args) {
        binary_search obj=new binary_search();
        getInput();
        cal();

    }
    }




