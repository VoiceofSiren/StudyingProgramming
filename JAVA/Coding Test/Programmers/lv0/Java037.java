import java.util.Scanner;

public class Java037 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120909
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        System.out.println(solution.solution(n));
    }

    private static class Solution {
        public int solution(int n) {
            int answer = 2;
            int root = (int) Math.pow(n, 0.5);
            if (n == (int) Math.pow(root, 2)) {
                answer = 1;
            }
            return answer;
        }
    }
}

// 144
// 976