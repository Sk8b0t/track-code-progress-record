package com.company;

public class instructor_maintain {
       String[] Names = {"S.K BISWAS", "SAMBHU PRASAD", "E.AHMED", "DIBAKAR BISWAS", "T.R MAJHI", "S. C. Hembram"};
        long[] B = {1666143214, 1562074430, 1665978872, 1664794894, 1654395227, 1760502786};
        int[] input = new int[6];
     void check() {
         class_routine obj=new class_routine();
         obj.generate();
        int t = 0, s = 0, u = 0, v = 0, r = 0, q = 0;
        for (int i = 0; i < input.length; i++) {
            boolean k = false;
            if (input[i] == 2) {
                t++;
                if (t > 2) {
                    while (k != true) {
                        input[i] = (int) (Math.random() * 6);
                        if (input[i] != 2)
                            k = true;
                        else
                            k = false;
                    }
                } else {
                    continue;
                }
            }

            if (input[i] == 1) {
                s++;
                if (s > 2) {
                    while (k != true) {
                        input[i] = (int) (Math.random() * 6);
                        if (input[i] != 1)
                            k = true;
                        else
                            k = false;
                    }
                }
            } else {
                continue;
            }
        }
    }

}
