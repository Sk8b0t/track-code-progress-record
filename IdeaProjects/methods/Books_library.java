package com.company;
import java.util.*;

interface useMethods{
    //This methods are used in making this program
    //I uses in the interface to know which methods to implement in a class
    void inputBooksName();
    void showAvailableBooks();
    void setIssueBooks();
    void returnBooks();
}

class Library implements useMethods {
Scanner in=new Scanner(System.in);
    int books = 0, books1 = 0, books3=0;
    String decision, decision2;

   String[] bookName =new String[books];
   String[] issueBooks = new String[2];
   String[] returnBooks = new String[10];

   public void inputBooksName() {
        System.out.print("How many books you want to input : ");
        this.books =in.nextInt();
        bookName=new String[books];
        in.nextLine();

        for (int i = 0; i<bookName.length; i++) {
            System.out.printf("Enter the name of %d book : ", i+1);
            bookName[i]= in.nextLine();
        }
    }

    public void showAvailableBooks() {
        System.out.println("The available books are : ");
        for(int i = 0; i <bookName.length; i++) {
            System.out.println(" * "+ bookName[i]);
        }
    }
int t=0;
    public void setIssueBooks()
    {
        System.out.println("Do you want to issue any book(Y/N)");
        decision = in.next();

        if (decision.equals("Y")) {
            System.out.println("How many books do you want to issue : ");
            books1 = in.nextInt();
            in.nextLine();
            issueBooks = new String[books1];
            for (int i = 0; i < issueBooks.length; i++) {
                System.out.printf("Enter the book %d : ", i + 1);
                issueBooks[i] = in.nextLine();
            }
            for (int i = 0; i < bookName.length; i++) {
                for (int j = 0; j < issueBooks.length; j++) {
                    if (bookName[i].equals(issueBooks[j])) {
                        t++;
                    }
                }
            }
            if (t == books1) {
                System.out.println();
            } else {
                System.out.println("Please  input the book(s) name(s) correctly to issue   !!!!!!\n Try Again");
            }

        } else {
            System.out.println("OK...");

        }
    }
    
int returnNumber=0;

    public void returnBooks() {

        System.out.println("Do you want to return(Y/N)");
        decision2=in.next();

        if (decision2.equals("Y") )
        {
            System.out.println("How many books do wanna return : ");
            books3 = in.nextInt();
            in.nextLine();
            returnBooks=new String[books3];
            System.out.println("Enter the book names :");

            for (int i = 0; i<returnBooks.length; i++) {
                returnBooks[i] = in.nextLine();
            }

            for(int i=0;i< issueBooks.length;i++){
                for(int j=0;j< returnBooks.length;j++){
                    if(issueBooks[i].equals(returnBooks[j])){
                        returnNumber++;}
                    if(returnNumber==books3) {
                        System.out.println();
                    }else{
                        System.out.println("You have not issued one of the book(s)");}
                }}
        }
        else {
            System.out.println("ok....");
        }
    }

    void showAvailableBooksAfterIssueAndReturn() {
        System.out.println("The available books after issuing and returning are : ");


    }
}
public class Books_library {
    public static void main(String[] args) {
Library c=new Library();
        c.inputBooksName();
        c.showAvailableBooks();
        c.setIssueBooks();
        c.returnBooks();
        c.showAvailableBooksAfterIssueAndReturn();
    }
}
