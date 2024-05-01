import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Java064 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181911?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] my_strings = inputString.substring(2, inputString.length() - 2).split("\", \"");

        inputString = scanner.nextLine();
        int[][] parts = stringToIntArray(inputString);


        System.out.println(solution.solution(my_strings, parts));
    }

    private static class Solution {
        public String solution(String[] my_strings, int[][] parts) {
            String answer = "";
            for (int i = 0; i < parts.length; i++) {
                answer += my_strings[i].substring(parts[i][0], parts[i][1] + 1);
            }
            return answer;
        }
    }

    public static int[][] stringToIntArray(String str) {
        return Stream.of(str.substring(2, str.length() - 2).split("], \\["))
                .map(s -> Arrays.stream(s.split(", "))
                        .mapToInt(Integer::parseInt)
                        .toArray())
                .toArray(int[][]::new);
    }
}

/*
["progressive", "hamburger", "hammer", "ahocorasick"]
[[0, 4], [1, 2], [3, 5], [7, 7]]
 */