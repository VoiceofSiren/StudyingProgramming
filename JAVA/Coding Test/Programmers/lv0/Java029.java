import java.util.Arrays;
import java.util.Scanner;

public class Java029 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120892
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String cipher = inputString.substring(1, inputString.length() - 1);
        int code = scanner.nextInt();
        System.out.println(solution.solution(cipher, code));
    }

    private static class Solution {
        public String solution(String cipher, int code) {
            String answer = "";
            for (int i = 0; i < cipher.length(); i++) {
                if (i%code == code - 1) {
                    answer += cipher.charAt(i);
                }
            }
            return answer;
        }
    }
}

/*
"dfjardstddetckdaccccdegk"
4
 */

/*
"pfqallllabwaoclk"
2
 */