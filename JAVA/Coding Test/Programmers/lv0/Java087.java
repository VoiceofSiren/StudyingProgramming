import java.util.Arrays;
import java.util.Scanner;

public class Java087 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181870?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(2, inputString.length() - 2).split("\",\"");

        System.out.println(solution.returnToString(solution.solution(strArr)));
    }

    private static class Solution {
        public String[] solution(String[] strArr) {
            return Arrays.stream(strArr)
                    .filter(str -> !contains_ad(str))
                    .toArray(String[]::new);
        }

        public boolean contains_ad(String str) {
            for (int i = 0; i < str.length() - 1; i++) {
                String slice = str.substring(i, i + 2);
                if (slice.equals("ad")) {
                    return true;
                }
            }
            return false;
        }

        public String returnToString(String[] numbers) {
            String result = "[";
            if (numbers.length == 1) {
                result += numbers[0];
            } else {
                for (int i = 0; i < numbers.length - 1; i++) {
                    result += numbers[i] + ", ";
                }
                result += numbers[numbers.length - 1];
            }
            result += "]";
            return result;
        }
    }
}

/*
["and","notad","abcd"]
 */

/*
["there","are","no","a","ds"]
 */