import java.util.Scanner;

public class Java081 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120823?language=java
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            if (i != n) {
                System.out.println();
            }
        }
    }
}

/*
3
 */