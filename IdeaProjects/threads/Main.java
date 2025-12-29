package com.company;
//by extending thread class
class myThread extends Thread{
    myThread(MyNewThread sa, String name){
        super(name);
    }
    public void run(){
        while(true)
         //   System.out.println(this.getName());
            System.out.println(Thread.currentThread().getName());
    }
}

public class Main {

    public static void main(String[] args) {
        myThread sheetal=new myThread(new MyNewThread("sa"), "Sheetal Priya Barjo");
        myThread sayan=new myThread(new MyNewThread("sa"), "Sayan Biswas");
          myThread shresth=new myThread(new MyNewThread("sa"), "Shresth Jaiswal");
          sheetal.setPriority(Thread.MAX_PRIORITY);
           sayan.setPriority(Thread.NORM_PRIORITY);
            shresth.setPriority(Thread.MIN_PRIORITY);
            sheetal.start();
            sayan.start();
            shresth.start();

    }
}
