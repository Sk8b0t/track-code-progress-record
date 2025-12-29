package com.company;
//What if we extend and implement thread to same class ??
//Lets see what happens:-->
class MyNewThread extends Thread implements Runnable {

    MyNewThread(String name) {
        super(name);
    }

    public void run() {
     //   System.out.println("Thread 1: " + this.getName());
        System.out.println("Thread : "+ Thread.currentThread().getName());
    }
}
public class experiment {
    public static void main(String[] args) {
                MyNewThread t=new MyNewThread("Sayan 1");
                  t.start();                //--> Prints Sayan 1
                Thread t2=new Thread(t,"Sayan Biswas 2");
                t2.start();           //--> Prints Sayan 2 (it accepts the 1st object)
                Thread t3=new Thread(new MyNewThread("sayan 3"));
                t3.start();      //--> Prints Thread 0 (no String is passed as per syntax i.e Thread(target object, String name))
          Thread t4 = new myThread(new MyNewThread("sayan biswas"), "Sayan");
                t4.start();             //--> Serious Doubt

//                       DOUBTS REGARDING THE 3RD THREAD :
//         --> What the hell it does with the string passed in the object??
//-->  if no string is passed in the constructor ,then why it does not call the default constructor??



//                     DOUBTS REGARDING THE 4TH THREAD :
//        Thread t4 = new myThread(new MyNewThread("sayan biswas"), "Sayan")
//--> Why this object creation leads to a loop which prints "Sayan" infinitily???#doubt



//What is the meaning of this piece of code :
//Thread.currentThread().getName();

        // CONCLUSION : The Runnable interface is not commonly used , extending thread class is mostly used by the people
    }
}
