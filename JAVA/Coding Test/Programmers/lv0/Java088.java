import java.util.Arrays;
import java.util.Scanner;

public class Java088 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181849?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String num_str = scanner.nextLine();

        System.out.println(solution.solution(num_str));
    }

    private static class Solution {
        public int solution(String num_str) {
            int answer = 0;
            for (int i = 0; i < num_str.length(); i++) {
                answer += Integer.parseInt("" + num_str.charAt(i));
            }
            return answer;
        }
    }
}

/*
123456789
 */

/*
1000000
 */