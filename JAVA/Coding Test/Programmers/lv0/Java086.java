import java.util.Scanner;

public class Java086 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181847?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String n_str = scanner.nextLine();

        System.out.println(solution.solution(n_str));
    }

    private static class Solution {
        public String solution(String n_str) {
            return "" + Integer.parseInt(n_str);
        }
    }
}

/*
0010
 */

/*
854020
 */