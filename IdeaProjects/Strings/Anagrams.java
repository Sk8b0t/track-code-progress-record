package com.company;
import java.util.Scanner;
public class Anagrams
{

	String n="sayan",m="nayas";
	char []A=new char[n.length()];
	char[]B=new char[m.length()];
	void checkLength(){
		if(n.length()!=m.length()) {
			System.out.println("Not an anagram");
			System.exit(1);
		}
		else{
			System.out.println();
		}
	}
	void toCharArray(){
		for(int i=0;i<A.length;i++) {
			A[i] = n.charAt(i);
			B[i] = m.charAt(i);
		}
		}
		int min=0,min1=0;
	char c=' ',c1=' ';
		void sort() {

			//To sort the 1st array
			for (int i = 0; i < A.length; i++) {
				min = i;
				min1 = i;
				for (int j = i + 1; j < A.length; j++) {
					if (A[min]> A[j])
						min = j;
				}
				c = A[i];
				A[i] = A[min];
				A[min] = c;
			}
			//To sort the second array
			for (int i = 0; i < B.length; i++) {
				min1 = i;
				for (int j = i + 1; j < B.length; j++) {
					if (B[min1]> B[j])
						min1 = j;
				}
				c1 = B[i];
				B[i] = B[min1];
				B[min1] = c1;
			}
		}
		void output(){
			String str="",str1="";
			for(char c:A)
				str+=c;
			for (char c:B)
				str1+=c;
			//System.out.println(str+"\t"+ str1);
			if(str1.equals(str))
				System.out.println("Anagram ");
			else
				System.out.println("Not an Anagram");
		}
	public static void main(String[] args)
	{
	}




}