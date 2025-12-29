package com.company;
//Can also use import scanner,Random objects separately
import java.util.*;
class game{
    int num,num1;
    void getUserInput() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number : ");
        num = in.nextInt();
    }
    void getCompInput() {
        Random rand = new Random();
        num1 = rand.nextInt(100);
    }
    void isCorrectNumber(){
        if(num==num1){
            System.out.println("Your guess is correct...");
        }
        else if(num>num1){
            System.out.println("You guess is too big...");
        }
        else if(num<num1){
            System.out.println("Your gues is too low...");
        }

    }
}

public class guess_number {
    public static void main(String[] args) {
        game guess=new game();
        guess.getCompInput();
       boolean b=false;
     for(;b!=true;){
        guess.getUserInput();
        guess.isCorrectNumber();}                                                                                                                 /*

             OR
        while (!b){
            guess.getUserInput();
            guess.isCorrectNumber();
            }                                                                                                            */



    }
}
