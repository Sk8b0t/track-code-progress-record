package com.company;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>(5);
       Scanner in=new Scanner(System.in);
        System.out.println("Enter the numbers: ");
        for (int i = 0; i <5; i++) {
            a.add(in.nextInt());
            in.nextLine();
        }
        for(int i:a)
            System.out.print(i+" ");

    }
}

