import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.LinkedList;

public class sheetal {
    public static void main(String[] args) {
       ArrayList <Integer> a=new ArrayList<>();
        LinkedList<Integer>b=new LinkedList<>();
        ArrayDeque<Integer>c=new ArrayDeque<>();
           c.add(3);
        c.add(1233);

            c.add(13);
        c.clone();
        c.element();
        System.out.println( c.poll());
        b.add(0,13);
        b.add(0,123);
        b.pollFirst();
        b.clone();
        System.out.println(b.element());
        System.out.println(b.element());
        System.out.println(b.get(0));
        System.out.println(b.clone());


        }
    }
