/*
        Intro to Java
        Simple code 1
*/
import java.util.Scanner;
class Example {
        // This is a simple program to get acquanted with the user
        public static void main(String args[]){
                String name;
                name= "Ben";
                System.out.println("Hello "+ name);
                System.out.println("Finding your age!");

        // FInding the age of the user
                Scanner in = new Scanner(System.in);
                System.out.print("What is your birth year?: ");
                int b_year = in.nextInt();
                System.out.println(b_year);
        // Find the current year

        }
}
