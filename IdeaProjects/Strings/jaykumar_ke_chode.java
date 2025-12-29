package com.company;

import java.util.Scanner;

public class jaykumar_ke_chode {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);

        System.out.print("Enter a string : ");
        String name=in.nextLine();
         name=" "+name;

        String first=name.substring(0,name.lastIndexOf(' ')),
        second=name.substring(name.lastIndexOf(' ')+1);


        for(int i=0;i<first.length();i++) {
            char ch = first.charAt(i);
            if (ch == ' ')
                System.out.print(first.charAt(i + 1)+" ");
        }
        System.out.println(second);

        }
    }

