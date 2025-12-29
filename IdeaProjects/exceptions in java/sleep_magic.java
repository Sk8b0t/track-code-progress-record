package com.company;

public class sleep_magic extends Thread {
    public static void main(String[] args) {
        System.out.print("Loading");
        try {
            for (int i = 0; i < 10; i++) {
                Thread.sleep(500);
                System.out.print(".");
            }
            System.out.println("\nfck");
        }
            catch(Exception e){
                System.out.println(e);
            }

        //System.out.println("------");
    }
}
