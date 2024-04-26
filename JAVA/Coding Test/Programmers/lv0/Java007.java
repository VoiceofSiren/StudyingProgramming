import java.util.Arrays;
import java.util.Scanner;

public class Java007 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120820
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        int age = scanner.nextInt();
        System.out.println(solution.solution(age));
    }

    private static class Solution {
        public int solution(int age) {
            return 2022 - age + 1;
        }
    }
}

// 40
// 23