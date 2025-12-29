package com.company;

public class remove_duplicated {
        char ch = ' ';
        String n = "9110202";
          char A[]=new char[n.length()];

void input() {
    for (int i = 0; i < n.length(); i++) {
        ch = n.charAt(i);
        A[i] = ch;}
}

void calculate() {
    for (int i = 0; i < n.length(); i++) {
        for (int j = i + 1; j < n.length(); j++) {
            if (A[i] == A[j])
                A[j] =0;}}
    //there is a difference between 0 and '0' 😎
//   0-'null' and '0'- 48
    }

void output(){
    System.out.println("\u001B[31m");
    System.out.println("\u001B[40m");
    for(char c:A)
                  if(c==0)
                      continue;
                  else
                      System.out.print(c);
                  System.out.println("\u001B[40m");
}

    public static void main(String[] args) {
        remove_duplicated a=new remove_duplicated();
        a.input();
        a.calculate();
        a.output();


    }
}