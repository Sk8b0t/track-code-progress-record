package com.company;

public class all_max_min {
    public static void main(String[] args) {
          System.out.println("\u001B[31m");
    System.out.println("\u001B[40m");

    String space= "Anna Banana";
System.out.println(space.replaceAll(" ","\b"));
           System.out.println( "Byte min.: " + Byte.MIN_VALUE );           // -128
    System.out.println( "Byte max.: " + Byte.MAX_VALUE );           // 127
    System.out.println( "Char min.: " + (int)Character.MIN_VALUE );      // '\u0000'
    System.out.println( "Char max.: " + (int)Character.MAX_VALUE );      // '\uFFFF'
    System.out.println( "Int min.: " + Integer.MIN_VALUE );         // -2147483648
    System.out.println( "Int max.: " + Integer.MAX_VALUE );         // 2147483647
    System.out.println( "Double min.: " + Double.MIN_VALUE );       // 4.9E-324
    System.out.println( "Double max.: " + Double.MAX_VALUE );       // 1.797...E308

    }
}
//The minimum value of Char is the character with the value of 0.
// This is not the same as the character which represents '0'.
// '0' is ASCII is represented by the bytes with a decimal value of 48
// (see http://www.asciitable.com/).
//The bytes with a value of 0 represent the 'NUL' character
// which will not be output on the console as there's no representation of 'NUL'.
// In fact the first 6 characters in ascii are largely regarded as unprintable characters.
//The decimal value for '0'- 48
//the decimal of 0  is 'null'
