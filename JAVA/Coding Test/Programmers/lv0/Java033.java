import java.util.Arrays;
import java.util.Scanner;

public class Java033 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120903
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] s1 = inputString.substring(2, inputString.length() - 2).split("\", \"");

        inputString = scanner.nextLine();
        String[] s2 = inputString.substring(2, inputString.length() - 2).split("\", \"");


        System.out.println(solution.solution(s1, s2));
    }

    private static class Solution {
        public int solution(String[] s1, String[] s2) {
            int answer = 0;
            for (String s: s1) {
                if (Arrays.stream(s2).anyMatch(str -> str.equals(s))) {
                    answer += 1;
                }
            }
            return answer;
        }
    }
}

/*
["a", "b", "c"]
["com", "b", "d", "p", "c"]
 */

/*
["n", "omg"]
["m", "dot"]
 */