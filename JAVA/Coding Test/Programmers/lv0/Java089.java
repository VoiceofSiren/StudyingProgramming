import java.util.Scanner;

public class Java089 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181845?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        System.out.println(solution.solution(n));
    }

    private static class Solution {
        public String solution(int n) {
            return "" + n;
        }
    }
}

/*
123
 */

/*
2573
 */