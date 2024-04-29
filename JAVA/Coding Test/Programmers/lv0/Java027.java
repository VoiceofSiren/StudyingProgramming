import java.util.Arrays;
import java.util.Scanner;

public class Java027 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120851
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.solution(my_string));
    }

    private static class Solution {
        public int solution(String my_string) {
            int answer = 0;
            String[] numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
            for (int i = 0; i < my_string.length(); i++) {
                int finalI = i;
                if (Arrays.stream(numbers).anyMatch(s -> s.equals("" + my_string.charAt(finalI)))) {
                    answer += Integer.parseInt("" +my_string.charAt(finalI));
                }
            }
            return answer;
        }
    }
}

// "aAb1B2cC34oOp"
// "1a2b3c4d123"