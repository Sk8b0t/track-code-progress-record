package com.company;

public class arre {
    public static void main(String[] args) {
        ZeroValueException z=new ZeroValueException();
        try{
            z.dublicate();
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }

    }
}
class ZeroValueException extends Exception{
    public String getMessage(){
        return "This is an Exception , pls donot input 0";
    }
   void dublicate() throws ZeroValueException {
        int arr[]={1,2,3,2,1,4,7,65,5};
        //checking the array elements whether it contains 0 or not
       for (int i=0;i<arr.length;i++){
           if (arr[i]==0) {
               throw new ZeroValueException();
           }

       }
        for(int i=0;i<arr.length;i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j])
                    arr[j] = 0;
            }
        }
        for (int i:arr) {
            if (i!=0)
                System.out.print(i + "\t");
        }
            }
        }
