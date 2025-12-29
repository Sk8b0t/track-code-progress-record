package com.company;
import java.util.*;


class game {

    int num,num1;

    public void getUserInput() {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number between 1 to 100 : ");
        num = in.nextInt();
    }
    public void getCompInput() {
      num1=(int)((Math.random()*100)+1);
    }
  public void isCorrectNumber(){
        if(num==num1){
            System.out.println("Your guess is correct...");
            System.out.println("Play another round....!!!");

        }
        else if(num>num1){
            System.out.println("You guess is too big...");
        }
        else {
            System.out.println("Your guess is too low...");
        }

    }
}

public class guess_the_number {
    public static void main(String[] args) {
        game guess=new game();
        guess.getCompInput();
        boolean b=false;
        while (b!=true){
            guess.getUserInput();
            guess.isCorrectNumber();
            }



    }
}
