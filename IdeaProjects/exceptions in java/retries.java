package com.company;

import java.util.Scanner;

class MaxRetriesException extends Exception {
    Scanner in = new Scanner(System.in);

    public String getMessage() {
        return "the retries has been exceeded";
    }

    public void access() throws MaxRetriesException {
        int arr[] = {12, 3, 4, 5, 3};
        int i = 0;
        while (i < 5) {

            try {
                System.out.print("Enter the index : ");
                int index = in.nextInt();
                System.out.println("Index value= " + arr[index]);
                break;
            } catch (Exception e) {
                System.out.println("Enter a valid index");
                i++;
            }
            if (i >= 5) {
                throw new MaxRetriesException();
            }
        }

    }
}
public class retries {
    public static void main(String[] args) {
        MaxRetriesException n=new MaxRetriesException();
        try{
            n.access();
    }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}
