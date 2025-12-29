package com.company;
import java.util.Scanner;
public class even_odd {
   int number=0;
    void input(){
        Scanner in=new Scanner(System.in);
        System.out.println("Enter a number : ");
        number=in.nextInt();
        if(calculate(number)==1)
             System.out.println("The numbers contain total even or odd digits.");
        else
            System.out.println("They are mixed");

    }
    int even_count=0,odd_count=0,count=0,r,r1;
     int calculate(int n){
          for(int i=n;i>0;i=i/10) {
              r = i % 10;
              count++;
               if(r%2==0)
           even_count++;
               else
            odd_count++;

          }
      if(even_count==count||odd_count==count)
         return 1;
      else
          return 0;
    }

    public static void main(String[] args) {
        even_odd obj=new even_odd();
        obj.input();
    }
}
