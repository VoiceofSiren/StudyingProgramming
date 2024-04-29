import java.util.Scanner;

public class Java030 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120893
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(my_string));
    }

    private static class Solution {
        public String solution(String my_string) {
            String answer = "";
            for (int i = 0; i < my_string.length(); i++) {
                String alphabet = "" + my_string.charAt(i);
                // 소문자일 경우
                if (alphabet.equals(alphabet.toLowerCase())) {
                    answer += alphabet.toUpperCase();
                }
                // 대문자일 경우
                else {
                    answer += alphabet.toLowerCase();
                }
            }
            return answer;
        }
    }
}

// "cccCCC"
// "abCdEfghIJ"