package com.company;
import java.util.*;
public class Main {
    public static void main(String[] pk) {
        Scanner in = new Scanner(System.in);
        System.out.print("enter a number : ");
        int n = in.nextInt();
        int sum = 0,a=n,n1=n;
        
sum=n;// to find happy number

 do {
    n = sum;
    sum = 0;
    while (n > 0) {
        int r = n % 10;
        sum += r * r;
        n/=10;
    }
}while(sum>=10);


if(sum==1){
    System.out.println( " it is a happy number");}

else
{System.out.println("it is not a happy number");}//end of happy number calculation


        int i=1,t=0;// to find and display prime number
while(i<=a)
{
    if(a%i==0) {

       t++; }
    i++;
}
if(t==2)
    System.out.println("it is a prime number");
else
    System.out.println("it is not a prime number"); //end of prime number calculation

//to find perfect number
      int j=1,sum1=0; //to find perfect number
      while(j<n1){
          if(n1%j==0)
          { sum1+=j; }
          j++;
      }
      if(sum1==n1)
          System.out.println("it is a perfect number");
      else
          System.out.println("it is not a perfect number"); //end of perfect number calculation
}
}
