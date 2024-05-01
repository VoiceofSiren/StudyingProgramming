import java.util.Scanner;

public class Java072 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181935?language=java
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
            if (n%2 == 1) {
                for (int i = 1; i <= n; i += 2) {
                    answer += i;
                }
            } else {
                for (int i = 0; i <= n; i += 2) {
                    answer += (int) Math.pow(i, 2);
                }
            }
            return answer;
        }
    }
}

/*
7
 */

/*
10
 */