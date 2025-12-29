package com.company;
class myThread2 implements Runnable{
   // myThread2(Runnable r, String name){
    public void run(){
        System.out.println("Sheetal\n");
        System.out.println("Thread name : "+Thread.currentThread().getName());
    }
}
public class runnable {
    public static void main(String[] args) {
Thread t=new Thread(new myThread2(),"My Sheetal Priya");
t.start();


    }
}
