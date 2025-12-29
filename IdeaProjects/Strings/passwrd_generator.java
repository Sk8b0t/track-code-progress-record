package com.company;

//import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class passwrd_generator {
    static String passGenerate(int len){
        String lower="abcdefghhijklmnopqrstuvwxyz33";
        String upper=lower.toUpperCase();
        String digits="0123456789",symbols="<>?/()&*!@#$%^{}[]_\\|.__\"";
        String combo=lower+symbols+digits+upper;
//        for(int i=64;i<91;i++)
//            combo+=(char)i;
//        combo+="0123__456789\\/|>/<|";
        Random r=new Random();
        String password="";
        for(int i=0;i<len;i++)
            password+=combo.charAt(r.nextInt(combo.length()-1));

        return password;
    }


    public static void main(String[] args) {
        Main m=new Main();
        Scanner in=new Scanner(System.in);
        System.out.print("\u001B[40m"+"\u001B[32m"+"Enter the length of the passoword :");
        int len=in.nextInt();
        //m.load();
        System.out.println("Your password is : "+"\u001B[31m"+passGenerate(len));
    }
}
