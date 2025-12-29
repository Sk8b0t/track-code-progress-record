package com.company;
import java.util.Scanner;
public class gp2 {
        Scanner in=new Scanner(System.in);
        float r=0.0f,t=0.0f,n=0.0f;
        float[]A;

        void getInput() {
            System.out.println("How many terms do you want to input : ");
            n = in.nextFloat();
            A=new float[(int) n];
            for(int i=0;i<A.length;i++){
                System.out.printf("Enter the number %d:  ", i+1);
                A[i]=in.nextInt();
                System.out.println();
            }
            r=A[1]/A[0];
        }

        void checkArray(){
        for(int i=0;i<A.length-1;i++){
            if(A[i+1]/A[i]==r) {
                t++;}
        }
        }

        void getOutput() {
            if (t == A.length - 1) {
                System.out.println("Enter the term which you want to know :");
               int input1 = in.nextInt();
                float output = (float) (A[0] * Math.pow(r, input1-1));
                System.out.println("Common difference : "+r+"\tfirst term :"+ A[0]);
                System.out.printf("\nThe %d term : %f", input1, output);
            } else {
                System.out.println("Wrong G.P sequence...");
            }
        }

    public static void main(String[] args) {
        gp2 g=new gp2();
        g.getInput();
        g.checkArray();
        g.getOutput();
    }

    }

