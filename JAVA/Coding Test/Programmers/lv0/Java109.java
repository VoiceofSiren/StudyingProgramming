import java.util.Scanner;

public class Java109 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120836
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
            for (int i = 1; i <= n; i++) {
                if (n%i == 0) {
                    answer += 1;
                }
            }
            return answer;
        }
    }
}

/*
20
 */

/*
100
 */