package com.company;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Sayan_ka_Calendar {

    static Sayan_ka_Calendar date(){
        DateTimeFormatter format=DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate d= LocalDate.now();
        System.out.println("\u001B[31m Date : "+d.format(format));
        return null;
    }
    static Sayan_ka_Calendar time(String zone){
         LocalTime time=LocalTime.now(ZoneId.of(zone));
        DateTimeFormatter format=DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("Time:"+time.format(format));
        return null;
    }
    static Sayan_ka_Calendar day(){
        LocalDate day=LocalDate.now();
        DateTimeFormatter format =DateTimeFormatter.ofPattern("E");
        System.out.println("Day: "+day.format(format));
        return null;
    }

    public static void main(String[] args) {
        date();
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the time zone : ");
        String timeZone=in.next();
        time(timeZone);
        day();
    }
}
