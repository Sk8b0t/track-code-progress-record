package com.company;
import java.util.Scanner;
public class name_selection_sort {

    int min=0;
    String c="";
    String[] A;

     void input() {
         Scanner in = new Scanner(System.in);
         System.out.print("How many numbers do you wanna input ?: ");
         int number = in.nextInt();
         A = new String[number];
         in.nextLine();

         for (int i = 0; i < number; i++) {
             System.out.printf("Enter name %d : ", i + 1);
             A[i] = in.nextLine();
         }
     }
     void calculate() {
         for (int i = 0; i < A.length; i++) {
             min = i;
             for (int j = i + 1; j < A.length; j++) {
                 if (A[min].compareTo(A[j]) > 0)
                     min = j;
             }
             c = A[i];
             A[i] = A[min];
             A[min] = c;
         }
     }
     void output() {
         for (String i : A) {
             System.out.println(i);
         }
     }
    public static void main(String[] args) {
        name_selection_sort obj=new name_selection_sort();
        obj.input();
        obj.calculate();
        obj.output();

    }
        }


