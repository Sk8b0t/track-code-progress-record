package com.company;
 //0-s.k Biswas
//1- sambhu
//2-ahmed
//3-dibakar
//4-majhi
//5-S. C. Hembram

public class class_routine {

        String[] Names = {"S.K BISWAS", "SAMBHU PRASAD", "E.AHMED", "DIBAKAR BISWAS", "T.R MAJHI", "S. C. Hembram"};
        long[] B = {1666143214, 1562074430, 1665978872, 1664794894, 1654395227, 1760502786};
        int[] input = new int[6];

    void generate() {
        for (int i = 0; i < Names.length; i++) {
            input[i] = (int) (Math.random() * 6);
        }
    }



int number=0;
    int t=0;

void output(){
    for(int i=0;i< input.length;i++)
    {

    if(input[i]==0){
        number=input[i];
    t++;

    if(t==1)
         System.out.println("1st class (09:15 - 10:00)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==2)
         System.out.println("2nd class (10:00- 10:45)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==3)
         System.out.println("3rd class (10:45- 11:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==4)
         System.out.println("4th class (14:45 -  15:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==5)
         System.out.println("5th class (15:30 - 16:15)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==6)
         System.out.println("6th class (16:15 - 17:00)\t"+Names[number]+ "\t\t"+B[number]);
    }

    else if(input[i]==1) {
        number = input[i];

        t++;

        if (t == 1)
            System.out.println("1st class (09:15 - 10:00)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 2)
            System.out.println("2nd class (10:00- 10:45)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 3)
            System.out.println("3rd class (10:45- 11:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 4)
            System.out.println("4th class (14:45 -  15:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 5)
            System.out.println("5th class (15:30 - 16:15)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 6)
            System.out.println("6th class (16:15 - 17:00)\t" + Names[number] + "\t\t" + B[number]);
    }


    else if(input[i]==2) {

        number = input[i];
        t++;

        if (t == 1)
            System.out.println("1st class (09:15 - 10:00)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 2)
            System.out.println("2nd class (10:00- 10:45)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 3)
            System.out.println("3rd class (10:45- 11:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 4)
            System.out.println("4th class (14:45 -  15:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 5)
            System.out.println("5th class (15:30 - 16:15)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 6)
            System.out.println("6th class (16:15 - 17:00)\t" + Names[number] + "\t\t" + B[number]);
    }
    else if(input[i]==3) {
        number = input[i];
        t++;

        if (t == 1)
            System.out.println("1st class (09:15 - 10:00)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 2)
            System.out.println("2nd class (10:00- 10:45)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 3)
            System.out.println("3rd class (10:45- 11:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 4)
            System.out.println("4th class (14:45 -  15:30)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 5)
            System.out.println("5th class (15:30 - 16:15)\t" + Names[number] + "\t\t" + B[number]);
        else if (t == 6)
            System.out.println("6th class (16:15 - 17:00)\t" + Names[number] + "\t\t" + B[number]);
    }
   else if(input[i]==4){

        number=input[i];
        t++;

    if(t==1)
         System.out.println("1st class (09:15 - 10:00)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==2)
         System.out.println("2nd class (10:00- 10:45)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==3)
         System.out.println("3rd class (10:45- 11:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==4)
         System.out.println("4th class (14:45 -  15:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==5)
         System.out.println("5th class (15:30 - 16:15)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==6)
         System.out.println("6th class (16:15 - 17:00)\t"+Names[number]+ "\t\t"+B[number]);
   }
   else if(input[i]==5){

        number=input[i];
        t++;

    if(t==1)
         System.out.println("1st class (09:15 - 10:00)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==2)
         System.out.println("2nd class (10:00- 10:45)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==3)
         System.out.println("3rd class (10:45- 11:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==4)
         System.out.println("4th class (14:45 -  15:30)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==5)
         System.out.println("5th class (15:30 - 16:15)\t"+Names[number]+ "\t\t"+B[number]);
    else if(t==6)
         System.out.println("6th class (16:15 - 17:00)\t"+Names[number]+ "\t\t"+B[number]);
   }
    }
}

    public static void main(String[] args) {

        System.out.println(   "JOINING ID’S FOR ONLINE CLASSES ON DATE : 15.04.2021, PRO TE/ECRC/CC 01/21(B)");
         System.out.println("------------------------------------------------------");
        System.out.println("CLASS SCHEDULE\t\t\t\tINSTRUCTORS\t\t\tJOINING IDs");
        class_routine obj=new class_routine();
        instructor_maintain obj1=new instructor_maintain();
        obj.generate();
        obj1.check();
        obj.output();
         System.out.println("------------------------------------------------------");
    }
}
