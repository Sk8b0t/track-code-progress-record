package com.company;
import java.util.Scanner;
class base{
    int x;
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public base(int x) {
        System.out.println("The value of x is: " + x);
    }}
class derived extends base {
    int y;

    public derived(int x, int y) {
        super(x);
        System.out.println("The Value of y is : " + y);
    }
}
class childOfDerived extends derived {
    int z;

    public childOfDerived(int x, int y, int z) {
        super(x, y);
        System.out.println("The value of z is : " + z);
    }
}
public class inheritance
{
    public static void main(String[] args) {
       Scanner in=new Scanner(System.in);
 /*      System.out.println("");
        System.out.println("Enter the value of x : ");
       int a=in.nextInt();
        System.out.println("Enter the value of y : ");
        int b=in.nextInt();
        System.out.println("enter the value of Z : ");
        int c=in.nextInt();*/
        System.out.print("Enter the value of x,y and z : ");
        childOfDerived d=new childOfDerived(in.nextInt(),in.nextInt(),in.nextInt());




    }
}
