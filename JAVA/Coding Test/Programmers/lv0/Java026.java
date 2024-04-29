import java.util.Arrays;
import java.util.Scanner;

public class Java026 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120849
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
            String[] vowels = {"a", "e", "o", "u", "i"};
            for (int i = 0; i < my_string.length(); i++) {
                int finalI = i;
                if (Arrays.stream(vowels).anyMatch(s -> s.equals("" + my_string.charAt(finalI)))) {
                    continue;
                } else {
                    answer += my_string.charAt(i);
                }
            }
            return answer;
        }
    }
}

// "bus"
// "nice to meet you"