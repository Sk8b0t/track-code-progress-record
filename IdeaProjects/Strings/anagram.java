package com.company;

import java.util.Objects;

public class anagram {
    public static void main(String[] args) {
        System.out.println("3");
     int p=0;
     for(int i=5;i<16;i+=2){
         p=i;
         for(int j=3;j<=i;j+=2){
             System.out.print(p+ " ");
             p++;
         }
         System.out.println();
         i=--p;
     }
        }

}