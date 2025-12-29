package com.company;
import java.util.Scanner;
class game1 {

    //1-rock
    //2-paper
    //3-scissors
    int yourChoice, computerChoice;

    void getInput() {
        Scanner in = new Scanner(System.in);
        yourChoice = in.nextInt();
        System.out.println();
    }

    void getCompInput() {
        computerChoice = (int) ((Math.random() * 3) + 1);
        //Starting the calculations
    }

    void getCorrectAnswer() {
        if (computerChoice == yourChoice) {
            System.out.println("Draw");
        }
        if (yourChoice >= 0 && yourChoice <= 3 && computerChoice != yourChoice) {
            if (computerChoice == 1 && yourChoice == 3 || computerChoice == 2 && yourChoice == 1 || computerChoice == 3 && yourChoice == 2) {
                System.out.println("Computer wins");
                if (computerChoice == 1) {
                    System.out.println("computer's choice was Rock");
                }
                if (computerChoice == 2) {
                    System.out.println("Computer's choice was Paper");
                }
                if (computerChoice == 3) {
                    System.out.println("Computer's choice was Scissors");
                }
            } else {
                System.out.println("You win");
                if (computerChoice == 1) {
                    System.out.println("computer's choice was Rock");
                }
                if (computerChoice == 2) {
                    System.out.println("Computer's choice was Paper");
                }
                if (computerChoice == 3) {
                    System.out.println("Computer's choice was Scissors");
                }
            }
        } else if(yourChoice<3) {
            System.out.println("Wrong Choice ........");
        }
    }
}

public class Main {

    public static void main(String[] args)
    {
        System.out.println("Enter 1 for Rock");
        System.out.println("Enter 2 for Paper");
        System.out.print("Enter 3 for scissors\nEnter your choice :  ");

    game1 g=new game1();
        g.getInput();
        g.getCompInput();
        g.getCorrectAnswer();

        }
    }
