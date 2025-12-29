package com.company;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

public class java_time {
    static java_time SayanFormat(){


// PRACTICE
        LocalDateTime dt= LocalDateTime.now();
        DateTimeFormatter df=DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println("Date : "+dt.format(df));

        LocalTime t=LocalTime.now();
        DateTimeFormatter f=DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("Time : "+t.format(f));

        LocalDate d=LocalDate.now();
         DateTimeFormatter d2=DateTimeFormatter.ofPattern("E");
        System.out.println("Day :"+d.format(d2));

         ZonedDateTime z=ZonedDateTime.now();
        DateTimeFormatter df2=DateTimeFormatter.RFC_1123_DATE_TIME;
        System.out.println(z.format(df2));

        return null;
    }

    public static void main(String[] args) {
        SayanFormat();
    }
}
