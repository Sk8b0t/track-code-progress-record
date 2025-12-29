package com.company;
import java.util.*;

public class Main {
    public static void load(){
        System.out.print("Loading");
        try {
            for (int i = 0; i < 8; i++) {
                Thread.sleep(269);
                System.out.print(".");
            }
            System.out.println();
        }
            catch(Exception e){
                System.out.println(e);
            }
    }
    public static void main(String PK[]) {

        //to find the middle string of a sentence (both with odd or even set of words)
        Scanner in = new Scanner((System.in));
        System.out.print("Enter a string : ");
        String n = in.nextLine();
        int t = 0, s = 0;char ch1=' ';
        for (int i = 0; i < n.length(); i++) {
            if (n.charAt(i) == ' ') {
                t++;
            }
        }

        int c = (t / 2);
        switch(c) {
            case 0:
                System.out.print("The middle word is : '");
                load();
                System.out.println(n.substring(n.indexOf(' '), n.lastIndexOf(' ') + 1)+"'");
                break;
        }
        if (t % 2 == 0) {
            for (int i = 0; i < n.length(); i++) {
                ch1 = n.charAt(i);
                if (ch1 == ' ') {
                    s++;
                    if (s == c) {
                        int a = n.indexOf(' ', i + 1);
                        load();
                        System.out.print("\nthe middle string is: '");
                        System.out.println(n.substring(i + 1, a + 1)+ "'");
                        break;
                    }
                }
            }
        }
        else if(t % 2!=0)
        {
            for(int i=0;i<n.length();i++){
                ch1=n.charAt(i);
                if(ch1==' ') {
                    s++;
                    if (s == c) {
                        int a = n.indexOf(' ', i + 1);
                        int b = n.indexOf(' ',a+1);
                        load();
                        System.out.println("\nThe middle string is : "+ "'" + n.substring(i + 1, b)+ "'");
                    break; }}}
        }

    }
}








