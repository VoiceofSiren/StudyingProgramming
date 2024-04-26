import java.util.Arrays;
import java.util.Scanner;

public class Java010 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120831
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        System.out.println(solution.solution(n));
    }

    private static class Solution {
        public int solution(int n) {
            int answer = 0;
            for (int i = 0; i <= n; i += 2) {
                answer += i;
            }
            return answer;
        }
    }
}

// 10
// 4