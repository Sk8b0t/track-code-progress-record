package com.company;
import java.util.InputMismatchException;
import java.util.Scanner;
class MyException extends Exception {
    @Override
    public String toString() {
        return "I am toString() method";
    }

    public String getMessage() {
        return "I am getMessage()";
    }
}

public class custom_exception {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int input = in.nextInt();
        if (input > -1) {
            try {
                throw new MyException();
            } catch (Exception e) {
                System.out.println(e.toString());
                System.out.println(e.getMessage());
                e.printStackTrace();
            }


        }
    }
}

