package com.company;
import java.util.*;
public class find_integer_in_array
{
    public static void main(String pk[])
            //find integer in a given array
    {
        Scanner in=new Scanner(System.in);
        System.out.print("Enter an integer which value is to be found in the array : ");
        int n=in.nextInt();int t=0;
        int A[]={45,56,55,78,23};
        for(int i=0;i<A.length;i++)
        {
            if(n==A[i]){
                t++;
                break; }
        }
        if(t==1)
            System.out.printf(" yes the integer %d is present in the array", n);
        else
            System.out.printf(" no  the integer %d is not present in the array", n);
        }


    }

