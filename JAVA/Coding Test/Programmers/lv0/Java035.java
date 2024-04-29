import java.util.Arrays;
import java.util.Scanner;

public class Java035 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120906
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
            while (n > 0) {
                answer += n%10;
                n /= 10;
            }
            return answer;
        }
    }
}

// 1234
// 930211