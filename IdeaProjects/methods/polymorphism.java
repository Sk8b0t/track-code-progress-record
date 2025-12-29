package com.company;

import java.util.Scanner;

interface wifi{
    void getNetworks();
}
interface camera{
    private void greet(){
        System.out.println("Good afternoon");
    }
    default void printGreet(){
        greet();
    }
    void takePhoto();
    void recordVideo();
    void takePortrait();
}
interface gps{
    void getLocation();
}
class cellphone{
    Scanner in=new Scanner(System.in);
    void callNumber(){
        System.out.println("Enter your number : ");
        long PhoneNumber=in.nextLong();
        System.out.println("calling "+ PhoneNumber );

    }
    void ring(){
        System.out.println("Ringing.....");
    }
}
class smartphone extends cellphone implements wifi,camera,gps
{

   public void getNetworks(){
        String[]networks={"Sayan","Shresth","Ronit"};
        for (String element : networks) {
            System.out.printf("getting wifi of %s\n", element);}
    }

   public void takePhoto(){
        System.out.println("Clicking photo...");
    }
    public void recordVideo(){
        System.out.println("Recording video");
    }
   public void takePortrait(){
        System.out.println("Taking a portrait shot...");
    }
  public   void getLocation(){
        System.out.println("I dont know your location , turn on GPS");
    }

}
public class polymorphism {
    public static void main(String[] args) {

        //ek interface call karke usmai dusra interface ka method call nhi kr sakte h in smartphone class
       wifi w=new smartphone(); //calling wifi interface in smartphone class
        w.getNetworks();

        gps g=new smartphone();
        g.getLocation();

        cellphone nokia=new smartphone(); //calling nokia class in smartphone method
        nokia.callNumber();

        smartphone pixel6=new smartphone();
        pixel6.takePhoto();
        pixel6.getNetworks();
        pixel6.getLocation();
        pixel6.getNetworks();
        pixel6.recordVideo();
        Scanner in=new Scanner(System.in);
        camera c=new smartphone();
        c.recordVideo();
        c.takePortrait();
    }
}
