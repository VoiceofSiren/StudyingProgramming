import java.util.Scanner;

public class Java022 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120825
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String my_string = scanner.nextLine();
        int n = scanner.nextInt();

        System.out.println(solution.solution(my_string, n));
    }

    private static class Solution {
        public String solution(String my_string, int n) {
            String answer = "";

            for (int i = 0; i < my_string.length(); i++) {
                for (int j = 0; j < n; j++) {
                    answer += my_string.charAt(i);
                }
            }
            return answer;
        }
    }
}

/*
hello
3
 */