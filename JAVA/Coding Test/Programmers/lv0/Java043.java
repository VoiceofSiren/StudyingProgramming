import java.util.Arrays;
import java.util.Scanner;

public class Java043 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181869?language=java
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
            return my_string.split(" ");
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

// "i love you"
// "programmers"