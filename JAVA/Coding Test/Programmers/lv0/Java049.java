import java.util.Scanner;

public class Java049 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181878?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String myString = inputString.substring(1, inputString.length() - 1);

        inputString = scanner.nextLine();
        String pat = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(myString, pat));
    }

    private static class Solution {
        public int solution(String myString, String pat) {
            myString = myString.toLowerCase();
            pat = pat.toLowerCase();
            if (pat.length() > myString.length()) {
                return 0;
            } else {
                for (int i = 0; i < myString.length() - pat.length() + 1; i++) {
                    if (myString.substring(i, i + pat.length()).equals(pat)) {
                        return 1;
                    }
                }
                return 0;
            }
        }
    }
}

/*
"AbCdEfG"
"aBc"
 */

/*
"aaAA"
"aaaaa"
 */