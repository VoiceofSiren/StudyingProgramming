import java.util.Arrays;
import java.util.Scanner;

public class Java032 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120899
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");

        int[] array = solution.convert(input_arr);

        System.out.println(solution.returnToString(solution.solution(array)));
    }

    private static class Solution {
        public int[] solution(int[] array) {
            int max_value = Arrays.stream(array).max().getAsInt();
            int idx = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] == max_value) {
                    idx = i;
                    break;
                }
            }
            return new int[]{max_value, idx};
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

// [1, 8, 3]
// [9, 10, 11, 8]