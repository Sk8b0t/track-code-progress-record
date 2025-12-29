package com.company;
import java.util.Scanner;
public class remove_dupicate {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int[]A=new int[6];
        System.out.println("Enter the array : ");
          for(int i=0;i<A.length;i++)
              A[i]=in.nextInt();

 for(int i=0;i<A.length-1;i++) {
     for (int j = i + 1; j < A.length; j++) {
         if (A[i] == A[j])
             A[j] = 0;
     }
 }
        System.out.println("New array after removing duplicates");
        for(int i:A){
            if(i==0)
                continue;
            else
                System.out.println(i);
        }

    }
}
