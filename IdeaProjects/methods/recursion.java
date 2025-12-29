package com.company;

public class recursion {
    int fact(int n){
        if(n==1 || n==0)
            return 1;
        else
          return n*fact(n-1);//how ??
    }

    public static void main(String[] args) {
        int n=5;
        recursion ob=new recursion();
        System.out.println("sum= "+ob.fact(n));
        int a=2,b=3,c=9;
        int x=a*(++b)%c;
        System.out.println(2*4%9*3);
    }
}
