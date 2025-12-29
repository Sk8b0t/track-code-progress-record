package com.company;

public class Main {
// method using static keyword
     static int sum(int x, int y)
    {
    int z;
    //x=6; Here the value gets changed,
        // as after changing the value the calculation is performed.
    z=x+y;
    x=6;//Here no change takes place because the change is made after performing the calculation.
        // if the value is changed here then no problem because, the calculation
        // is already done and changing is has no effect on the calculation performed!
    return z;
    }
    public static void main(String[] args) {
        int a=7,b=6,c;
        c=sum( a, b);
        System.out.println(c);

        //method using object
        /*
   int sum(int x,int y) {
        int z;
        z = x + y;
        return z;
    }
 public static void main(String[] args) {
        int a=6,b=7,c;
        Main obj=new Main();
        c=obj.sum(a,b);
        System.out.println(c);
        */


    }
}

