import java.util.Arrays;
import java.util.Scanner;

public class Java036 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120908
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String str1 = inputString.substring(1, inputString.length() - 1);

        inputString = scanner.nextLine();
        String str2 = inputString.substring(1, inputString.length() - 1);


        System.out.println(solution.solution(str1, str2));
    }

    private static class Solution {
        public int solution(String str1, String str2) {
            int answer = 2;
            if (str2.length() > str1.length()) {
                return answer;
            }
            int len = str2.length();
            for (int i = 0; i < str1.length() - len + 1; i++) {
                String slice = str1.substring(i, i + len);
                System.out.println(slice);
                if (slice.equals(str2)) {
                    answer = 1;
                    break;
                }
            }
            return answer;
        }
    }
}

/*
"ab6CDE443fgh22iJKlmn1o"
"6CD"
 */

/*
"ppprrrogrammers"
"pppp"
 */

/*
"AbcAbcA"
"AAA"
 */