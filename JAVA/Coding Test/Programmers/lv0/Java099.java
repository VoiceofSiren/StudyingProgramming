import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Java099 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/120862
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] strArr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] numbers = solution.convert(strArr);

        System.out.println(solution.solution(numbers));
    }

    private static class Solution {
        public Integer solution(int[] numbers) {
            List<Integer> answer = new ArrayList<>();
            for (int i = 0; i < numbers.length - 1; i++) {
                for (int j = i + 1; j < numbers.length; j++) {
                    answer.add(numbers[i] * numbers[j]);
                }
            }
            Integer[] arr = answer.stream().toArray(Integer[]::new);
            return get_max(arr);
        }

        public Integer get_max(Integer[] arr) {
            Integer max_value = -100000000;
            for (int i = 0; i < arr.length; i++) {
                max_value = Math.max(max_value, arr[i]);
            }
            return max_value;
        }

        public int[] convert(String[] input_arr) {
            int[] num_list = new int[input_arr.length];
            for (int i  = 0; i < input_arr.length; i++) {
                num_list[i] = Integer.parseInt(input_arr[i]);
            }
            return num_list;
        }
    }
}

/*
[1, 2, -3, 4, -5]
 */

/*
[0, -31, 24, 10, 1, 9]
 */

/*
[10, 20, 30, 5, 5, 20, 5]
 */