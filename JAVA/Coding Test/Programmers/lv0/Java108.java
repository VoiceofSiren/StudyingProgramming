import java.util.Arrays;
import java.util.Scanner;

public class Java108 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120824
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] num_list = solution.convert(strArr);

        System.out.println(solution.returnToString(solution.solution(num_list)));
    }

    private static class Solution {
        public int[] solution(int[] num_list) {
            int[] answer = {0, 0};
            for (int num: num_list) {
                if (num%2 == 0) {
                    answer[0] += 1;
                } else {
                    answer[1] += 1;
                }
            }
            return answer;
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
        }

        public String returnToString(int[] numbers) {
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
[1, 2, 3, 4, 5]
 */

/*
[1, 3, 5, 7]
 */