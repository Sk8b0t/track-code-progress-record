package com.company;
//making the game with GUI java.awt
import javax.swing.*;
public class guess_no_gui
{
    public static void main(String[] args) {
        int computerChoice=(int)((Math.random()*3)+1);
        int userInput=0;
        System.out.println("The correct guess would be "+ computerChoice);
        int count =1;
        while(userInput!=computerChoice){
            String response=JOptionPane.showInputDialog(null,"Enter a gues between 1 to 3" + " ","Guessing game",3);
            userInput=Integer.parseInt(response);
            JOptionPane.showMessageDialog(null,""+ determineGuess(userInput,computerChoice,count));
            count++;
        }
    }
    public static String
    determineGuess(int userAnswer,int computerNumber,int count){
        if(userAnswer<=0 || userAnswer>3){
            return "Your guess is invalid";}
            else if(userAnswer==computerNumber) {
            return "Your choice is right.\nTotal guesses : " + count;
        }else if(userAnswer<computerNumber){
                return "Your guess is too low, Try again later.\nTry number: "+ count;}
            else {
                return "Your guess is incorrect.\nTry number: "+ count;
            }

    }
}
