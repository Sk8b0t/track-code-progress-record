package com.company;

import java.util.Scanner;

public class try_catch {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int id[]=new int [5];
        for(int i=0;i<id.length;i++) {
            id[i] = (i + 1) * 10;

        }
        boolean k=false;
        while(!k){
            System.out.println("Enter the index :");
            try {
                int a = in.nextInt();
                System.out.println(id[a] + " is the element");
                k=true;
            }
            catch (ArrayIndexOutOfBoundsException e){
                System.out.println("Index not available \n");
            }

        }
        for(int i:id)
            System.out.print(i+"\t");
    }
}
