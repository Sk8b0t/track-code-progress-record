package com.company;

import org.w3c.dom.ls.LSOutput;

import javax.crypto.spec.PSource;

public class sum_2 {
  int A[] = {1, 3, 6, 9, 2};
        int sum=9;
//short process to do the same thing
    void find() {
        for(int i=0;i<A.length;i++){
            for(int j=i+1;j<A.length;j++)
                if(A[i]+A[j]==sum)
                    System.out.printf("%d + %d = %d\n",A[i],A[j],sum);
        }
    }
    //long process to do the same thing...
    void find2(){
        for(int i=0;i<A.length;i++){
            for(int j=0;j<A.length;j++)
                if (A[i] + A[j] == sum && i != j)
                    System.out.printf("%d + %d = %d\n", A[i], A[j], sum);
        }
    }
    void noSemicolon(){
        String a="Hello World";
        //if(System.out.printf(a).equals(null)){
       System.out.println(System.out.printf(""));


        }

    public static void main(String[] args) {
        sum_2 a=new sum_2();
        System.out.println("By first process :");
        a.find();//short and easy process
        System.out.println("By second process :");
        a.find2();//long and difficult process
        a.noSemicolon();
    }
}