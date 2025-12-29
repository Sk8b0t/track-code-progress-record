package com.company;

import java.util.Scanner;
public class err {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);

        String[] A = new String[6];
        System.out.println("Enter 6 numbers :");
         for(int i=0;i<A.length;i++) {
             A[i]=in.nextLine();
         }
        //String[]B=new String[A.length];
        for(int i=0;i<A.length;i++) {
            for (int j = i + 1; j < A.length; j++) {
                if (A[i].equals(A[j]))
                    A[j] ="";
            }
        }
        for(String i:A)
            if(i.equals(""))
                continue;
            else
                System.out.print(i+" ");



        }
        }





