import java.util.Arrays;
import java.util.Scanner;

public class Java042 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181868?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String my_string = inputString.substring(1, inputString.length() - 1);

        System.out.println(solution.returnToString(solution.solution(my_string)));
    }

    private static class Solution {
        public String[] solution(String my_string) {
            String[] result = Arrays.stream(my_string.split(" "))
                    .filter(str -> !str.equals(""))
                    .map(String::new)
                    .toArray(String[]::new);
            return result;
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

// " i    love  you"
// "    programmers  "