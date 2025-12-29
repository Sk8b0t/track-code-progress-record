package com.company;

import java.util.Scanner;

class NegativeRadiusException extends Exception {
    @Override
    public String toString() {
        return "The radius is negative ";
    }

    @Override
    public String getMessage() {
        return "The radius is negative ";
    }
    public static double area(double r) throws NegativeRadiusException{
        if(r<0)
            throw new NegativeRadiusException();
        double result=Math.PI*r*r;
        return result;
    }
}

public class throw_throws {
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the radius of the circle (in metre) : ");
        double radius=in.nextDouble();
        NegativeRadiusException n=new NegativeRadiusException();
                try{
            double area=n.area(radius);
            System.out.println("Area of the circle : "+area+ " metre square");
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}
