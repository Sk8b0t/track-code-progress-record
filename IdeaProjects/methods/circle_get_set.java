package com.company;
//This is how you can calculate area and perimeter of a circle by doing a circus by using -> getter and setter
import java.util.Scanner;
class circle{
    private int radius;
    private double area ;
    private double perimeter;

    public int getRadius(int r) {
        radius=r;
        return radius;
    }
    public void setArea(){
         area =3.14*radius*radius;
        System.out.println("area= "+ area+ "m");
    }

    public void setPerimeter() {
        perimeter=2*3.14*radius;
        System.out.println("perimeter = "+ perimeter+ "m");
    }
}

public class circle_get_set{
    public static void main(String[] args) {
       Scanner in=new Scanner(System.in);
        circle c=new circle();
        System.out.print("Enter the radius of the Circle(in metre) : ");
        int a= in.nextInt();
     c.getRadius(a);
       c.setPerimeter();
       c.setArea();

    }
}



   
