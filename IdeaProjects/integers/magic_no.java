package com.company;

public class magic_no {
    int sum=0,count =0;
     String green="\u001B[32m";
   void magic(int n){
        int r;
        for(int i=n;i>0;i=i/10) {
            r = i % 10;
            count++;
            sum += r;}

        }

        void check() {
            boolean k = false;
            int t = sum;

            while (!k) {
                if (sum == 1) {
                    k = true;
                    System.out.println("Magic number");}

                else {
                    if (count==1) {
                        System.out.println(green+"not a magic number ");
                        break;
                    } else {
                        t = sum;
                        sum = 0;
                        count=0;
                        magic(t);}}}
        }

    public static void main(String[] args) {
        magic_no magic=new magic_no();
        int num=23;


        if(num==0){
            // System.out.print("\u001B[31m");
            System.out.println("Not a magic number ");
        }
        magic.magic(num);
        magic.check();
    }
}
