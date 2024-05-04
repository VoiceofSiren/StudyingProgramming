import java.util.Scanner;

public class Java105 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120822
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String my_string = scanner.nextLine();

        System.out.println(solution.solution(my_string));
    }

    private static class Solution {
        public String solution(String my_string) {
            String answer = "";
            for (int i = my_string.length() - 1; i >= 0; i--) {
                answer += "" + my_string.charAt(i);
            }
            return answer;
        }
    }
}

/*
jaron
 */

/*
bread
 */