package com.company;
//gives all the timezones
import java.sql.Time;
import java.util.Arrays;
import java.util.Calendar;
import java.util.TimeZone;

public class Main {


    public static void main(String[] args) {
//        int b[]={1,2,3,4,5,6,7,8,9,10};
//        System.out.println(Arrays.toString(b));
//        String a[]={"Sundar Pichai","Satya Nadela","Parag Agarwal","Arvind Krishna"};
//        System.out.println(Arrays.toString(a));



TimeZone tz = TimeZone.getTimeZone("America/Los_Angeles");
 TimeZone.setDefault(TimeZone.getTimeZone("Brazil/DeNoronha"));
        System.out.println(TimeZone.getDefault().getID());


        for(String ID:TimeZone.getAvailableIDs())
            System.out.println(ID);
        //                    OR
        //  System.out.println((Arrays.toString(TimeZone.getAvailableIDs())));

Calendar c= Calendar.getInstance();
        System.out.println(c.getTime());
    }
}
