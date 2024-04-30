import java.util.Arrays;
import java.util.Scanner;

public class Java051 {
    /*
    https://school.programmers.co.kr/learn/courses/30/lessons/181882?language=java
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);

        String inputString = scanner.nextLine();
        String[] input_arr = inputString.substring(1, inputString.length() - 1).split(", ");
        int[] arr = solution.convert(input_arr);

        System.out.println(solution.returnToString(solution.solution(arr)));
    }

    private static class Solution {
        public int[] solution(int[] arr) {
            int[] result = new int[arr.length];

            final int[] idx = {0};
            Arrays.stream(arr).forEach(num -> {
                if (num%2 == 0) {
                    if (num >= 50) {
                        result[idx[0]] = num/2;
                    } else {
                        result[idx[0]] = num;
                    }
                } else {
                    if (num < 50) {
                        result[idx[0]] = num*2;
                    } else {
                        result[idx[0]] = num;
                    }
                }
                idx[0] += 1;
            });
            return result;
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

// [1, 2, 3, 100, 99, 98]