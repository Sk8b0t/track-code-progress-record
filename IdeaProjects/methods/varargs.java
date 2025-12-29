package com.company;

public class varargs {
    static int sum(int ...A)
    {
        //int []A; is written in the method as int...A

        // instead of repeating the method, create an array and do the calculation.
        // This method is called varArgs
        int t=0;
        for(int i=0;i<A.length;i++)
        {
            t+=A[i];
        }
        return t;
    }

    public static void main(String[] args) {
        System.out.println("sum= "+sum(4,5,6)); //because the method is an array. So, we can input how many numbers we want.
        System.out.println("sum = "+sum(4,5,6,5,6,7,8,9,8,9,66,5));
    }


    }
