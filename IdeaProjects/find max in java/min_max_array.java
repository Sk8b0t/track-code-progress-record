package com.company;
import java.util.*;
public class min_max_array {
//to find maximum and minimum in arrays

    public static void main(String args[]) {
        Scanner in=new Scanner(System.in);
        System.out.print("Enter a number : ");
        int A[] = new int[10];int max = 0,min=0;
        int i = 0;
        while (i <10) {
            A[i] = in.nextInt();
            i++;
        }
        i=0;max=A[0]; min=A[0];

        while(i<10){

            if(max<A[i])
            {
                max=A[i];}
            i++;
        }
        System.out.println("max= "+max);
        i=0;
        while(i<10){
            if(min>A[i])
            {
                min=A[i];
            }i++;
        }
        System.out.println("min= "+ min);
    }
}


