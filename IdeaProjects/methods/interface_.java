package com.company;
interface Bicycle{
    int a=45;

    void applyBrake(int decrement);
    void UpSpeed(int increment);
    default void askLisence(String n,int i){
        System.out.println(n+"\t"+i);
    }
}
class AvonCycle implements Bicycle{
    void BlowHorn(int a,int b){
        System.out.printf("a=%d\tb=%d\n",a,b);
        System.out.println("Blowing horn po-po-pe-pe-po-po");
    }
    public void applyBrake(int decrement) {

        System.out.printf("Applying brake of decreasing speed of %d m/s \n",a);
    }
    public void UpSpeed(int increment){
        System.out.printf("increasing speed of %d km/hr\n",a);
    }
}
class Gang extends AvonCycle implements Bicycle{
    @Override
    public void applyBrake(int decrement){
        System.out.println("Applying brake....");
    }
    public void Upspeed(int increment){
        System.out.println("Increasing speed ");
    }
}
public class interface_ {
    public static void main(String[] args) {
        int i=45;
        while(i>0) {
            AvonCycle newCycle = new AvonCycle();
            newCycle.applyBrake(45);
            String sayan = "loll";
            newCycle.askLisence(sayan,234);
            newCycle.UpSpeed(45);
            newCycle.BlowHorn(4, 5);
            Gang newCycle1 = new Gang();
            newCycle1.applyBrake(56);
            newCycle1.Upspeed(12);
            newCycle1.BlowHorn(8, 5);
            i++;
        }
    }
}
