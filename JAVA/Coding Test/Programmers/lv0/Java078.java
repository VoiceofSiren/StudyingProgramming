import java.util.Scanner;

public class Java078 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181944?language=java
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        if (n%2 == 0) {
            System.out.println(n + " is even");
        } else {
            System.out.println(n + " is odd");
        }
    }
}

/*
100
 */

/*
1
 */