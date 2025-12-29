package com.company;
import java.util.Random;
public class abc {
    public static void main(String[] args) {
        int [][][]A=new int [3][2][4];
Random r=new Random();
for(int i=0;i<A.length;i++){
    for(int j=0;j<A[i].length;j++){
        for(int k=0;k<A[i][j].length;k++)
            A[i][j][k] = i+j+k++;
        }
    }

for(int [][]i2:A){
for(int []i:i2) {
    for (int i1 : i)
        System.out.print("\u001B[31m"+i1 + "\t");
    System.out.println();
}
    System.out.println("--------------");
}


    }

}
        //System.out.println("Sayan\n".repeat(100));


