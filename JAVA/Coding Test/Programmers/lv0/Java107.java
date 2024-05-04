import java.util.Scanner;

public class Java107 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120895
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String my_string = scanner.nextLine();
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        System.out.println(solution.solution(my_string, num1, num2));
    }

    private static class Solution {
        public String solution(String my_string, int num1, int num2) {
            String answer = "";
            String s1 = "" + my_string.charAt(num1);
            String s2 = "" + my_string.charAt(num2);

            for (int i = 0; i < my_string.length(); i++) {
                if (i == num1) {
                    answer += s2;
                } else if (i == num2) {
                    answer += s1;
                } else {
                    answer += "" + my_string.charAt(i);
                }
            }
            return answer;
        }
    }
}

/*
hello
1
2
 */

/*
I love you
3
6
 */