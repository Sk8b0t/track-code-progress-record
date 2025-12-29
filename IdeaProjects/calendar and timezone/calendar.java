package com.company;

import java.util.*;

public class calendar {
    public static void main(String[] args) {
        TimeZone t= TimeZone.getTimeZone("GMT-8");
        System.out.println(t);

        Calendar c= Calendar.getInstance(TimeZone.getTimeZone("Asia/Calcutta"));
        System.out.printf("%d:%d:%d\n",c.get(Calendar.HOUR_OF_DAY),c.get(Calendar.MINUTE),c.get(Calendar.SECOND));

        GregorianCalendar g=new GregorianCalendar();
        System.out.println(g.getTimeZone());
        Date d=new Date();
        System.out.println(d);
        System.out.println(c.get(Calendar.DATE));
        System.out.println(c.get(Calendar.YEAR));

        year y=year.check();
        year y1=(year)year.hello("Hello ");
       System.out.println(y);
    }
}
abstract class year{
    static year check(){
        System.out.println("Checked...its fine ");
        return null;
    }
    static Object hello(String i){
        System.out.println("Checked..its fine "+i);
        return null;
    }
    int area(int a,int b){
        return a*b;
    }
}

