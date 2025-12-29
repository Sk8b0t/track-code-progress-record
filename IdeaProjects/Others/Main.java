package com.company;
import java.util.*;
/*class passenger{
    int PNR1;
    public int getPNR(){
    long a=100000000000L;
        PNR1=(int)((Math.random()*a)+1);
        return  PNR1;
    }
}*/

public class Main {

    public static void main(String[] args) {
	// write your code here
     Scanner in=new Scanner(System.in);
     int[]count=new int[10];
        long []PNR=new long[10];
        int t=0;
        String[]name=new String[10];

        for(int i=0;i< name.length;i++){
            System.out.println("Enter Your name :  ");
            name[i]=in.nextLine();
            System.out.println("Enter the type of coach you want ,(say sleeper class)");
            String type=in.nextLine();
            t++;
            if(t>0&&t<=72){
                System.out.println("seat is available ");
                System.out.println("Your coach number is : "+ type.charAt(0)+ t+1);
            }
long a=10000000000L;
            PNR[i]=(long)((Math.random()*a)+1);

            System.out.println("PNR : "+ PNR[i]);
        }
    }
}
