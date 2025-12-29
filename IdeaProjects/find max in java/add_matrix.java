package com.company;
import java.util.*;
public class add_matrix {

    public static void main(String sk[]) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int row=in.nextInt();
        System.out.println("Enter the number of columns");
        int column=in.nextInt();
        int[][] A = new int[row][column];
        int[][] B = new int[row][column];
        int sum = 0;

        System.out.println("For 1st matrix\nenter the elements of 1st row : ");

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
                if(i==0){
                A[i][j] = in.nextInt(); }
                if(i==1) {
                    System.out.printf("enter the %d value elements of 2nd row : ",j+1);
                     A[i][j] = in.nextInt();}

            }
        }
        System.out.println("for 2nd matrix\nenter elements of 1st row ");

        for (int i = 0; i < B.length; i++) {
            for (int j = 0; j < B[i].length; j++) {
                if(i==0){
                B[i][j] = in.nextInt();}
                if(i>=1){
                    System.out.printf("enter the %d elements of 2nd row : ",j+1);
                B[i][j] = in.nextInt();}
            }
        }
       
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
            sum=A[i][j]+B[i][j];
                System.out.print(sum+"\t");
                }
            System.out.print("\n");
            }

    }
}










